from src import logger
from src.pipeline.Stage_01_dataingestion import Data_ingestion_pipeline



STAGE_NAME = "Data_ingestion_stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>entered into {STAGE_NAME}<<<<<<<<<<<<<<<")
    obj = Data_ingestion_pipeline()
    obj.main()
    logger.info(f"Exist from {STAGE_NAME}")

except Exception as e:
    raise e
