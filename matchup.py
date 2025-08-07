from data_fetcher import get_team_stats, get_team_players
from utils import predict_score, extract_stat, summarize_player_stats, calculate_win_probability
from visuals import (
    plot_team_comparison,
    plot_win_probabilities,
    plot_player_comparison
)

def simulate_matchup(team1, team2, year):
    # Fetch team-level stats
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    # Fetch player stats
    players1 = get_team_players(team1, year)
    players2 = get_team_players(team2, year)

    # Predict score and win probability
    score1, score2 = predict_score(stats1, stats2)
    win_prob1, win_prob2 = calculate_win_probability(score1, score2)

    # Determine winner
    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    # Print stat summaries
    print(f"\n--- 📊 Stat Summary ---")
    print(f"{team1} - Total Yards: {extract_stat(stats1, 'totalYards')}, "
          f"Passing: {extract_stat(stats1, 'netPassingYards')}, "
          f"Rushing: {extract_stat(stats1, 'rushingYards')}")
    print(f"{team2} - Total Yards: {extract_stat(stats2, 'totalYards')}, "
          f"Passing: {extract_stat(stats2, 'netPassingYards')}, "
          f"Rushing: {extract_stat(stats2, 'rushingYards')}")

    # Print result
    print(f"\n--- 🏆 Matchup Result ---")
    print(f"{team1} {score1} - {score2} {team2} → Winner: {winner}")

    # Display visualizations
    plot_team_comparison(team1, team2, stats1, stats2)
    plot_win_probabilities(team1, team2, win_prob1, win_prob2)
    plot_player_comparison(players1, stat_type="passingYards")
    plot_player_comparison(players2, stat_type="rushingYards")

