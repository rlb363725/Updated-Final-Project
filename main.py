from matchup import simulate_matchup
from data_fetcher import get_team_players, get_api_key
from utils import summarize_player_stats
from visuals import plot_player_comparison

def main():
    print("🏈 College Football Matchup Analyzer")
    print("------------------------------------")

    # Prompt for API key if it hasn't been provided via environment variable.
    # This ensures the user is asked at least once per session.
    get_api_key()

    team1 = input("Enter the first team (e.g., Ohio State): ")
    team2 = input("Enter the second team (e.g., Michigan): ")
    year = input("Enter the season year (e.g., 2024): ")

    print("\nWhat would you like to view?")
    print("1. Team Stats & Score Prediction")
    print("2. Player Stats Summary")
    print("3. Top Player Comparison Chart")
    print("4. All of the Above")

    choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

    try:
        if choice in ("1", "4"):
            result = simulate_matchup(team1, team2, year)
            print("\n✅ Simulation complete!")
            print(f"🏆 Predicted Score — {team1}: {result['score1']}, {team2}: {result['score2']}")

        if choice in ("2", "4"):
            players1 = get_team_players(team1, year)
            players2 = get_team_players(team2, year)

            stat_type = input("Enter stat type to summarize (e.g., rushing.yards, passing.yards, receiving.yards, fumbles.rec, tackles, sacks, interceptions): ").strip()

            print(f"\n📊 {team1} {stat_type} Summary:")
            summary1 = summarize_player_stats(players1, stat_type)
            for key, val in summary1.items():
                print(f"{key.capitalize()}: {val:.2f}")

            print(f"\n📊 {team2} {stat_type} Summary:")
            summary2 = summarize_player_stats(players2, stat_type)
            for key, val in summary2.items():
                print(f"{key.capitalize()}: {val:.2f}")

        if choice in ("3", "4"):
            players1 = get_team_players(team1, year)
            players2 = get_team_players(team2, year)

            stat_type = input("Enter stat type to compare top players (e.g., rushing.yards, passing.yards, receiving.yards, fumbles.rec, tackles, sacks, interceptions): ").strip()
            top_n = input("How many top players to display per team? (e.g., 5): ").strip()

            try:
                top_n = int(top_n)
            except ValueError:
                top_n = 5

            combined_players = players1 + players2
            plot_player_comparison(combined_players, stat_type=stat_type, top_n=top_n)

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()











