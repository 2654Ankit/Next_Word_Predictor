from utils.common import read_yaml,save_json
from constants import *
import pickle
import os
from logger import logger
import mlflow
from urllib.parse import urlparse
from tensorflow.keras.models import load_model

class Evaluation:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)


    def load_model(self):
        path = os.path.join(self.config.model_trainer.model_dir,self.config.model_trainer.model_name)
        return load_model(path)

    def load_test_data(self):
        path = os.path.join(self.config.data_transformation.transformed_data_dir)
        x_test = pickle.load(open(path+"/x_test.pkl","rb"))
        y_test = pickle.load(open(path+"/y_test.pkl","rb"))

        return x_test,y_test


    def evaluate(self):
        model = self.load_model()
        x_test,y_test = self.load_test_data()

        result = model.evaluate(x_test,y_test)

        self.eval_res = result

    def save_json_data(self,loss,acc,precision,recall):
        path = Path("save_score.json")
        save_json(path,{"loss":loss,"accuracy":acc,"precision":precision,"recall":recall})


    def log_into_mlflow(self):
        mlflow.set_registry_uri(uri="http://127.0.0.1:5000")
        mlflow.set_experiment("NextWordPredictor_Experiment")
        tracking_uri = urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run():
            mlflow.log_params(self.params.ModelParams)

            self.save_json_data(self.eval_res[0],self.eval_res[1],self.eval_res[2],self.eval_res[3])

            mlflow.log_metrics({"loss":self.eval_res[0],"acuracy":self.eval_res[1],"precision":self.eval_res[2],"recall":self.eval_res[3]})

            mlflow.set_tag("Training Info", "Basic LSTM model for next_word_predictor on self dataset")


        logger.info(">>>>>>>>>>>> logged all the params and metrics in mlflow")
















