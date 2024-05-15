# import sys
# import pandas as pd
# import joblib

# # Carga el modelo
# model = joblib.load('./../../model-ml/model.pkl')

# # Lee los datos de entrada
# csv_file_path = sys.argv[1]

# # Lee el archivo CSV en un DataFrame de pandas
# df = pd.read_csv(csv_file_path)

# # Haz una predicción con el modelo
# prediction = model.predict(df)

# # Imprime la predicción
# print(prediction[0])

import sys
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Carga el modelo
model = joblib.load('./../../model-ml/model.pkl')

# Lee los datos de entrada
csv_file_path = sys.argv[1]

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv(csv_file_path)

# Convierte la característica 'Date' en un objeto datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calcula la fecha mínima en tus datos
min_date = df['Date'].min()

# Crea una nueva característica 'Time' que represente el número de días desde la fecha mínima
df['Time'] = (df['Date'] - min_date) / np.timedelta64(1, 'D')

# Haz una predicción con el modelo utilizando la característica 'Time'
prediction = model.predict(df[['Time']])

# Imprime la predicción
print(prediction[0])


# import sys
# import pandas as pd
# import numpy as np
# import joblib
# from datetime import datetime
# from sklearn.impute import SimpleImputer

# # Carga el modelo
# model = joblib.load('./../../model-ml/model.pkl')

# # Lee los datos de entrada
# csv_file_path = sys.argv[1]

# # Lee el archivo CSV en un DataFrame de pandas
# df = pd.read_csv(csv_file_path)

# # Convierte la característica 'Date' en un objeto datetime
# df['Date'] = pd.to_datetime(df['Date'])

# # Calcula la fecha mínima en tus datos
# min_date = df['Date'].min()

# # Crea una nueva característica 'Time' que represente el número de días desde la fecha mínima
# df['Time'] = (df['Date'] - min_date) / np.timedelta64(1, 'D')

# # Crea un imputador que reemplace los valores NaN con la media de los datos existentes
# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# # Utiliza el imputador para reemplazar los valores NaN en df
# df_imputed = imputer.fit_transform(df[['Time']])

# # Haz una predicción con el modelo utilizando la característica 'Time'
# prediction = model.predict(df_imputed)

# # Imprime la predicción
# print(prediction[0])