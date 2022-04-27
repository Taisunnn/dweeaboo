import requests
import pandas as pd
from sqlalchemy import create_engine

from airflow.hooks.base import BaseHook


def get_animes(title: str) -> dict:
    response = requests.get(f"https://api.jikan.moe/v3/search/anime?q={title}")
    return response.json()

def extract_animes(anime_list: list) -> list:
    combined = []
    for title in anime_list:
        anime_raw_info = get_animes(title)["results"]
        combined += anime_raw_info

    return combined

def transform_animes(combined: list) -> pd.DataFrame:
    COLUMNS = ["title", "score"]
    anime_df = pd.DataFrame(combined)
    anime_df = anime_df[COLUMNS]
    print(anime_df)
    return anime_df

def load_animes(filtered_anime: pd.DataFrame) -> None:

    AIRFLOW_CONN_ID = "anime_db"
    TABLE = "animes"

    print("Connecting to the database...")

    conn = BaseHook.get_connection(AIRFLOW_CONN_ID)
    engine = create_engine(f"mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{AIRFLOW_CONN_ID}")

    print("Connected to the database...")

    print("Loading animes to database...")
    filtered_anime.to_sql(
        name=TABLE, 
        con=engine,
        if_exists="append", 
        index=False, 
        )
    print("Finished loading users to database!")


def anime_pipeline(anime_list: list) -> None:
    anime = extract_animes(anime_list)
    clean_data = transform_animes(anime)
    _     = load_animes(clean_data)