FROM python:3.11.6-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY docker_first.py .

RUN echo "Hello from installing"

CMD ["python", "docker_first.py"]
