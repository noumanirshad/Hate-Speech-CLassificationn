import os
import sys
from src.Hate_Speech_Classifier.exception import CustomException
from src.Hate_Speech_Classifier.logger import logging
import pandas as pd

import numpy as np
import pickle



def save_object(file_path, obj):
    try:
        logging.info("Create pickle file")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)