from src.entity.config_entity  import PredictionConfig,ModelTrainerConfig
from src.utils.common import read_yaml
from src import logger
from src.constants import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

import pickle

class Prediction:
    def __init__(self):
        self.modl_trainer_yaml=  read_yaml(path_to_yaml=CONFIG_FILE_PATH)

    def predict(self,text):
        
        try:
            logger.info(">>>>>>>>>>> predicting <<<<<<<<<<<<<<<<")

            model_trainer = self.modl_trainer_yaml.model_trainer

            model_path = model_trainer.model_dir+"/" + model_trainer.model_name

            model = pickle.load(open(model_path,'rb'))

            tokenizer_path = "artifacts/transformed_data/tokenizer.pkl"

            tokenizer  = pickle.load(open(tokenizer_path,'rb'))

            for i in range(1):
                #tokenize
                token_text = tokenizer.texts_to_sequences([text])[0]
                #pad_sequence
                padded_token_text = pad_sequences([token_text],maxlen=29,padding='pre')
                #predict
                pos = np.argmax(model.predict(padded_token_text))
                for word,index in tokenizer.word_index.items():
                    if index == pos:
                        text = text + " "+ word
            return text
        except Exception as e:
            raise e

