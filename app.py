from src.utils.logger import logging
from src.utils.exception import AppException
import sys
from src.pipeline.training_pipeline import TrainPipeline
from src.components import deploy




# obj = TrainPipeline()
# obj.run_pipeline()

deploy = deploy.run_deployment()

