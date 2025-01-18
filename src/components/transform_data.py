import numpy as np
import pandas as pd
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense
from src.entity.config_entity import DataTransformationConfig
from tensorflow.keras.utils import to_categorical
from src import logger
from src.utils.common import load_text
from pathlib import Path
import pickle

class TransformData:
    def __init__(self,DataTransformationConfig:DataTransformationConfig):
        self.data_transformation_config = DataTransformationConfig

    
    def transform_data(self):
        

        try:
            logger.info(">>>>>>>>> Transforming data <<<<<<<<<")
            data_file_path = self.data_transformation_config.data_file_path
            data_file_path = Path(data_file_path+"/"+self.data_transformation_config.data_file_name)
            print(f"file path is {data_file_path}")
            content  = load_text(path=data_file_path)
            data = content.split("=")[1]
            data = data.replace('"""',"")

            tokenizer = Tokenizer()

            tokenizer.fit_on_texts([data])
            
            self.unique_word_count  = len(tokenizer.word_index)

            input_sequences = []
            for sentence in data.split("\n"):
                tokenized_sentence = tokenizer.texts_to_sequences([sentence])[0]
                for i in range(1, len(tokenized_sentence)):
                    input_sequences.append(tokenized_sentence[:i+1])

            print("input sequence is ",input_sequences)
        
            self.max_len = max([len(x) for x in input_sequences])
            print("maximum length is ",self.max_len)

            padded_input_sequences = pad_sequences(input_sequences,maxlen=self.max_len,padding='pre')

            x = padded_input_sequences[:,:-1]

            y = padded_input_sequences[:,-1]

            y = to_categorical(y,num_classes=self.unique_word_count+1 )


            x_path = self.data_transformation_config.transformed_data_x + "/x.pkl"
            y_path = self.data_transformation_config.transformed_data_y + "/y.pkl"
            with open(x_path,'wb') as f:
                pickle.dump(x,f)

            

            
            with open(y_path,'wb') as f:
                pickle.dump(y,f)



            
        except Exception as e:
            raise e

    def unique_word(self):
        return (self.unique_word_count,self.max_len)

    
