import os

from typing import Optional

from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

from app.common.logger import get_logger


logger = get_logger(__name__)
parent_dir_path = os.path.dirname(os.path.realpath(__file__))

database = os.environ["MYSQL_DATABASE"]
password = os.environ["MYSQL_ROOT_PASSWORD"]
user = os.environ["MYSQL_USER"]
host = os.environ["MYSQL_HOST"]

sqlEngine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
Session = sessionmaker(bind = sqlEngine)
session = Session()

app = FastAPI()

Base = declarative_base()

class Animes(Base):
    
    __tablename__ = 'animes'
    anime_id = Column(Integer, primary_key =  True)
    title = Column(String)
    score = Column(Float)
    synopsis = Column(String)
    episodes = Column(String)
    rated = Column(String)


templates = Jinja2Templates(directory=parent_dir_path + "/templates")
app.mount('/static', StaticFiles(directory=(parent_dir_path + "/static")), name="static")

IMAGES = { 
    "naruto": "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg", 
    "bleach": "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Bleachanime.png/220px-Bleachanime.png" 
}

#add images to database

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("home.html", context)

@app.get("/search/")
def get_anime(request: Request, query:Optional[str]):
    logger.info("Received Request. Reading Results from Model...")
    results = session.query(Animes).filter(Animes.title.contains(query.lower()))
    logger.info("Returning Template")
    context = {'request' : request, 'results' : results}
    if results.count() == 0:
        return templates.TemplateResponse("invalid.html", context)  
    else:
        return templates.TemplateResponse("anime.html", {'request': request, 'results': results[0]})   

@app.get("/about", response_class=HTMLResponse)
def index(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("about.html", context)

@app.get("/contact", response_class=HTMLResponse)
def index(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("contact.html", context)

@app.get("/fundme", response_class=HTMLResponse)
def index(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("fundme.html", context)