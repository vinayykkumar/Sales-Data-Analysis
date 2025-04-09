from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get JSON input
        features = np.array(data['features']).reshape(1, -1)  # Convert input to numpy array
        prediction = model.predict(features)  # Make prediction

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

