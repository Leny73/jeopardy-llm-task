# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the app's port
EXPOSE 8000

# Command to run the app (exec form)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]