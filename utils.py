def extract_stat(stat_list, stat_name, key="statValue"):
    """
    Extracts a stat value from a list of stat dictionaries based on stat name.
    The ``key`` parameter controls which value to pull (e.g., ``statValue`` for
    totals or ``statAverage`` for per-game averages). Returns 0.0 if the stat is
    not found.
    """
    if not isinstance(stat_list, list):
        print(f"DEBUG: Expected list for stat_list, got {type(stat_list)}")
        return 0.0

    for stat in stat_list:
        if isinstance(stat, dict) and stat.get("statName") == stat_name:
            try:
                return float(stat.get(key, 0.0))
            except (TypeError, ValueError):
                print(f"DEBUG: Could not convert stat value to float for '{stat_name}'")
                return 0.0

    print(f"DEBUG: Stat '{stat_name}' not found in list.")
    return 0.0


def predict_score(stats1, stats2):
    """
    Predicts a realistic score for each team based on per-game yardage averages
    and opponent defensive averages. Returns a tuple of (score1, score2).
    """
    try:
        team1_off_yards_pg = extract_stat(stats1, "totalYards", key="statAverage")
        team2_off_yards_pg = extract_stat(stats2, "totalYards", key="statAverage")

        team1_def_yards_pg = extract_stat(stats1, "totalYardsOpponent", key="statAverage")
        team2_def_yards_pg = extract_stat(stats2, "totalYardsOpponent", key="statAverage")

        team1_score = int(((team1_off_yards_pg + team2_def_yards_pg) / 2) * 0.1)
        team2_score = int(((team2_off_yards_pg + team1_def_yards_pg) / 2) * 0.1)

        return team1_score, team2_score

    except Exception as e:
        print("ERROR in predict_score:", e)
        return 0, 0


def extract_player_stats(player_list, stat_type):
    """
    Filters and extracts stats for players matching the specified stat type.
    Returns a list of tuples: (player_name, stat_value).
    """
    if not isinstance(player_list, list):
        print(f"DEBUG: Expected list for player_list, got {type(player_list)}")
        return []

    results = []
    for player in player_list:
        if player.get("statType") == stat_type:
            try:
                value = float(player.get("stat", 0.0))
                results.append((player.get("player", "Unknown"), value))
            except (TypeError, ValueError):
                print(f"DEBUG: Failed to convert stat for player {player.get('player', 'Unknown')}")
    return results


def summarize_player_stats(player_list, stat_type):
    """
    Summarizes player statistics by stat_type.
    Returns a dictionary with total, average, max, min, and count of players.
    """
    extracted = extract_player_stats(player_list, stat_type)
    values = [v for _, v in extracted]

    if not values:
        return {
            "total": 0.0,
            "average": 0.0,
            "max": 0.0,
            "min": 0.0,
            "count": 0
        }

    return {
        "total": sum(values),
        "average": sum(values) / len(values),
        "max": max(values),
        "min": min(values),
        "count": len(values)
    }
def calculate_win_probability(score1, score2):
    """
    Calculates win probabilities based on predicted scores.
    Returns a tuple of percentages (team1, team2).
    """
    total = score1 + score2
    if total == 0:
        return 50.0, 50.0  # default if tied at 0

    prob1 = (score1 / total) * 100
    prob2 = (score2 / total) * 100
    return round(prob1, 1), round(prob2, 1)












