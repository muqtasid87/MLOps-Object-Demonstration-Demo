#Where all the files and folders generated will be stored
ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion Constants
"""
#Folder in which data will be downloaded
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
#Ingesting Data from Roboflow 
RF_API = "H4q9DQu5MD1pKmGnJGDD"
RF_VERSION = 1
RF_TYPE = "yolov8"
RF_PROJECT = "toll-booth-kzuxu"
RF_WORKSPACE = "ml-rcff8"





"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "data.yaml"]




"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s.pt" 
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16
PROJECT_PATH: str = "toll_booth_project_runs"


