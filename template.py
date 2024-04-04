import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

Project_name="hate"

list_of_files=[
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/components/data_ingestion.py",
    f"{Project_name}/components/data_transformation.py",
    f"{Project_name}/components/model_trainer.py",
    f"{Project_name}/components/model_evaluation.py",
    f"{Project_name}/components/model_pusher.py",
    f"{Project_name}/configuration/__init__.py",
    f"{Project_name}/configuration/gcloud_syncer.py",
    f"{Project_name}/constants/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/entity/config_entity.py",
    f"{Project_name}/entity/artifact_entity.py",
    f"{Project_name}/exception/__init__.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/pipeline/train_pipeline.py",
    f"{Project_name}/pipeline/prediction_pipeline.py",
    f"{Project_name}/ml/__init__.py",
    f"{Project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]


for filepath in list_of_files:
    filepath=Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Crating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exists")

