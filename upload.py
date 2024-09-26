
import roboflow
from src.entity.config_entity import DataIngestionConfig

rf = roboflow.Roboflow(api_key=DataIngestionConfig().rf_api)

# get a workspace
workspace = rf.workspace(DataIngestionConfig().rf_workspace)

# Upload data set to a new/existing project
workspace.upload_dataset(
    "./dataset/", # This is your dataset path #TODO
    DataIngestionConfig().rf_project, 
    num_workers=10,
    project_license="MIT",
    project_type="object-detection",
    batch_name=None,
    num_retries=0
)



project = rf.workspace().project(DataIngestionConfig().rf_project)
project.generate_version(settings={})