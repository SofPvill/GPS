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

# model importation
import pickle

warnings.simplefilter(action='ignore', category=FutureWarning)

demand_df = pd.read_csv("../assets/dataset/base-historical-product-demand.csv")

demand_df = demand_df[demand_df['Date'].notnull()]

demand_df['Date'] = pd.to_datetime(demand_df['Date'])
demand_df['Order_Demand'] = pd.to_numeric(demand_df['Order_Demand'], errors='coerce')

demand_df['Date'] = pd.to_datetime(demand_df['Date'])
demand_df_group = demand_df.groupby(pd.Grouper(key='Date', freq='M'))['Order_Demand'].sum().reset_index()

demand_df = demand_df[demand_df['Date']>'2011-12-31']

category_19_df = demand_df[(demand_df['Warehouse'] == 'Whse_J') & (demand_df['Product_Category'] == 'Category_019')]

category_19_df = category_19_df.loc[:, ['Date', 'Order_Demand']]
category_19_df['Date'] = pd.to_datetime(category_19_df['Date'])
category_19_df['Order_Demand'] = pd.to_numeric(category_19_df['Order_Demand'], errors='coerce')

category_19_df['Time'] = (category_19_df['Date'] - category_19_df['Date'].min()) / np.timedelta64(1, 'D')
category_19_df['Time'] = category_19_df['Time'].astype(int)

category_19_df = category_19_df.dropna(subset=['Order_Demand'])

X = category_19_df[['Time']]
y = category_19_df['Order_Demand']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: ", rmse)

future_times = np.array([X['Time'].max() + i for i in range(1, 31)]).reshape(-1, 1)
future_predictions = model.predict(future_times)
future_predictions = np.round(future_predictions, 2)

mean = float(category_19_df['Order_Demand'].mean())
median = float(category_19_df['Order_Demand'].median())
mode = float(category_19_df['Order_Demand'].mode()[0])

results = {
    "Future Predictions": future_predictions.tolist(),
    "mean": mean,
    "median": median,
    "mode": mode
}

results_json = json.dumps(results)

print("JSON Results: ", results_json)

pickle.dump(model, open('model.pkl', 'wb'))