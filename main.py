from matchup import simulate_matchup

def main():
    print("College Football Matchup Analyzer")
    print("------------------------------------")

    team1 = input("Enter the first team (e.g., Ohio State): ")
    team2 = input("Enter the second team (e.g., Michigan): ")
    year = input("Enter the season year (e.g., 2023): ")

    try:
        result = simulate_matchup(team1, team2, year)
        print("\nSimulation complete!")
    except Exception as e:
        print(f"\n Error: {e}")

if __name__ == "__main__":
    main()










