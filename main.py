from src import logger
from src.pipeline.Stage_01_dataingestion import Data_ingestion_pipeline
from src.pipeline.Stage_02_transform_data import Data_Transformation_Pipeline
from src.pipeline.stage_03_model_trainer import Model_Trainer_Pipeline
from src.pipeline.Stage_04_model_evaluation import Model_Evaluation_Pipeline

# from src.components.prediction import Prediction
from src.pipeline.Prediction_pipeline import Prediction_Pipeline

# STAGE_NAME = "Data_ingestion_stage"

# try:
#     logger.info(f">>>>>>>>>>>>>>>>>Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
#     obj = Data_ingestion_pipeline()
#     obj.main()
#     logger.info(f"Exist from {STAGE_NAME}")

# except Exception as e:
#     raise e

# STAGE_NAME = "Data_transformation_stage"

# try:
#     logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
#     obj = Data_Transformation_Pipeline()
#     unique_word = obj.main()
#     logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

# except Exception as e:
#     raise e


STAGE_NAME = "Model_trainer_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")

    obj = Model_Trainer_Pipeline(unique_word=2,max_len=2)
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

except Exception as e:
    raise e


STAGE_NAME = "Model_evaluation_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")

    obj = Model_Evaluation_Pipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

except Exception as e:
    raise e










