# Use the official Python image from the Docker Hub
#FROM python:3.10-slim
FROM python:3.10.5

# Install necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
git \
libmemcached-dev \
zlib1g-dev \
libssl-dev \
libcurl4-openssl-dev \
libgl1-mesa-glx \
libglib2.0-0 \
&& rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock* /app/

# Install the dependencies
RUN poetry install --no-root

# Copy the application code
COPY main.py .
COPY test.jpg .

# Command to keep the container running
CMD ["sleep", "infinity"]
