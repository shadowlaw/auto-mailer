import yaml


def read_yaml_file(path):
    with open(path, 'r') as fptr:
        return yaml.load(fptr, Loader=yaml.FullLoader)
