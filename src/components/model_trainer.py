import os
import sys
from src.utils.main_utils import *
from src.utils.logger import logging
from src.utils.exception import AppException
from src.entity.config_entity import ModelTrainerConfig, DataIngestionConfig
from src.entity.artifacts_entity import ModelTrainerArtifact, DataIngestionArtifact
from ultralytics import YOLO
import wandb
from wandb.integration.ultralytics import add_wandb_callback

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_ingestion_artifact: DataIngestionArtifact): 
        self.model_trainer_config = model_trainer_config
        self.data_ingestion_artifact = data_ingestion_artifact 
        self.batch_size = self.model_trainer_config.batch_size
        self.no_epochs = self.model_trainer_config.no_epochs
        self.weight_name = self.model_trainer_config.weight_name
        self.data_path = self.data_ingestion_artifact.data_file_path
        self.version = DataIngestionConfig.rf_version 

    def configure_yaml(self, yaml_path):
        yaml = read_yaml_file(yaml_path)
        yaml['path'] = f"./artifacts/data_ingestion/data-v{self.version}"        
        yaml['train'] = "./train/images"
        yaml['test'] = "./test/images"
        yaml['val'] = "./valid/images"            
        write_yaml_file(yaml_path, yaml)
        return yaml_path

    def train_model(self, model, yaml_path):
        increment_exp()
        results = model.train(
            data=yaml_path, 
            epochs=self.no_epochs, 
            save=True, 
            project=self.model_trainer_config.project_path, 
            name=f"experiment_{read_exp_num()-1}",
            plots=True, 
            device=0, 
            workers=0
        )
        
 
        return results

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        try:
            # Ensure project path exists
            os.makedirs(self.model_trainer_config.project_path, exist_ok=True)
            
            # Initialize W&B only once
            
            run = wandb.init(
                project="toll_booth", 
                name=f"experiment_{read_exp_num()}",
                id = f"experiment_{read_exp_num()}",
                config={
                    "epochs": self.no_epochs,
                    "batch_size": self.batch_size,
                    "weight_name": self.weight_name,
                    "data_path": self.data_path
                },
                job_type="training"
            )
            
            run_id = wandb.run.id
            
        
            # Load the pretrained YOLO model
            model = YOLO(self.weight_name)
            add_wandb_callback(model, enable_model_checkpointing=False)
            yaml_path = os.path.join(self.data_path, "data.yaml")
            # Configure the YAML file
            yaml_path = self.configure_yaml(yaml_path)
            # Train the model
            self.train_model(model, yaml_path)
   

            model_path = os.path.join(
                self.model_trainer_config.project_path, 
                f"experiment_{read_exp_num()-1}", 
                "weights", "best.pt"
            )
            
        
            run = wandb.init(
                project="toll_booth", 
                id = run_id,
                job_type="logging",
                resume="must"
            )
             
            logged_artifact = run.log_artifact(artifact_or_path= f"./{model_path}", type="model") 
            run.link_artifact(artifact = logged_artifact, target_path = f"muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza")
            
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=model_path
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            run.finish()
            return model_trainer_artifact


        except Exception as e:
            logging.error(f"Exception in initiate_model_trainer: {e}")
            raise AppException(e, sys)
