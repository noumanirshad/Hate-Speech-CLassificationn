import os
import sys
import numpy as np
import pandas as pd
from src.Hate_Speech_Classifier.logger import logging
from src.Hate_Speech_Classifier.exception import CustomException
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('Artifacts', 'train.csv')
    test_data_path:str = os.path.join('Artifacts', 'test.csv')
    raw_data_path:str = os.path.join('Artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def get_data_ingestion(self):
        try:
            df = pd.read_csv(os.path.join("src/Hate_Speech_Classifier/Data", "labeled_data.csv"))
            logging.info("Reading data from starting point")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            df.to_csv(self.ingestion_config.raw_data_path, index =False, header = True)

            logging.info("Data ingestion is completed successfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info(f"An exception has occurred : {e}")
            raise Exception(e, sys)



