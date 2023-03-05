FROM --platform=linux/x86_64 python:3.10.7-slim

# Pre-build variables
ARG PIPENV_EXTRA_ARGS

#For STDIN STDOUT
ENV PYTHONUNBUFFERED=1

#Enter to the project folder if it was created. If not - Docker will create and move into.
WORKDIR /app/

RUN apt-get update \
    # dependencies for building Python packages && cleaning up unused files
    && apt-get install -y build-essential \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
RUN pip install --upgrade pip pipenv setuptools

COPY Pipfile Pipfile.lock ./
RUN pipenv sync --system ${PIPENV_EXTRA_ARGS}

# Current PATH where Docker will copy a current project into folder 'APP'. 
# ROOT PATH is a path were Dockerfile is created
COPY . /app