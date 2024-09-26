import wandb
import shutil
import os
import glob
#Download latest trained model
def download_model():
    old_model_path = glob.glob('production_model/*.pt')[0] if glob.glob('production_model/*.pt') else None
    if os.path.exists(old_model_path):
        os.remove(old_model_path)
    run = wandb.init(anonymous="must")
    production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
    production_dir = production.download(root=f"production_model")
    model_file = f"{production_dir}/best.pt"
    shutil.move(model_file, f"{production_dir}/model_{production.version}.pt")
    wandb.finish()
    print(f"Model saved to {production_dir}")
    
    
   


if __name__=="__main__":
    download_model()
    
    