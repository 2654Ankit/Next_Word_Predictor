from src.model.ModelArchitecture import ModelArhitecture
from src.entity.config_entity import ModelTrainerConfig
import pickle
from src.utils.common import read_yaml
from src import logger
from src.constants import *
from src.components.transform_data import TransformData
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

        model_params = self.params.ModelParams
        EPOCHS = model_params.EPOCHS

        model_ = ModelArhitecture(input_dim=unique_word,output_dim=model_params.output_dim,input_length=max_len,units=model_params.units)

        model = model_.model()
        model.fit(x,y,epochs = EPOCHS)

        model_path = self.model_trainer_config.model_dir +"/" + self.model_trainer_config.model_name

        pickle.dump(model,open(model_path,'wb'))
        logger.info(f">>>>>>>>>>>>> model is at {self.model_trainer_config.model_dir} <<<<<<<<<<<<<<")

        logger.info(">>>>>>>>> Model training completed <<<<<<<<<<<<<<<<")