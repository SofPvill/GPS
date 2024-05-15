#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings
import json
import sys
import joblib

# model importation
import pickle

warnings.simplefilter(action='ignore', category=FutureWarning)

def preprocess_and_predict(csv_file_path):
    # Carga el modelo
    model = joblib.load('./model-ml/model.pkl')

    # Lee el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(csv_file_path)
    
    df = df.dropna()
    
    print(df)

    # Convierte la característica 'Date' en un objeto datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Calcula la fecha mínima en tus datos
    min_date = df['Date'].min()

    # Crea una nueva característica 'Time' que represente el número de días desde la fecha mínima
    df['Time'] = (df['Date'] - min_date) / np.timedelta64(1, 'D')

    # Haz una predicción con el modelo utilizando la característica 'Time'
    prediction = model.predict(df[['Time']])

    # Imprime la predicción
    print(prediction)
    print(prediction[0])

if __name__ == "__main__":
    csv_file_path = sys.argv[1]
    preprocess_and_predict(csv_file_path)