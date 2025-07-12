from flask import Flask, request, jsonify, send_from_directory, render_template, send_file
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
from sklearn.exceptions import DataConversionWarning
import webbrowser
import threading
import time
import traceback

# Initialize Flask app
app = Flask(__name__, static_folder='.')
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500", "http://localhost:5000"]}})

# Load the model
model = joblib.load('models/random_forest_model_tuned_params.joblib')

FEATURE_NAMES = ['Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'LDL', 'VLDL', 'BMI']

def open_browser():
    """Open the default web browser after a short delay"""
    time.sleep(1.5)  # Wait for the server to start
    webbrowser.open('http://localhost:5000')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please check server logs.',
            'prediction': 0,
            'confidence': 0
        }), 500
        
    try:
        data = request.get_json()
        if not data:
            raise ValueError('No JSON data received')

        # Log received data for debugging
        print("Received data:", data)
        
        # Get features in the correct order
        features = []
        for name in FEATURE_NAMES:
            value = data.get(name)
            if value is None:
                raise ValueError(f'Missing required parameter: {name}')
            try:
                features.append(float(value))
            except (ValueError, TypeError) as e:
                raise ValueError(f'Invalid value for {name}: {value}. Must be a number.')
        
        df = pd.DataFrame([features], columns=FEATURE_NAMES)
        print("Features for prediction:", features)
        
        # Make prediction
        pred = model.predict(df)[0]
        confidence = model.predict_proba(df)[0][1] if pred == "Positive" else model.predict_proba(df)[0][0]
        print("Raw prediction:", pred)
        print("Confidence:", confidence)

        # Map string predictions to numeric values
        map_prediction = {"Positive": 1, "Negative": 0}
        try:
            prediction = int(pred)
        except ValueError:
            prediction = map_prediction.get(pred, 0)

        confidence = 0.1
        if hasattr(model, 'predict_proba'):
            try:
                proba = model.predict_proba(df)[0]
                confidence = float(proba[1] if prediction == 1 else proba[0])
            except:
                pass

        return jsonify({
            'prediction': prediction,
            'confidence': confidence,
            'features_used': FEATURE_NAMES,
            'input_values': features
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'prediction': 0,
            'confidence': 0
        }), 400
    
if __name__ == '__main__':
    # Start the browser in a separate thread
    threading.Thread(target=open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=5000)