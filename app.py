from flask import Flask, request, url_for, redirect, render_template, jsonify
from joblib import load
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = load('animalModel.pkl')

cols = ['hair', 'feather', 'egg', 'milk', 'airborne', 'aquatic', 
'predator', 'toothed', 'backbone', 'breathes',
'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int(int_features))
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = model.predict(data_unseen.values)
    return render_template('home.html', pred='The Animal Type is {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run()