import os
import urllib.request as request
from src.WineQuality import logger
import zipfile
from src.WineQuality.entity.config_entity import (DataIngestionConfig)
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url  = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info :\n{headers}")
        else:
            logger.info(f"file already exists")

    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        