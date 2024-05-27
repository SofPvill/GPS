from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app) # CORS Policies

with open('./model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    time_value = data['Time']

    X_new = np.array([[time_value]])
    y_pred = model.predict(X_new)
    
    print("Unwrapped prediction: ", y_pred)

    return jsonify(prediction=y_pred.tolist())

if __name__ == '__main__':
    app.run(port=3000)
