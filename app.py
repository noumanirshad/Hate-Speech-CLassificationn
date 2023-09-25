from src.Hate_Speech_Classifier.logger import logging
from src.Hate_Speech_Classifier.exception import CustomException
import sys
from src.Hate_Speech_Classifier.components.data_ingestion import DataIngestion
# from src.Hate_Speech_Classifier.components.data_transformation import DataTransformation

import pandas as pd
# from src.Hate_Speech_Classifier.utils import read_sql_data


if __name__ == '__main__':
    logging.info("The exsecution project has been created")


    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.get_data_ingestion()

        # data_transformation = DataTransformation()
        # data_transformation.initiate_data_transformation(train_path, test_path)

    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)