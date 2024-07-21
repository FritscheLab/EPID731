import configparser
import openai
import os
import csv
import re
from tiktoken import get_encoding
from google.colab import userdata

# Access the OpenAI API key from secrets
api_key = userdata.get('openai_api_key')

# Initialize the tokenizer for GPT-2
tokenizer = get_encoding("gpt2")

def process_line(client, input_line, system_message_content, user_message_template, model, response_settings):
    # Construct the user message content
    user_message_content = user_message_template.format(input_line=input_line)
    # Construct the full prompt
    prompt = f"{system_message_content}\n{user_message_content}"
    response = client.chat.completions.create(
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

    # Tokenize and count tokens for input and output separately
    prompt_tokens = tokenizer.encode(prompt)
    output_tokens = tokenizer.encode(output)

    return output, len(prompt_tokens), len(output_tokens)

def read_lines_from_file(file_path):
    """
    Reads lines from a given file, returning a list of lines.
    """
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def read_prompt_from_file(file_path):
    """
    Reads the prompt from a given file.
    """
    with open(file_path, 'r') as file:
        prompt = file.read().strip()
    return prompt

def parse_output(output, keys):
    """
    Parses the structured output into a dictionary dynamically.
    """
    result = {}
    for line in output.split("\n"):
        for key in keys:
            if line.startswith(key):
                result[key] = line.split(": ", 1)[1].strip()
    return result

def get_output_keys(system_prompt):
    """
    Extracts expected output keys from the system prompt.
    """
    lines = system_prompt.split('\n')
    keys = []
    for line in lines:
        match = re.match(r"^(.*): \[.*\]", line)
        if match:
            keys.append(match.group(1))
    return keys

def process_lines(config_file, system_prompt_file, user_prompt_file, input_file, output_location, file_prefix):
    # Load the configuration file
    config = configparser.ConfigParser()
    config.read(config_file)

    # Extract models dynamically from the config file
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

    output_format_settings = {
        'format': config.get('output_format', 'format').strip(),
        'include_model': config.getboolean('output_format', 'include_model'),
        'include_input_line': config.getboolean('output_format', 'include_input_line'),
        'include_prompt_tokens': config.getboolean('output_format', 'include_prompt_tokens'),
        'include_output_tokens': config.getboolean('output_format', 'include_output_tokens')
    }

    # Load the system prompt, user prompt template, and input lines list
    system_message_content = read_prompt_from_file(system_prompt_file)
    user_message_template = read_prompt_from_file(user_prompt_file)
    input_lines_list = read_lines_from_file(input_file)

    # Ensure the output directory exists
    if not os.path.exists(output_location):
        os.makedirs(output_location, exist_ok=True)
        print(f"Created output directory: {output_location}")

    # Set the OpenAI API key
    openai.api_key = api_key

    # Determine output keys from system prompt
    output_keys = get_output_keys(system_message_content)

    results = []
    for model in models:
        for input_line in input_lines_list:
            output, prompt_tokens, output_tokens = process_line(openai, input_line, system_message_content, user_message_template, model, response_settings)
            if output_keys:
                parsed_output = parse_output(output, output_keys)
                result = {
                    "Model": model if output_format_settings['include_model'] else None,
                    "Input Line": input_line if output_format_settings['include_input_line'] else None,
                    "Prompt Tokens": prompt_tokens if output_format_settings['include_prompt_tokens'] else None,
                    "Output Tokens": output_tokens if output_format_settings['include_output_tokens'] else None
                }
                # Add dynamically parsed fields
                for key in output_keys:
                    result[key] = parsed_output.get(key, "Unknown")
            else:
                result = {
                    "Model": model if output_format_settings['include_model'] else None,
                    "Input Line": input_line if output_format_settings['include_input_line'] else None,
                    "Output": output,
                    "Prompt Tokens": prompt_tokens if output_format_settings['include_prompt_tokens'] else None,
                    "Output Tokens": output_tokens if output_format_settings['include_output_tokens'] else None
                }
            results.append(result)

    # Output results to a file in the specified format
    output_file_path = f'{output_location}/{file_prefix}_results'
    if output_format_settings['format'] in ['text', 'txt']:
        output_file_path += '.txt'
        try:
            with open(output_file_path, 'w') as file:
                for result in results:
                    for key, value in result.items():
                        if value is not None:
                            file.write(f"{key}: {value}\n")
                    file.write("\n")
            print(f"Text file saved successfully at {output_file_path}")
        except Exception as e:
            print(f"Error writing text file: {e}")
    elif output_format_settings['format'] == 'csv':
        output_file_path += '.csv'
        try:
            with open(output_file_path, 'w', newline='') as csvfile:
                if output_keys:
                    fieldnames = ['Model', 'Input Line'] + output_keys + ['Prompt Tokens', 'Output Tokens']
                else:
                    fieldnames = ['Model', 'Input Line', 'Output', 'Prompt Tokens', 'Output Tokens']
                fieldnames = [field for field in fieldnames if field in results[0]]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

                writer.writeheader()
                for result in results:
                    writer.writerow({k: v for k, v in result.items() if v is not None})
            print(f"CSV file saved successfully at {output_file_path}")
        except Exception as e:
            print(f"Error writing CSV file: {e}")

    print(f"Results have been saved to '{output_file_path}'")

# Example usage:
# process_lines(config_file, system_prompt_file, user_prompt_file, medication_file, output_location, file_prefix)
