from logger import logger
from components.transform_data import TransformData
from config.configuration import ConfigurationManager

class Data_Transformation_Pipeline:
    def __init__(self):
        pass

    def main(self)->int:
        logger.info(">>>>>> Running data_transformation_pipeline<<<<<<<<<<")
        try:

            config = ConfigurationManager()
            data_transformation_config = config.data_transformation_config()

            data_transformation = TransformData(data_transformation_config)

            data_transformation.transform_data()
            unique_word = data_transformation.unique_word()

            return unique_word

        except Exception as e:
            raise e


    
STAGE_NAME = "Data_transformation_stage"
if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
        obj = Data_Transformation_Pipeline()
        unique_word = obj.main()
        logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

    except Exception as e:
        raise e
