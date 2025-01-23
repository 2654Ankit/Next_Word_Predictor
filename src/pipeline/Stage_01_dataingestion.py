# from src import logger
from components.data_ingestion import DataIngestion
from config.configuration import ConfigurationManager
from src import logger
class Data_ingestion_pipeline:
    def __init__(self):
        pass

    logger.info("Entered into data_ingestion_pipeline")

    def main(self):

        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(dataingestionConfig=data_ingestion_config)

            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e

    
        