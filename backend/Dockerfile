# Use the official Python image from the Docker Hub
FROM python:3.14-slim

# Set the working directory in the container
WORKDIR /app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Force stdout/stderr to be unbuffered
ENV PYTHONUNBUFFERED=1

# Install uv
RUN pip install uv

COPY pyproject.toml uv.lock ./

# This command will sync the dependencies listed in the uv.lock file with the environment
# The --frozen flag ensures that the dependencies are installed in a frozen state, meaning that their versions will not be changed even if a newer version is available.
RUN uv sync --frozen

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]