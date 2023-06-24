# Use the official Python base image
FROM python:3.9

# Add your Dockerfile instructions here
EXPOSE 8080

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the command to run the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
