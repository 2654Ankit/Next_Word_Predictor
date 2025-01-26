from components.model_evaluation import Evaluation
from logger import logger
class Model_Evaluation_Pipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            obj = Evaluation()
            obj.evaluate()
            obj.log_into_mlflow()
        except Exception as e:
            raise e


STAGE_NAME = "Model_evaluation_stage"

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")

        obj = Model_Evaluation_Pipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

    except Exception as e:
        raise e











        
