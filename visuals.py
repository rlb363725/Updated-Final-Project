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


def plot_rosters(team1, players1, team2, players2):
    """
    Displays the rosters for both teams in a table.
    """
    team1_names = [f"{p.get('first_name', '')} {p.get('last_name', '')}" for p in players1]
    team2_names = [f"{p.get('first_name', '')} {p.get('last_name', '')}" for p in players2]

    # Pad the shorter list with empty strings to make them equal length
    len1, len2 = len(team1_names), len(team2_names)
    if len1 > len2:
        team2_names.extend([''] * (len1 - len2))
    elif len2 > len1:
        team1_names.extend([''] * (len2 - len1))

    fig = go.Figure(data=[go.Table(
        header=dict(values=[team1, team2]),
        cells=dict(values=[team1_names, team2_names])
    )])

    fig.update_layout(title_text=f"{team1} vs {team2} Roster")
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
