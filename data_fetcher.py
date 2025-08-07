import os
from dotenv import load_dotenv
import requests
from functools import lru_cache

load_dotenv()  # Load environment variables from .env

@lru_cache(maxsize=None)
def get_api_key():
    api_key = os.getenv("CFB_API_KEY")
    if not api_key:
        print("⚠️  API key not found in .env file.")
        print("You can get a free API key from https://collegefootballdata.com/key")
        api_key = input("Please enter your CollegeFootballData API key: ").strip()
    return api_key

def get_team_stats(team, year):
    """
    Fetch season-level team stats from CollegeFootballData API.
    """
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/stats/season?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch team stats for {team}: {response.status_code} — {response.text}")

    return response.json()

def get_team_players(team, year):
    """
    Fetch real player stats for a given team and season.
    """
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/stats/player/season?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch player stats for {team}: {response.status_code} — {response.text}")

    return response.json()

def search_player(name):
    """
    Search for a player by name across all teams.
    """
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/player/search?searchTerm={name}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to search for player {name}: {response.status_code} — {response.text}")

    return response.json()








