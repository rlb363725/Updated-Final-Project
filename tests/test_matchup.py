import os
import sys

import pytest

# Ensure project root is on the Python path for direct module imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from matchup import simulate_matchup

def test_simulate_matchup_runs():
    result = simulate_matchup("Georgia", "Michigan", 2023)
    assert "winner" in result
    assert isinstance(result["score1"], int)
    assert isinstance(result["score2"], int)

# Mock version of get_team_stats to inject test data
def mock_get_team_stats(team, year):
    if team == "Ohio State":
        return [
            {"statName": "games", "statValue": 1},
            {"statName": "totalYards", "statValue": 500, "statAverage": 500},
            {"statName": "totalYardsOpponent", "statValue": 350, "statAverage": 350}
        ]
    elif team == "Michigan":
        return [
            {"statName": "games", "statValue": 1},
            {"statName": "totalYards", "statValue": 450, "statAverage": 450},
            {"statName": "totalYardsOpponent", "statValue": 400, "statAverage": 400}
        ]
    return []

def test_simulate_matchup_with_mock(monkeypatch):
    # Patch matchup.get_team_stats to use mock instead of real API
    monkeypatch.setattr("matchup.get_team_stats", mock_get_team_stats)

    result = simulate_matchup("Ohio State", "Michigan", 2023)
    assert result["winner"] in ["Ohio State", "Michigan", "Tie"]
    assert isinstance(result["score1"], int)
    assert isinstance(result["score2"], int)
