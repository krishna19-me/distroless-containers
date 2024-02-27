# Use the official Python image as the base image
FROM python:3.10-slim
 
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
# Set the working directory in the container
WORKDIR /app
 
# Copy the requirements file into the container at /app
COPY requirements.txt /app
 
# Install any dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
 
# Copy the Flask application code into the container at /app
COPY . /app
 
# Expose port 5000 to the outside world
EXPOSE 5000
 
# Run the Flask application
CMD ["python3", "app.py"]
