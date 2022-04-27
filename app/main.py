import os

from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

database = os.environ["MYSQL_DATABASE"]
password = os.environ["MYSQL_ROOT_PASSWORD"]
user = os.environ["MYSQL_USER"]
host = os.environ["HOSTNAME"]

sqlEngine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
dbConnection = sqlEngine.connect()

app = FastAPI()


@app.get("/")
def index():
    return {"Welcome": "To Tyson's anime website! It's a work in progress.."}


@app.get("/anime/{name}")
def get_user(name: str):
    query = pd.read_sql(f"SELECT * FROM animes WHERE (title = '{name}'", dbConnection)
    return query
