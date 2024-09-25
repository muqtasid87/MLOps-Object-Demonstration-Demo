import wandb
from src.entity.config_entity import  DataIngestionConfig
from src.utils.main_utils import *
from ultralytics import YOLO
import os


run = wandb.init(name="model_evaluation_and_comparison", anonymous='must')

#Download latest trained model
latest = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:latest', type='model')
latest_dir = latest.download(root="artifacts/evaluation/latest")

#Download production model
production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
production_dir = production.download(root="artifacts/evaluation/production")


latest_model = YOLO(f"{latest_dir}\\best.pt")
production_model = YOLO(f"{production_dir}\\best.pt")


for files in os.listdir('artifacts\\evaluation'):
    if os.path.exists('runs'):
        os.system("rm -rf r "+"runs")
metrics_latest = latest_model.val(data=f"./artifacts/data_ingestion/data-v{DataIngestionConfig.rf_version}/data.yaml", project="./artifacts/evaluation/runs/latest", name = 'val', workers=0, exist_ok = True)
metrics_production = production_model.val(data=f"./artifacts/data_ingestion/data-v{DataIngestionConfig.rf_version}/data.yaml", project="./artifacts/evaluation/runs/production", name='val', workers=0, exist_ok = True)

