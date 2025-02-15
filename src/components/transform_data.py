import numpy as np
import pandas as pd
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense
from entity.config_entity import DataTransformationConfig
from tensorflow.keras.utils import to_categorical
from logger import logger
from utils.common import load_text
from pathlib import Path
import pickle
from sklearn.model_selection import train_test_split

class TransformData:
    def __init__(self,DataTransformationConfig:DataTransformationConfig):
        self.data_transformation_config = DataTransformationConfig

    
    def transform_data(self):
        

        try:
            logger.info(">>>>>>>>> Transforming data <<<<<<<<<")
            data_file_path = self.data_transformation_config.data_file_path
            data_file_path = Path(data_file_path+"/"+self.data_transformation_config.data_file_name)
            content  = load_text(path=data_file_path)
            data = content.split("=")[1]
            data = data.replace('"""',"")

            tokenizer = Tokenizer()

            tokenizer.fit_on_texts([data])
            
            self.unique_word_count  = len(tokenizer.word_index)

            pickle.dump(self.unique_word_count,open("artifacts/transformed_data/unique_word_count.pkl","wb"))

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

            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3)

            x_train_path = self.data_transformation_config.transformed_data_x + "/x.pkl"
            y_train_path = self.data_transformation_config.transformed_data_y + "/y.pkl"
            x_test_path = self.data_transformation_config.transformed_data_x + "/x_test.pkl"
            y_test_path = self.data_transformation_config.transformed_data_y + "/y_test.pkl"

            tokenizer_path = self.data_transformation_config.transformed_data_x +"/tokenizer.pkl"
            with open(x_train_path,'wb') as f:
                pickle.dump(x,f)
            
            with open(y_train_path,'wb') as f:
                pickle.dump(y,f)

            with open(x_test_path,'wb') as f:
                pickle.dump(x_test,f)

            with open(y_test_path,'wb') as f:
                pickle.dump(y_test,f)
            
            with open(tokenizer_path,'wb') as f:
                pickle.dump(tokenizer,f)
            
            unique_max_word = (self.unique_word_count,self.max_len)
            pickle.dump(unique_max_word,open("artifacts/transformed_data/unique_max_word.pkl","wb"))



            
        except Exception as e:
            raise e

    def unique_word(self):
        
        return (self.unique_word_count,self.max_len)

    # def ret_tokenizer(self):
    #     return self.tokenizer

    
