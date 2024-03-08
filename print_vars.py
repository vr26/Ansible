# print_vars.py
import yaml
import os

# Load the vars_temp file
with open(f'Core_vars_temp_{os.environ["GITHUB_RUN_ID"]}.yml', 'r') as f:
    vars = yaml.safe_load(f)

# Print only the variables that start with 'Core'
for key, value in vars.items():
    if key.startswith('Core'):
        print(f'{key}: {value}')
