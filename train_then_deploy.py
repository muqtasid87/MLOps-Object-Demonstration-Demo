#THESE FILE CAN LATER BE AUTOMATED USING GITHUB ACTIONS, ONCE train.py has been run, deploy.py can be run.
from src.utils.logger import logging
from src.utils.exception import AppException
import sys
from src.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()



from src.components import add_production_alias
add_production_alias = add_production_alias.run_deployment()