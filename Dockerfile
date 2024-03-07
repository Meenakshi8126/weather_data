# Use the official Python image from Docker Hub
FROM python:3.11.1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY weather_data.py .

# Command to run the Python script when the container starts
CMD ["python", "weather_data.py"]

