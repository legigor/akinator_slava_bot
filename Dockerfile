FROM python:3.7.4-alpine

LABEL VERSION "$VERSION"
LABEL GITHUB_SHA "$GITHUB_SHA"
LABEL GITHUB_REPOSITORY "$GITHUB_REPOSITORY"
LABEL MAINTAINER="Igor Tamashchuk <legigor@gmail.com>"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY akinator .
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]