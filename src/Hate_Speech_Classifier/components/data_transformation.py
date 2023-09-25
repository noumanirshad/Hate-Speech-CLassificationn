import sys
import os
import pandas as pd
import numpy as np
from src.Hate_Speech_Classifier.logger import logging
from src.Hate_Speech_Classifier.exception import CustomException
from src.Hate_Speech_Classifier.components.data_ingestion import DataIngestion
from src.Hate_Speech_Classifier.components.Preprocessing import FeaturesPreprocessing
from src.Hate_Speech_Classifier.utils import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessing_path = os.path.join("src/Hate_Speech_Classifier/Data", 'preprocessing.pkl')

class DataTransformation:
    def __init__(self):
        self.preprocessing_config = DataTransformationConfig()


    def feature_extraction(self, data):
        try:
            logging.info("Lets creating and add target feature. ")
            data.drop("Unnamed: 0", axis = 1, inplace = True)

            data['labels'] = data['class'].map({
                0: "Hate Speech",
                1: "Offensive Language",
                2: "No Hate and No offensive"
            })
            logging.info("Successfully creating and add target feature. ")

            return data

        except Exception as e:
            logging.info(f"An exception has occurred : {e}")
            raise Exception(e, sys)
        

    def initiate_data_transformation(self):
        try:
            preprocessor = FeaturesPreprocessing()

            logging.info("Lets appling preprocessing and tokenize function")
            df = pd.read_csv(os.path.join("src/Hate_Speech_Classifier/Data", "labeled_data.csv"))
            # df = df.iloc[:5, :]
            df["tweet"] = df['tweet'].apply(preprocessor.preprocess_text)

            df = self.feature_extraction(df)
            logging.info("Data feature_extraction is completed successfully")

            save_object(
                file_path= self.preprocessing_config.preprocessing_path ,
                obj = preprocessor
            )
            logging.info(f"Data_transformation Successfully Loaded--------------")



        except Exception as e:
            logging.info(f"An exception has occurred : {e}")
            raise Exception(e, sys) 
    


    
