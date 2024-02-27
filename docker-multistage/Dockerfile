# Stage 1: Build the application
FROM python:3.10 as builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the Flask application code into the container at /app
COPY . /app/

# Stage 2: Create the final image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built application from the previous stage
COPY --from=builder /app /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the Flask application
CMD ["python3", "app.py"]

