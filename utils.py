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
            return float(stat.get("statValue", 0.0))

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
        return 0, 0  # Always return a tuple to avoid unpacking error


def calculate_win_probability(score1, score2):
    """
    Converts predicted scores into win probabilities.
    Returns a tuple: (team1_prob, team2_prob)
    """
    total = score1 + score2
    if total == 0:
        return 0.5, 0.5
    team1_prob = round(score1 / total, 4)
    team2_prob = round(score2 / total, 4)
    return team1_prob, team2_prob












