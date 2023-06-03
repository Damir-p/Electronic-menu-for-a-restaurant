FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENV DJANGO_SETTINGS_MODULE main.settings

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

