from src.utils.logger import logging
from src.utils.exception import AppException
import sys
from src.pipeline.training_pipeline import TrainPipeline
# from src.components import add_production_alias




obj = TrainPipeline()
obj.run_pipeline()

# add_production_alias = add_production_alias.run_deployment()

