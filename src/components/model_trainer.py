from model.ModelArchitecture import ModelArhitecture
from entity.config_entity import ModelTrainerConfig
import pickle
from utils.common import read_yaml
from logger import logger
from constants import *
from components.transform_data import TransformData
import mlflow
from urllib.parse import urlparse
import mlflow.keras
from utils.common import save_json
class ModelTrainer:
    def __init__(self,mode_trainer_config:ModelTrainerConfig):
        self.model_trainer_config = mode_trainer_config
        self.params = read_yaml(PARAMS_FILE_PATH)

    def train_model(self,unique_word,max_len):

        logger.info(">>>>>>>>> model training started <<<<<<<<<<<<<")
        x_path = self.model_trainer_config.transformed_data_dir + "/x.pkl"
        y_path = self.model_trainer_config.transformed_data_dir + "/y.pkl"
        with open(x_path,'rb') as f:
            x = pickle.load(f)

        with open(y_path,'rb') as f:
            y = pickle.load(f)

        input_len = len(x)
        x_test_len = input_len*0.3

        model_params = self.params.ModelParams
        EPOCHS = model_params.EPOCHS

        unique_word_count = pickle.load(open("artifacts/transformed_data/unique_max_word.pkl","rb"))

        print("unique word is ------------",unique_word_count)

        model_ = ModelArhitecture(input_dim=unique_word_count[0],output_dim=model_params.output_dim,input_length=unique_word_count[1])

        model = model_.model()
        model.fit(x,y,epochs = EPOCHS)
        self.model = model

        model_path = self.model_trainer_config.model_dir +"/" + self.model_trainer_config.model_name

        pickle.dump(model,open(model_path,'wb'))
        
        logger.info(f">>>>>>>>>>>>> model is at {self.model_trainer_config.model_dir} <<<<<<<<<<<<<<")

        logger.info(">>>>>>>>> Model training completed <<<<<<<<<<<<<<<<")

