# Start from a stable, slim Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's build cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (app.py, models folder) into the container
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# The command to run the application when the container starts
CMD ["python", "app.py"]