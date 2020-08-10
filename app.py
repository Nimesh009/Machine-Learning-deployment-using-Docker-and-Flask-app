# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:35:05 2020

@author: Nimesh
"""

from flask import Flask,request
import pandas as pd
import pickle
import numpy  as np

app=Flask(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome ALL"

@app.route('/predict')
def predict_note_auth():
    variance=request.args.get('variance')
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get('file'))
    predict=classfier.predict(df_test)
    return "Hello The answer is"+str(list(prediction))


if __name__=='__main__':
    app.run(host='127.0.0.1')