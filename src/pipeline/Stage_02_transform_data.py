from src import logger
from src.components.transform_data import TransformData
from src.config.configuration import ConfigurationManager

class Data_Transformation_Pipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(">>>>>> Running data_transformation_pipeline<<<<<<<<<<")
        try:

            config = ConfigurationManager()
            data_transformation_config = config.data_transformation_config()

            data_transformation = TransformData(data_transformation_config)

            data_transformation.transform_data()


        except Exception as e:
            raise e
