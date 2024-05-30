# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Set an environment variable
ENV MY_ENV_VARIABLE=value

# Copy the requirements.txt file from your host to the container's working directory
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# [Optional] Uncomment this line if you need to run the container as a non-root user
# USER nonroot

# [Optional] If you want to forward ports, use the EXPOSE instruction to indicate which ports should be exposed
# EXPOSE your_port_number

# Define the default command to run when starting the container
CMD ["python3"]