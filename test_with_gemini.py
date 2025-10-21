import os
import requests
import json
import google.generativeai as genai

# --- Configuration ---
# IMPORTANT: Before running, set your Gemini API key as an environment variable.
# In your terminal, run:
# export GEMINI_API_KEY="YOUR_API_KEY"
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("FATAL ERROR: Please set your GEMINI_API_KEY environment variable first.")
    exit()

# The URL of your running Docker container's API endpoint
DOCKER_API_URL = "http://localhost:5000/predict"

def test_model_with_gemini(topic):
    """
    Uses the Gemini API to generate features for a given topic, then sends
    those features to the running Docker container to get a prediction.
    """
    print(f"\n1. Contacting Gemini to generate data for the topic: '{topic}'...")

    # Set up the Gemini model
    model = genai.GenerativeModel('gemini-pro')

    # We create a very specific prompt asking Gemini for 4 numbers in a JSON format.
    # This makes the response easy for our script to parse.
    prompt = f"""
    Based on the topic "{topic}", provide four related and plausible numerical data points.
    These numbers should be suitable as features for a machine learning model.
    Return ONLY a single JSON object in the format: {{"features": [num1, num2, num3, num4]}}.
    Do not include any other text, explanations, or markdown formatting.

    For example, if the topic is "housing prices in a city", a good response would be:
    {{"features": [1200, 3, 2, 1995]}}
    """

    try:
        # Generate content using the Gemini API
        response = model.generate_content(prompt)
        
        # Clean the response text to ensure it is valid JSON
        json_text = response.text.strip().replace('```json', '').replace('```', '')
        gemini_data = json.loads(json_text)
        features = gemini_data.get("features")

        if not features or len(features) != 4:
            print("Error: Gemini did not return the expected list of 4 features.")
            return

        print(f"   - Success! Gemini provided features: {features}")

    except Exception as e:
        print(f"   - An error occurred while communicating with the Gemini API: {e}")
        print(f"   - Raw Gemini response: {response.text}")
        return

    print(f"\n2. Sending these features to your AI container at {DOCKER_API_URL}...")
    try:
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({"features": features})
        
        api_response = requests.post(DOCKER_API_URL, data=payload, headers=headers)
        api_response.raise_for_status()  # Raise an exception for bad status codes (like 404 or 500)

        prediction_data = api_response.json()
        prediction = prediction_data.get('prediction')

        print(f"   - Success! Your container responded.")
        print(f"   - Your Model's Prediction: {prediction}")

    except requests.exceptions.RequestException as e:
        print(f"   - FATAL ERROR: Could not connect to the Docker container.")
        print(f"   - Please ensure your container is running and accessible at {DOCKER_API_URL}")
        print(f"   - Details: {e}")
    except Exception as e:
        print(f"   - An unexpected error occurred during the request: {e}")


if __name__ == "__main__":
    print("--- AI Container Test Client using Gemini API ---")
    print("This script will test the AI service running in your Docker container.")
    print("--------------------------------------------------")
    
    # Get a topic from the user
    user_topic = input("Enter a topic to generate test data (e.g., 'a used car', 'daily weather'): ")
    
    if user_topic:
        test_model_with_gemini(user_topic)