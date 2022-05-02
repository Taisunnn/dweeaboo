import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
import pandas as pd

database = os.environ["MYSQL_DATABASE"]
password = os.environ["MYSQL_ROOT_PASSWORD"]
user = os.environ["MYSQL_USER"]
host = os.environ["MYSQL_HOST"]

sqlEngine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
dbConnection = sqlEngine.connect()

app = FastAPI()

templates = Jinja2Templates(directory="app")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context)


@app.get("/anime/{name}", response_class=HTMLResponse)
def get_anime(request: Request, name: str):
    query = pd.read_sql(f"SELECT * FROM animes WHERE (title = '{name.lower()}')", dbConnection)
    query = query.to_dict('records')[0]
    context = {'request' : request, 'query' : query}
    return templates.TemplateResponse("anime.html", context)