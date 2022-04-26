import os

from typing import Optional
from fastapi import FastAPI
from pymysql import DatabaseError
from sqlalchemy import create_engine
import pandas as pd
import pymysql

# database = os.environ['MYSQL_DATABASE']
# password = os.environ['MYSQL_ROOT_PASSWORD']
# user = os.environ['MYSQL_USER']
# host = 'localhost'
# port = '3308'

# sqlEngine = create_engine(f"mysql+pymysql://{host}:{password}@{host}/{database}")
# dbConnection = sqlEngine.connect()

app = FastAPI()

@app.get("/")
def index():
    return {"Welcome": "To Tyson's anime website! It's a work in progress.."}

@app.get("/anime/{name}")
def get_user(dbConnection, name: str):
    query = pd.read_sql(f"SELECT * FROM animes WHERE (anime_name = {name})", dbConnection)
    return query


