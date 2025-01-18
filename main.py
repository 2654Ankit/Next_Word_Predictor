from src import logger
from src.pipeline.Stage_01_dataingestion import Data_ingestion_pipeline
from src.pipeline.Stage_02_transform_data import Data_Transformation_Pipeline
from src.pipeline.stage_03_model_trainer import Model_Trainer_Pipeline



STAGE_NAME = "Data_ingestion_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
    obj = Data_ingestion_pipeline()
    obj.main()
    logger.info(f"Exist from {STAGE_NAME}")

except Exception as e:
    raise e

STAGE_NAME = "Data_transformation_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
    obj = Data_Transformation_Pipeline()
    unique_word = obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

except Exception as e:
    raise e


STAGE_NAME = "Model_trainer_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
    print("unique word is ",unique_word)
    
    obj = Model_Trainer_Pipeline(unique_word=unique_word[0],max_len=unique_word[1])
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

except Exception as e:
    raise e


