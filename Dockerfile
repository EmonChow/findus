# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    # apt-get install -y gcc libmariadb-dev default-libmysqlclient-dev build-essential pkg-config && \
    apt-get install -y gcc libmariadb-dev default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

    
# Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the spaCy model from the local machine
COPY en_core_web_sm-3.7.1-py3-none-any.whl /tmp/en_core_web_sm-3.7.1-py3-none-any.whl

# Install necessary packages
RUN pip install spacy==3.7.6

# Install the downloaded spaCy model
RUN pip install /tmp/en_core_web_sm-3.7.1-py3-none-any.whl

COPY . /usr/src/app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]