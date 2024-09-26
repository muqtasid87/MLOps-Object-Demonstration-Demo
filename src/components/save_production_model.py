import wandb
import shutil

#Download latest trained model
def download_model():
    run = wandb.init(anonymous="must")
    production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
    production_dir = production.download(root=f"production_model")
    model_file = f"{production_dir}/best.pt"
    shutil.move(model_file, f"{production_dir}/model_{production.version}.pt")
    wandb.finish()
    print(f"Model saved to {production_dir}")


if __name__=="__main__":
    download_model()