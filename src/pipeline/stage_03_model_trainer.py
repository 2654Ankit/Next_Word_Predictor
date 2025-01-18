from src import logger
from src.components.model_trainer import ModelTrainer
from src.config.configuration import ConfigurationManager

class Model_Trainer_Pipeline:
    def __init__(self,unique_word,max_len):
        self.unique_word = unique_word
        self.max_len = max_len

    def main(self):
        logger.info(">>>>>> Running model training pipeline <<<<<<<<<<")
        try:

            config = ConfigurationManager()
            data_transformation_config = config.model_trainer_config()

            model_trainer = ModelTrainer(data_transformation_config)

            model_trainer.train_model(self.unique_word,self.max_len)


        except Exception as e:
            raise e
