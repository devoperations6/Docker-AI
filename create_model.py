import pickle
import os
from sklearn.linear_model import LinearRegression
import numpy as np

# --- Create a dummy model for demonstration ---
# In a real scenario, you would use your own pre-trained model.

# 1. Create dummy data
# Let's imagine a model that predicts a value based on 4 features.
X_train = np.random.rand(100, 4)
# A simple linear relationship for the target
y_train = X_train.dot(np.array([1.5, -2.8, 0.9, 3.1])) + np.random.randn(100) * 0.5

# 2. Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Create the 'models' directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# 4. Save the trained model to a file
model_path = 'models/your_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model trained and saved to '{model_path}'")
print("You can now build the Docker image.")