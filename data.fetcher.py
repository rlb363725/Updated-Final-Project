import os
import requests

def get_team_stats(team, year):
    api_key = os.getenv("CFB_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }
    url = f"https://api.collegefootballdata.com/stats/season?year={year}&team={team}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch stats for {team}: {response.status_code}")

    return response.json()
