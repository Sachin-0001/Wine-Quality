import os
from src.WineQuality import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.WineQuality.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
        logger.info('Train and test datasets saved successfully.')
        logger.info(train.shape)
        logger.info(test.shape)