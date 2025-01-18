
from src.components.prediction import Prediction


class Prediction_Pipeline:
    def __init__(self):
        pass

    def predict(self,text):
        pred = Prediction()
        result =  pred.predict(text)
        return result