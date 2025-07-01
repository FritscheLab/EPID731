# EPID731 - Day 4

The materials for **Day 4** of the short course **EPID731: Analysis Of Electronic Health Record (EHR) Data**, offered at the University of Michigan. The focus of Day 4, taught by Lars Fritsche, is on using GPTs to harmonize medication data.

For general setup and installation instructions, please refer to the main `README.md` file in the root of this repository.

## Day 4 Repository Structure

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
