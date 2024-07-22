import configparser
import openai
import os
import csv
import re
import asyncio
from tiktoken import get_encoding
from google.colab import userdata

# Access the OpenAI API key from secrets
api_key = userdata.get('openai_api_key')

# Initialize the tokenizer for GPT-2
tokenizer = get_encoding("gpt2")

# Use the API key to create the asynchronous client
client = openai.AsyncClient(api_key=api_key)

async def process_line(client, input_line, system_message_content, user_message_template, model, response_settings):
    user_message_content = user_message_template.format(input_line=input_line)
    prompt = f"{system_message_content}\n{user_message_content}"
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message_content},
            {"role": "user", "content": user_message_content}
        ],
        temperature=response_settings['temperature'],
        max_tokens=response_settings['max_tokens'],
        top_p=response_settings['top_p'],
        frequency_penalty=response_settings['frequency_penalty'],
        presence_penalty=response_settings['presence_penalty']
    )
    output = response.choices[0].message.content.strip()

    prompt_tokens = tokenizer.encode(prompt)
    output_tokens = tokenizer.encode(output)

    return output, len(prompt_tokens), len(output_tokens)

def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

async def process_chunks(client, chunk, system_message_content, user_message_template, model, response_settings, output_keys):
    tasks = [process_line(client, line, system_message_content, user_message_template, model, response_settings) for line in chunk]
    results = await asyncio.gather(*tasks)
    formatted_results = []
    for input_line, (output, prompt_tokens, output_tokens) in zip(chunk, results):
        parsed_output = parse_output(output, output_keys)
        result = {
            "Model": model,
            "Input Line": input_line,
            "Output": output,
            "Prompt Tokens": prompt_tokens,
            "Output Tokens": output_tokens
        }
        for key in output_keys:
            result[key] = parsed_output.get(key, "Unknown")
        formatted_results.append(result)
    return formatted_results

async def process_batches(config_file, system_prompt_file, user_prompt_file, input_file, output_location, file_prefix, chunk_size=100):
    config = configparser.ConfigParser()
    config.read(config_file)
    try:
        models = [value for key, value in config.items('models')]
    except configparser.NoSectionError:
        raise ValueError("The 'models' section is missing in the configuration file.")

    response_settings = {
        'temperature': config.getfloat('response_settings', 'temperature'),
        'max_tokens': config.getint('response_settings', 'max_tokens'),
        'top_p': config.getfloat('response_settings', 'top_p'),
        'frequency_penalty': config.getfloat('response_settings', 'frequency_penalty'),
        'presence_penalty': config.getfloat('response_settings', 'presence_penalty')
    }

    system_message_content = read_prompt_from_file(system_prompt_file)
    user_message_template = read_prompt_from_file(user_prompt_file)
    input_lines_list = read_lines_from_file(input_file)

    if not os.path.exists(output_location):
        os.makedirs(output_location, exist_ok=True)
        print(f"Created output directory: {output_location}")

    openai.api_key = api_key
    output_keys = get_output_keys(system_message_content)

    for model in models:
        for chunk in chunk_list(input_lines_list, chunk_size):
            results = await process_chunks(client, chunk, system_message_content, user_message_template, model, response_settings, output_keys)
            # Output results to a file
            output_file_path = f'{output_location}/{file_prefix}_{model}_results.csv'
            with open(output_file_path, 'a', newline='') as csvfile:
                fieldnames = list(results[0].keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                if csvfile.tell() == 0:  # Write header only if file is empty
                    writer.writeheader()
                for result in results:
                    writer.writerow(result)
            print(f"Batch results saved to {output_file_path}")
