
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense

from utils.common import read_yaml
from constants import *
class ModelArhitecture:
    def __init__(self,input_dim,output_dim,input_length):

        self.input_dim = input_dim
        self.output_dim = output_dim
        self.input_length = input_length
        self.params = read_yaml(PARAMS_FILE_PATH)

    def model(self):
        model_params = self.params.ModelParams

        model = Sequential()
        model.add(Embedding(self.input_dim+1,model_params.output_dim,input_length=self.input_length,input_shape=(self.input_length-1,)))
        model.add(LSTM(model_params.units))
        model.add(Dense(self.input_dim+1,activation='softmax'))

        print("iput len",self.input_length)

        model.compile(loss= 'categorical_crossentropy',optimizer='adam',metrics=['accuracy','Precision',"Recall"])
        print(model.summary())

        return model