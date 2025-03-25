# src/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)
# Load the trained model at startup
model = joblib.load('house_price_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Expecting JSON input with features matching the training data columns
    input_data = request.get_json(force=True)
    # Convert input into a DataFrame (ensure that keys align with the trained model's features)
    input_df = pd.DataFrame([input_data])
    
    # Perform prediction
    prediction = model.predict(input_df)
    return jsonify({'predicted_sale_price': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)