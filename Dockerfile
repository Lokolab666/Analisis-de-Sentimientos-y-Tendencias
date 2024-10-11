
FROM python:3.9-slim

WORKDIR /Despliegue

# Copy the current directory contents into the container at /app
COPY . /Despliegue

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8070

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8070"]
