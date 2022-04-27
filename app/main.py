import os

from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
import pymysql

# database = os.environ['MYSQL_DATABASE']
# password = os.environ['MYSQL_ROOT_PASSWORD']
# user = os.environ['MYSQL_USER']
# host = os.environ['HOSTNAME']
# port = '3308'

sqlEngine = create_engine("mysql+pymysql://tyson:root@db/anime_db")
dbConnection = sqlEngine.connect()

app = FastAPI()

@app.get("/")
def index():
    return {"Welcome": "To Tyson's anime website! It's a work in progress.."}

@app.get("/anime/{name}")
def get_user(name: str):
    query = pd.read_sql(f"SELECT * FROM animes WHERE (title = '{name}'", dbConnection)
    return query


