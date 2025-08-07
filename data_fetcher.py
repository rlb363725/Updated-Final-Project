import os
from dotenv import load_dotenv
import requests
from functools import lru_cache

load_dotenv()  # Load environment variables from .env

@lru_cache(maxsize=None)
def get_api_key():
    """Return the API key from the environment.

    Previously this function prompted the user for input if the key was not
    found which caused automated environments (like the tests in this kata) to
    hang waiting for user input.  Instead we now simply warn and return an
    empty string so callers can decide how to proceed.
    """
    api_key = os.getenv("CFB_API_KEY")
    if not api_key:
        # Avoid interactive prompts which break non‑interactive runs
        print(
            "⚠️  API key not found in environment. Requests will be unauthenticated"
        )
        return ""
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
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(
                f"⚠️  Warning: Failed to fetch team stats for {team}: {response.status_code} — {response.text}"
            )
            return []
        return response.json() or []
    except requests.RequestException as e:
        print(f"⚠️  Warning: Exception fetching team stats for {team}: {e}")
        return []

def get_team_players(team, year):
    """
    Fetch team roster for a given team and season.
    """
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/roster?team={team}&year={year}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(
                f"⚠️  Warning: Failed to fetch roster for {team}: {response.status_code} — {response.text}"
            )
            return []
        return response.json() or []
    except requests.RequestException as e:
        print(f"⚠️  Warning: Exception fetching roster for {team}: {e}")
        return []

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
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(
                f"⚠️  Warning: Failed to search for player {name}: {response.status_code} — {response.text}"
            )
            return []
        return response.json() or []
    except requests.RequestException as e:
        print(f"⚠️  Warning: Exception searching for player {name}: {e}")
        return []








