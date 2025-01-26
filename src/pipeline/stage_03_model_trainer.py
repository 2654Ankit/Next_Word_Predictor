from logger import logger
from components.model_trainer import ModelTrainer
from config.configuration import ConfigurationManager
import pickle

class Model_Trainer_Pipeline:
    def __init__(self,unique_word,max_len):
        self.unique_word = unique_word
        self.max_len = max_len

    def main(self):
        try:
            logger.info(">>>>>> Running model training pipeline <<<<<<<<<<")

            config = ConfigurationManager()
            data_transformation_config = config.model_trainer_config()
            model_trainer = ModelTrainer(data_transformation_config)
            model_trainer.train_model(self.unique_word,self.max_len)

        except Exception as e:
            raise e



STAGE_NAME = "Model_trainer_stage"
if __name__ =="__main__":

    try:
        logger.info(f">>>>>>>>>>>>>>>>> Entered into {STAGE_NAME}<<<<<<<<<<<<<<<")

        unique_word = pickle.load(open("artifacts/transformed_data/unique_max_word.pkl","rb"))
       

        obj = Model_Trainer_Pipeline(unique_word=unique_word[0],max_len=unique_word[1])
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>> Exist from {STAGE_NAME} <<<<<<<<<<<<<<<<<<")

    except Exception as e:
        raise e







