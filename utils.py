def extract_stat(stat_list, stat_name):
    """
    Extracts a stat value from a list of stat dictionaries based on stat name.
    Returns 0.0 if the stat is not found.
    """
    if not isinstance(stat_list, list):
        print(f"DEBUG: Expected list for stat_list, got {type(stat_list)}")
        return 0.0

    for stat in stat_list:
        if isinstance(stat, dict) and stat.get("statName") == stat_name:
            try:
                return float(stat.get("statValue", 0.0))
            except (TypeError, ValueError):
                print(f"DEBUG: Could not convert stat value to float for '{stat_name}'")
                return 0.0

    print(f"DEBUG: Stat '{stat_name}' not found in list.")
    return 0.0


def predict_score(stats1, stats2):
    """
    Predicts a realistic score for each team based on total yards and opponent defense.
    Returns a tuple of (score1, score2). Will NEVER return None.
    """
    try:
        games1 = extract_stat(stats1, "games") or 1
        games2 = extract_stat(stats2, "games") or 1

        team1_off_yards_pg = extract_stat(stats1, "totalYards") / games1
        team2_off_yards_pg = extract_stat(stats2, "totalYards") / games2

        team1_def_yards_pg = extract_stat(stats1, "totalYardsOpponent") / games1
        team2_def_yards_pg = extract_stat(stats2, "totalYardsOpponent") / games2

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












