import os
import sys
from dotenv import load_dotenv
import requests
from functools import lru_cache
try:
    import cfbd
except ImportError:  # pragma: no cover - handle missing dependency gracefully
    cfbd = None

try:
    import cfbd
except ImportError:  # pragma: no cover - handled gracefully
    cfbd = None

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
    Fetch season-level team stats from CollegeFootballData API using the official
    ``cfbd`` client. Both total values and per-game averages are returned for
    downstream consumption.
    """

    # Configure API client
    if cfbd is None:
        print("⚠️  cfbd library not installed. Returning empty stats list.")
        return []

    configuration = cfbd.Configuration()
    api_key = get_api_key()
    if api_key:
        configuration.api_key["Authorization"] = api_key
        configuration.api_key_prefix["Authorization"] = "Bearer"

    try:
        with cfbd.ApiClient(configuration) as api_client:
            api_instance = cfbd.StatsApi(api_client)
            data = api_instance.get_team_season_stats(year=year, team=team)
    except Exception as e:  # Broad catch to avoid failing in environments without network
        print(
            f"⚠️  Warning: Exception fetching team stats for {team}: {e}"
        )
        return []

    if not data:
        return []

    team_stats = data[0]
    games = getattr(team_stats, "games", 0) or 0
    results = [{"statName": "games", "statValue": games}]

    for stat in getattr(team_stats, "stats", []) or []:
        name = getattr(stat, "stat_name", "")
        total = float(getattr(stat, "stat_value", 0) or 0)
        average = total / games if games else 0.0
        results.append({
            "statName": name,
            "statValue": total,
            "statAverage": average,
        })

    return results

def get_team_players(team, year):
    """Fetch season player statistics for a team using the CFBD client."""

    if cfbd is None:
        print("⚠️  Warning: cfbd library is not installed. Returning empty player list.")
        return []

    api_key = get_api_key()
    configuration = cfbd.Configuration()
    if api_key:
        configuration.api_key["Authorization"] = api_key
        configuration.api_key_prefix["Authorization"] = "Bearer"

    try:
        with cfbd.ApiClient(configuration) as api_client:
            api_instance = cfbd.StatsApi(api_client)
            stats = api_instance.get_player_season_stats(team=team, year=year) or []
            return [
                {
                    "player": s.player,
                    "statType": s.stat_type,
                    "stat": s.stat,
                }
                for s in stats
            ]
    except Exception as e:  # noqa: broad-except
        print(f"⚠️  Warning: Exception fetching player stats for {team}: {e}")
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








