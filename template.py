import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


project_name = "Hate_Speech_Classifier"

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/Pipeline/training_pipeline.py",
    f"src/{project_name}/Pipeline/prediction_pipeline.py",
    f"src/{project_name}/Configruation/gcloud_syncer.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/ML/feature.py",
    f"src/{project_name}/ML/model.py",
    f"src/{project_name}/exception.py ",
    f"src/{project_name}/logger.py ",
    f"src/{project_name}/utils.py ",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "requirements.txt",
    "demo.py",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")

