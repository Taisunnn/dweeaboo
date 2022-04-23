FROM python:3.9

#spin up fastapi webserver

WORKDIR /code
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app app
COPY ./airflow dags
RUN export AIRFLOW_HOME=airflow

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["airflow", "standalone"]