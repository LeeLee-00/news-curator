# Use the official Python image as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /frontend

# Copy the requirements file into the container
COPY front/requirements.txt requirements.txt
COPY front/app app
COPY shared_models shared_models

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8523

# Run the Streamlit app
CMD ["streamlit", "run", "app/main.py", "--server.port=8523", "--server.address=0.0.0.0"]
