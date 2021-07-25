from os import path, mkdir
from shutil import copyfile
import yaml
from json import load


def read_yaml_file(path):
    with open(path, 'r') as fptr:
        return yaml.load(fptr, Loader=yaml.FullLoader)


def read_json_file(path):
    with open(path, 'r') as fptr:
        return load(fptr)

def create_file(file_path):
    if not path.exists(file_path):
        if not path.exists(path.dirname(file_path)):
            mkdir(path.dirname(file_path))
        with open(file_path, 'w'):
            pass


def copy(src, dest):
    copyfile(src, dest)
