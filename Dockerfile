FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /
WORKDIR /

# Install dependencies into a virtualenv
RUN pip install --upgrade pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --dev --deploy

# Copy project code
COPY . /
