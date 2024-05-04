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


warnings.simplefilter(action='ignore', category=FutureWarning)

demand_df = pd.read_csv("../assets/dataset/base-historical-product-demand.csv")

demand_df = demand_df[demand_df['Date'].notnull()]

min_date = demand_df['Date'].min()
max_date = demand_df['Date'].max()

print(demand_df['Order_Demand'].dtypes)

demand_df['Date'] = pd.to_datetime(demand_df['Date'])
demand_df['Order_Demand'] = pd.to_numeric(demand_df['Order_Demand'], errors='coerce')

demand_df['Date'] = pd.to_datetime(demand_df['Date'])
demand_df_group = demand_df.groupby(pd.Grouper(key='Date', freq='M'))['Order_Demand'].sum().reset_index()

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=demand_df_group, x='Date', y='Order_Demand', color = '#18B15A')
plt.title('Demanda de pedidos a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Total de pedidos')
plt.savefig('../assets/images/demanda-tiempo-general.png')

demand_df = demand_df[demand_df['Date']>'2011-12-31']

demand_df_group_warehouse = demand_df.groupby(['Date', 'Warehouse'])['Order_Demand'].sum().reset_index()

g = sns.relplot(data=demand_df_group_warehouse, 
                x='Date', 
                y='Order_Demand', 
                kind="line",
                hue='Warehouse',
                palette=["#EF9A9A", "#673AB7", "#039BE5", "#FB8C00"],
                col='Warehouse',
                col_wrap=2,  
                height=3, aspect=1.5)
plt.savefig('../assets/images/demanda-grupo-almacen.png')

whse_s_df = demand_df[demand_df['Warehouse']=='Whse_S']
whse_a_df = demand_df[demand_df['Warehouse']=='Whse_A']
whse_c_df = demand_df[demand_df['Warehouse']=='Whse_C']
whse_j_df = demand_df[demand_df['Warehouse']=='Whse_J']

whse_s_df_group_category = whse_s_df.groupby(['Date', 'Product_Category'])['Order_Demand'].sum().reset_index().sort_values('Order_Demand', ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(data=whse_s_df_group_category, x='Product_Category', y='Order_Demand', color ="#EF9A9A")
plt.title('Demanda de producto alamacen S')
plt.xlabel('Categoria de producto')
plt.xticks(rotation=90)
plt.ylabel('Demanda del producto')
plt.savefig('../assets/images/demanda-producto-als.png')

whse_a_df_group_category = whse_a_df.groupby(['Date', 'Product_Category'])['Order_Demand'].sum().reset_index().sort_values('Order_Demand', ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(data=whse_a_df_group_category, x='Product_Category', y='Order_Demand', color ="#673AB7")
plt.title('Demanda de producto alamacen A')
plt.xlabel('Categoria de producto')
plt.xticks(rotation=90)
plt.ylabel('Demanda del producto')
plt.savefig('../assets/images/demanda-producto-ala.png')

whse_c_df_group_category = whse_c_df.groupby(['Date', 'Product_Category'])['Order_Demand'].sum().reset_index().sort_values('Order_Demand', ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(data=whse_c_df_group_category, x='Product_Category', y='Order_Demand', color ="#039BE5")
plt.title('Demanda de producto alamacen C')
plt.xlabel('Categoria de producto')
plt.xticks(rotation=90)
plt.ylabel('Demanda del producto')
plt.savefig('../assets/images/demanda-producto-alc.png')

whse_j_df_group_category = whse_j_df.groupby(['Date', 'Product_Category'])['Order_Demand'].sum().reset_index().sort_values('Order_Demand', ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(data=whse_j_df_group_category, x='Product_Category', y='Order_Demand', color ="#FB8C00")
plt.title('Demanda de producto alamacen j')
plt.xlabel('Categoria de producto')
plt.xticks(rotation=90)
plt.ylabel('Demanda del producto')
plt.savefig('../assets/images/demanda-producto-alj.png')

whse_j_df_cat_19 = whse_j_df[whse_j_df['Product_Category']=='Category_019']
whse_j_df_cat_19_group = whse_j_df_cat_19.groupby(pd.Grouper(key='Date', freq='M'))['Order_Demand'].sum().reset_index()

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=whse_j_df_cat_19_group, x='Date', y='Order_Demand', color = '#FB8C00')
plt.title('Demanda de pedidos de categoria 19 en Almacen J al paso del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Total de pedidos')
plt.savefig('../assets/images/demanda-producto-cat19.png')

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