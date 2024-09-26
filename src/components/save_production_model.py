import wandb
import os
run = wandb.init(name="git_download")

#Download latest trained model
production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
production_dir = production.download(root=f"model/production/")
model_file = f"{production_dir}/best.py"
os.rename(model_file, f"{production.version}_production_model")





print(f"Model saved to {production_dir}")