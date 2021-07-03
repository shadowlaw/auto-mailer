import yaml
from json import load


def read_yaml_file(path):
    with open(path, 'r') as fptr:
        return yaml.safe_load(fptr)


def read_json_file(path):
    with open(path, 'r') as fptr:
        return load(fptr)
