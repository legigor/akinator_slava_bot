FROM python:3.7.4-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY akinator .
COPY main.py .
ENTRYPOINT [ "python", "main.py" ]