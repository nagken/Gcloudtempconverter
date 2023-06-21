# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port that the application will run on
EXPOSE 8080

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
