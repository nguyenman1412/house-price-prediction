# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5100

# Set environment variable for Flask
ENV FLASK_APP=src/app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5100"]