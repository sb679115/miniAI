# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5002

# Create and set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the application port
EXPOSE 5002

# Command to run the Flask app
CMD ["flask", "run"]

