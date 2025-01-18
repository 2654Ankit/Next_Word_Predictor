
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense



class ModelArhitecture:
    def __init__(self,input_dim,output_dim,input_length,input_shape,units):

        self.input_dim = input_dim
        self.output_dim = output_dim
        self.input_length = input_length
        self.input_shape = input_shape
        self.units = units

    def model(self):


        model = Sequential()
        model.add(Embedding(self.input_dim,self.units,input_length=self.input_length,input_shape=(self.input_shape,)))
        model.add(LSTM(self.units))
        model.add(Dense(self.input_dim,activation='softmax'))