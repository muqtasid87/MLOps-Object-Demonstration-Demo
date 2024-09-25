import wandb

run = wandb.init(name="model_evaluation_and_comparison", anonymous='must')

#Download latest trained model
production = run.use_artifact('muqtasid87-international-islamic-university-malaysia-org/wandb-registry-model/toll_plaza:production', type='model')
production_dir = production.download(root="model/production")



production = (f"{production_dir}\\best.pt")