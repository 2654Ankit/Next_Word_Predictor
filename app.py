from flask import Flask,request,jsonify,render_template,url_for
import os
from flask_cors import CORS,cross_origin
from src.pipeline.Prediction_pipeline import Prediction_Pipeline

app = Flask(__name__)
CORS(app)



@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training success"

@app.route("/predict",methods=['POST'])
@cross_origin()
def predict():
    text = request.form.get("text")
    obj = Prediction_Pipeline()
    result = obj.predict(text)
    return render_template("index.html",result=result)

import os


if __name__ =="__main__":

    app.run(debug=True,host='0.0.0.0',port=8080) 