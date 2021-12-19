FROM python:3.8

WORKDIR /app

ENV DEBUG=False
ENV PORT=8000

ADD . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]