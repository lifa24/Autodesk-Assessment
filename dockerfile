FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./logging_config.ini /app/logging_config.ini

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "assessment.py"]