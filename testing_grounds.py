import wandb
from src.entity.config_entity import  DataIngestionConfig
from src.utils.main_utils import *
from ultralytics import YOLO




run = wandb.init()
latest = run.use_artifact('muqtasid87-international-islamic-university-malaysia/toll_booth/run-experiment_3-best.pt:v0', type='model')
print(latest.version)




# latest_dir = latest.download(root="artifacts/evaluation/latest")

# #Download production model
# production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
# production_dir = production.download(root="artifacts/evaluation/production")


# latest_model = YOLO(f"{latest_dir}\\best.pt")
# production_model = YOLO(f"{production_dir}\\best.pt")

# metrics_latest = latest_model.val(data=f"./artifacts/data_ingestion/data-v{DataIngestionConfig.rf_version}/data.yaml", project="./artifacts/evaluation/runs/latest", name = 'val', workers=0)
# metrics_production = production_model.val(data=f"./artifacts/data_ingestion/data-v{DataIngestionConfig.rf_version}/data.yaml", project="./artifacts/evaluation/runs/production", name='val', workers=0)




# if metrics_latest.box.map > metrics_production.box.map:
#     #CODE TO ADD PRODUCTION ALIAS TO LATEST MODEL
#     pass