import os.path
import sys
import yaml
import base64
from src.utils.exception import AppException
from src.utils.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)


def increment_exp():
    try:
        with open("artifacts\\experiments_run.txt", "r") as f:
            current_number = f.read().strip()
    except FileNotFoundError:
        current_number = 0
    
    current_number = int(current_number) +1
    
    with open("artifacts\\experiments_run.txt", "w") as f:
        f.write(str(current_number))
        
def read_exp_num():
    try:
        with open("artifacts\\experiments_run.txt", "r") as f:
            current_number = f.read().strip()
    except FileNotFoundError:
        current_number = 0
    
    current_number = int(current_number) +1
    
    return(current_number)