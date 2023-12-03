FROM python:3.11.6-slim

RUN mkdir my_reserve
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get upgrade


COPY . .

RUN echo "Hello from installing"

CMD ["python", "weather.py", "Тернопіль", "Львів", "Київ"]
