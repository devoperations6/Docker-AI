from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model from the file
try:
    with open('models/your_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None

@app.route('/')
def home():
    return "<h1>AI Model API</h1><p>Send a POST request to /predict to use the model.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please ensure the model file exists.'}), 500

    try:
        # Get data from the POST request
        data = request.get_json(force=True)
        
        # Ensure the 'features' key exists and is a list
        if 'features' not in data or not isinstance(data['features'], list):
            return jsonify({'error': "Request must contain a 'features' key with a list of values."}), 400
            
        features = np.array(data['features'])
        
        # The model expects a 2D array, so we reshape a single sample
        prediction = model.predict(features.reshape(1, -1))
        
        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible from outside the container
    app.run(host='0.0.0.0', port=5000)