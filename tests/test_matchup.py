import pytest
from matchup import simulate_matchup

def test_simulate_matchup_runs():
    result = simulate_matchup("Georgia", "Michigan", 2023)
    assert "Winner" in result

def mock_get_team_stats(team, year):
    # Fake stats for controlled testing
    if team == "Ohio State":
        return [{"category": "offense", "stat": 500}]
    elif team == "Michigan":
        return [{"category": "offense", "stat": 450}]
    return []

def test_simulate_matchup_with_mock(monkeypatch):
    # Monkeypatch the real data_fetcher.get_team_stats
    monkeypatch.setattr("matchup.get_team_stats", mock_get_team_stats)

    result = simulate_matchup("Ohio State", "Michigan", "2023")
    assert "

