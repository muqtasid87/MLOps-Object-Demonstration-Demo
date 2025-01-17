from src.components.evaluate import metrics_latest, metrics_production
from src.utils.main_utils import *
import wandb

def run_deployment():
    wandb.init(project="toll_booth", anonymous='must', id = f"experiment_{read_exp_num()-1}", resume="must")
    if metrics_latest.box.map >= metrics_production.box.map:
        latest = wandb.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:latest', type='model')
        latest.aliases.append("production")
        latest.save()
        print("Production alias added to latest model")

    wandb.finish()
    
    
if __name__=="__main__":
    run_deployment()