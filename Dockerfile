FROM python:3.11.6-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

#RUN apt-get upgrade
RUN python -m pip install --upgrade pip
RUN pip install poetry


COPY . .
RUN poetry install

CMD ["python", "iss_main.py"]
