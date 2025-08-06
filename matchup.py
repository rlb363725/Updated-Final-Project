from data_fetcher import get_team_stats
from utils import predict_score, extract_stat, calculate_win_probability
from visuals import (
    plot_team_comparison,
    plot_win_probabilities,
    plot_headlines_and_players
)

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    score1, score2 = predict_score(stats1, stats2)
    win_prob1, win_prob2 = calculate_win_probability(score1, score2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    # Print stat summaries to terminal
    print(f"\n--- Stat Summary ---")
    print(f"{team1} - Total Yards: {extract_stat(stats1, 'totalYards')}, Passing: {extract_stat(stats1, 'netPassingYards')}, Rushing: {extract_stat(stats1, 'rushingYards')}")
    print(f"{team2} - Total Yards: {extract_stat(stats2, 'totalYards')}, Passing: {extract_stat(stats2, 'netPassingYards')}, Rushing: {extract_stat(stats2, 'rushingYards')}")
    print(f"\n--- Matchup Result ---")
    print(f"{team1} {score1} - {score2} {team2} → Winner: {winner}")
    print(f"\nWin Probability: {team1} {win_prob1}% | {team2} {win_prob2}%")

    # Show all visuals
    plot_team_comparison(team1, team2, stats1, stats2)
    plot_win_probabilities(team1, team2, win_prob1, win_prob2)
    plot_headlines_and_players(team1, team2)

    return score1, score2

