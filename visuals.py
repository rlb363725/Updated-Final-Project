import plotly.graph_objects as go
from utils import extract_stat

def plot_team_comparison(team1, team2, stats1, stats2):
    # Extract key stats
    team1_off_yards = extract_stat(stats1, "totalYards")
    team2_off_yards = extract_stat(stats2, "totalYards")

    team1_def_yards = extract_stat(stats1, "totalYardsOpponent")
    team2_def_yards = extract_stat(stats2, "totalYardsOpponent")

    categories = ["Offensive Yards", "Defensive Yards Allowed"]
    team1_values = [team1_off_yards, team1_def_yards]
    team2_values = [team2_off_yards, team2_def_yards]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=team1_values,
        name=team1
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=team2_values,
        name=team2
    ))

    fig.update_layout(
        title=f"{team1} vs {team2} - Yardage Comparison",
        xaxis_title="Category",
        yaxis_title="Yards",
        barmode='group'
    )

    fig.show()


def plot_player_comparison(player_stats, stat_type="passingYards", top_n=5):
    """
    Plot comparison of top N players by a specific stat.
    `player_stats` should be the result of get_team_players(team, year)
    """
    # Filter out None players and players without the specified statType
    filtered_players = [
        p for p in player_stats 
        if p and p.get("statType") == stat_type and p.get("stat") is not None
    ]
    
    # Sort players by stat value
    sorted_players = sorted(
        filtered_players, 
        key=lambda p: float(p["stat"]), 
        reverse=True
    )[:top_n]

    if not sorted_players:
        print(f"⚠️  Warning: No players found with stat type '{stat_type}'. Skipping plot.")
        return

    names = [p.get("player", "Unknown") for p in sorted_players]
    stats = [float(p["stat"]) for p in sorted_players]

    fig = go.Figure([go.Bar(x=names, y=stats)])

    fig.update_layout(
        title=f"Top {top_n} Players by {stat_type}",
        xaxis_title="Player",
        yaxis_title=stat_type,
        template="plotly_white"
    )

    fig.show()
import plotly.graph_objects as go

def plot_win_probabilities(team1, team2, win_prob1, win_prob2):
    """
    Plots a pie chart of win probabilities.
    """
    fig = go.Figure(data=[
        go.Pie(labels=[team1, team2],
               values=[win_prob1, win_prob2],
               hole=0.4,
               hoverinfo='label+percent',
               textinfo='label+value')
    ])
    
    fig.update_layout(
        title_text=f"Win Probabilities: {team1} vs {team2}",
        annotations=[dict(text='Win %', x=0.5, y=0.5, font_size=18, showarrow=False)]
    )
    
    fig.show()

def plot_headlines_and_players(team1, team2):
    """
    Placeholder for future implementation of headlines or player highlights.
    """
    print(f"[Visual Placeholder] Headlines and player highlights for {team1} vs {team2}.")
