import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load environment variables from .env

def get_team_stats(team, year):
    api_key = os.getenv("CFB_API_KEY")
    if not api_key:
        raise Exception("API key not found. Make sure .env file is configured correctly.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/stats/season?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch stats for {team}: {response.status_code} — {response.text}")

    return response.json()







