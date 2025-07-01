# EPID731 - Day 4

This repository contains the materials for **Day 4** of the short course **EPID731: Analysis Of Electronic Health Record (EHR) Data**, offered at the University of Michigan. The focus of Day 4, taught by Lars Fritsche, is on using GPTs to harmonize medication data.

### Description

This short course offers an overview of modern analytical methods and research applications using EHR data, with a specific focus on epidemiologic inferences. For Day 4, participants will learn about using GPTs to harmonize medication data.

## Repository Structure

### configs

Contains configuration files for different models and temperature settings.
- `config_example_3models.ini`
- `config_example_3models_cs.ini`
- `config_example_high_temperature.ini`
- `config_example_low_temperature.ini`

### inputs

Contains input files used for the analysis.
- `medication_example_1med.txt`
- `medication_example_1med_x.txt`
- `medication_example_5meds.txt`
- `medication_example_aha.txt`
- `unique_drug_concept_names.txt`

### prompts

Contains system and user prompt files used for processing. These are consecutive steps to develop a clear and efficient system prompt for a GPT API.
- `system_prompt_01.txt`
- `system_prompt_02.txt`
- `system_prompt_03.txt`
- `system_prompt_04.txt`
- `system_prompt_05.txt`
- `system_prompt_06.txt`
- `system_prompt_07.txt`
- `system_prompt_08.txt`
- `system_prompt_09.txt`
- `system_prompt_10.txt`
- `user_prompt.txt`

### scripts

Contains Python scripts used for processing and analysis.
- `gpt_line_processor.py`: Processes each line of input using the GPT model.
- `gpt_process_batches.py`: Processes input data in batches using the GPT model.

### Script Details

In this workshop, participants will learn how to:
1. Set up the environment for using the OpenAI API.
2. Develop a powerful prompt to classify medications.
3. Explore various parameters of the API that influence the model's performance.

Here is the revised "Getting Started" section that includes a note about needing an API key to access the OpenAI API:

---

## Getting Started

### Prerequisites

- Python 3.x
- An OpenAI API key
- Required Python packages:

```plaintext
openai
pandas
configparser
tiktoken
csv
re
asyncio
```

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/statgen/EPID731.git
```

Navigate to the repository directory:

```bash
cd EPID731
```

Install the required packages:

```bash
pip install openai pandas configparser
pip install tiktoken --only-binary :all:
```

### OpenAI API Key

To use the OpenAI API, you need to have an API key. You can get your API key by signing up on the OpenAI website.

Once you have your API key, set it as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Usage

To run the batch processing script, use the following example:

```python
# Import the external script containing batch processing functions
exec(open("Day4/scripts/gpt_process_batches.py").read())

# Define the asynchronous function to handle batch processing
async def run():
    await process_batches(
        config_file='Day4/configs/config_example_low_temperature.ini',
        system_prompt_file='Day4/prompts/system_prompt_9.txt',
        user_prompt_file='Day4/prompts/user_prompt.txt',
        input_file='Day4/inputs/medication_example_aha.txt',
        output_location='GPT_Outputs',
        file_prefix='Example4_prompt09_aha_meds',
        chunk_size=100  # Adjust based on API rate limits and performance needs
    )

# Execute the asynchronous batch processing
await run()
```

Alternatively, you can run the `gpt_line_processor.py` script with the necessary parameters set within the script:

1. Open `scripts/gpt_line_processor.py`.
2. Set the parameters for `process_batches` function.
3. Run the script:

```bash
python scripts/gpt_line_processor.py
```
