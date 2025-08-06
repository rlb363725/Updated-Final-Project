from data_fetcher import get_team_stats
from utils import predict_score, extract_stat, calculate_win_probability
from visuals import plot_team_comparison, plot_win_probability, plot_headline_board

def print_stat_summary(team_name, stats):
    total_yards = extract_stat(stats, "totalYards")
    passing_yards = extract_stat(stats, "netPassingYards")
    rushing_yards = extract_stat(stats, "rushingYards")

    print(f"\n📊 {team_name} Stat Summary:")
    print(f"  • Total Yards: {total_yards}")
    print(f"  • Passing Yards: {passing_yards}")
    print(f"  • Rushing Yards: {rushing_yards}")

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    score1, score2 = predict_score(stats1, stats2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    result = f"\n--- Matchup Result ---\n{team1} {score1} - {score2} {team2} → Winner: {winner}"
    print(result)

    # Print terminal summaries
    print_stat_summary(team1, stats1)
    print_stat_summary(team2, stats2)

    # Print win probabilities
    team1_prob, team2_prob = calculate_win_probability(score1, score2)
    print(f"\n📈 Win Probability:")
    print(f"  • {team1}: {team1_prob * 100:.1f}%")
    print(f"  • {team2}: {team2_prob * 100:.1f}%")

    # Show visuals
    plot_team_comparison(team1, team2, stats1, stats2)
    plot_win_probability(team1, team2, score1, score2)
    plot_headline_board(team1, team2)

    return result




