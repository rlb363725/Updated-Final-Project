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




