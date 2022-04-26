FROM python:3.9

#spin up fastapi webserver, 

WORKDIR /code
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY app /app

CMD ["uvicorn", "app.main:app", "--reload"]