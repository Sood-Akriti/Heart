# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:46:27 2022

@author: A
"""

from flask import Flask
from flask import render_template,request
import pickle
import numpy as np

app = Flask(__name__)
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 15)
    loaded_model = pickle.load(open("heart_prediction.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/index/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if int(result)== 1:
            prediction ='You are likely to suffer from Heart diseases.'
        else:
            prediction ='Congrtas!! You are not suffering from heart diseses.'           
        return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
     app.run()