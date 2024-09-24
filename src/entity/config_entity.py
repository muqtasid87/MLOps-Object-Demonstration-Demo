import os
import yaml
from dataclasses import dataclass

# Load configuration from params.yaml
def load_yaml_config(filepath: str) -> dict:
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

# Path to params.yaml
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'params.yaml')
CONFIG = load_yaml_config(CONFIG_PATH)

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = CONFIG['training_pipeline']['artifacts_dir']

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        TrainingPipelineConfig().artifacts_dir, CONFIG['data_ingestion']['data_ingestion_dir_name']
    )
    rf_api: str = CONFIG['data_ingestion']['rf_api']
    rf_version: int = CONFIG['data_ingestion']['rf_version']
    rf_type: str = CONFIG['data_ingestion']['rf_type']
    rf_project: str = CONFIG['data_ingestion']['rf_project']
    rf_workspace: str = CONFIG['data_ingestion']['rf_workspace']

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        TrainingPipelineConfig().artifacts_dir, CONFIG['data_validation']['data_validation_dir_name']
    )
    valid_status_file_dir: str = os.path.join(
        data_validation_dir, CONFIG['data_validation']['data_validation_status_file']
    )
    required_file_list = CONFIG['data_validation']['required_file_list']

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        TrainingPipelineConfig().artifacts_dir, CONFIG['model_trainer']['model_trainer_dir_name']
    )
    weight_name: str = CONFIG['model_trainer']['pretrained_weight_name']
    no_epochs: int = CONFIG['model_trainer']['no_epochs']
    batch_size: int = CONFIG['model_trainer']['batch_size']
    project_path: str = os.path.join(
        TrainingPipelineConfig().artifacts_dir, CONFIG['model_trainer']['project_path']
    )
