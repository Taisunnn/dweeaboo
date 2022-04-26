import requests
import pandas as pd

anime_list = ["Naruto", "Bleach"]

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
    COLUMNS = ["title"]
    anime_df = pd.DataFrame(combined)
    anime_df = anime_df[COLUMNS]
    return anime_df

def load_animes(filtered_anime: pd.DataFrame) -> None:
    pass

def anime_pipeline(anime_list: list) -> None:
    anime = extract_animes(anime_list)
    print(transform_animes(anime))