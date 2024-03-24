from yaml import safe_load
import os

settings = {}

config_path = os.environ.get('CONFIG_FILE', './config/local.yml')
with open(config_path, 'r') as config_file:
  settings = safe_load(config_file)