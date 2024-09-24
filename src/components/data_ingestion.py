import os
import sys
import shutil
from src.utils.logger import logging
from src.utils.exception import AppException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifact
from roboflow import Roboflow


class DataIngestion:
    
    """
    This class handles data ingestion from Roboflow, including downloading datasets and managing configurations. It provides methods to download data and initiate the data ingestion process, returning relevant artifacts.

    Attributes:
        data_ingestion_config: Configuration settings for data ingestion.
        rf: Instance of Roboflow for accessing the API.
        project: Project instance from Roboflow workspace.
        version: Version instance of the dataset.

    Methods:
        download_data: Fetches data from Roboflow and saves it to a specified directory.
        initiate_data_ingestion: Initiates the data ingestion process and returns a DataIngestionArtifact.

    """

    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        
        try:
            self.data_ingestion_config = data_ingestion_config
            self.rf = Roboflow(api_key=self.data_ingestion_config.rf_api)
            self.project = self.rf.workspace(self.data_ingestion_config.rf_workspace).project(self.data_ingestion_config.rf_project)
            self.version = self.project.version(self.data_ingestion_config.rf_version)
            
        except Exception as e:
           raise AppException(e, sys)
        

        
    def download_data(self)-> str:
        '''
        Fetch data from Roboflow
        '''

        try: 
            #Make necessary to directories
            data_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(data_download_dir, exist_ok=True)
            data_dir_name = f"data-v{self.data_ingestion_config.rf_version}"
            full_custom_path = os.path.join(data_download_dir, data_dir_name)
            logging.info(f"Downloading data from Roboflow into file {full_custom_path}")
            
            #Check if data is already downloaded
            if not os.path.exists(full_custom_path):
                #Download the data
                dataset = self.version.download(self.data_ingestion_config.rf_type)
                #Move and rename downloaded file to the data_ingestion folder
                downloaded_folder = dataset.location
                current_path = shutil.move(downloaded_folder, data_download_dir)
                os.rename(current_path, full_custom_path)

                logging.info(f"Downloaded data from {self.data_ingestion_config.rf_workspace} workspace into file {full_custom_path}")
            
            return full_custom_path

        except Exception as e:
            raise AppException(e, sys)
    



    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try: 
            #Initiate data ingestion
            full_custom_path = self.download_data()
    

            data_ingestion_artifact = DataIngestionArtifact(
                data_file_path=full_custom_path
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        

    
    
        