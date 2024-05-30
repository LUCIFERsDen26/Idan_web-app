# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the requirements.txt file from your host to the container's working directory
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# [Optional] If you want to forward ports, use the EXPOSE instruction to indicate which ports should be exposed
EXPOSE 5000

# Define the default command to run when starting the container
CMD ["python", "-m", "flask", "run"]