# print_vars.py
import yaml
import os

# Get the type from the environment variable
type = os.getenv('TYPE')

# Load the vars_temp file
with open(f'{type}_vars_temp_{os.environ["GITHUB_RUN_ID"]}.yml', 'r') as f:
    vars = yaml.safe_load(f)

# Print only the variables that start with the given type
for key, value in vars.items():
    if key.startswith(type):
        print(f'{key}: {value}')
