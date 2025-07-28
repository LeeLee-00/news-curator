# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /backend

# Copy the requirements file into the container
COPY backend/requirements.txt requirements.txt
COPY backend/app app
COPY shared_models shared_models

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
EXPOSE 8527

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8527", "--reload"]
