# Define a base stage that uses the official python runtime base image
FROM python:3.12.10-slim-bullseye AS base

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VERSION=2.1.2

# Add curl for healthcheck
RUN apt update && \
    apt install -y --no-install-recommends curl psmisc && \
    apt clean

# Set the application directory
WORKDIR /app

# Install poetry dependencies
COPY poetry.lock pyproject.toml ./
RUN python -m pip install poetry==$POETRY_VERSION && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-directory --no-cache

# Copy our code from the current folder to the working directory inside the container
COPY ./src .

# Make port 8080 available for metrics
EXPOSE 8000

# Define our command to be run when launching the container
CMD ["celery", "-A", "src.tasks", "worker", "-l", "INFO"]