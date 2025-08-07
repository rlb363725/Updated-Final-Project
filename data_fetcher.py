import os
import sys
from dotenv import load_dotenv
import requests
from functools import lru_cache

load_dotenv()  # Load environment variables from .env

@lru_cache(maxsize=None)
def get_api_key():
    """Retrieve the CFBD API key.

    The key is first pulled from the ``CFB_API_KEY`` environment variable. If
    it is not present and the session is interactive, the user is prompted once
    for the key.  Non-interactive sessions (such as automated tests) skip the
    prompt and proceed without a key.
    """
    api_key = os.getenv("CFB_API_KEY")
    if api_key:
        return api_key

    if os.getenv("PYTEST_CURRENT_TEST") or not sys.stdin.isatty():
        print(
            "⚠️  API key not found in environment. Requests will be unauthenticated"
        )
        return ""

    # Prompt the user once for their API key
    api_key = input(
        "Enter your CollegeFootballData API key (free at collegefootballdata.com): "
    ).strip()
    if not api_key:
        print("You can obtain a free key at https://collegefootballdata.com")
    os.environ["CFB_API_KEY"] = api_key
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








