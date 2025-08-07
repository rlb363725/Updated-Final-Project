import plotly.graph_objects as go
from utils import extract_stat, extract_player_stats

__all__ = [
    "plot_team_comparison",
    "plot_rosters",
    "plot_win_probabilities",
    "plot_headlines_and_players",
    "plot_player_comparison",
]

def plot_team_comparison(team1, team2, stats1, stats2):
    # Extract key stats
    team1_off_yards = extract_stat(stats1, "totalYards", key="statAverage")
    team2_off_yards = extract_stat(stats2, "totalYards", key="statAverage")

    team1_def_yards = extract_stat(stats1, "totalYardsOpponent", key="statAverage")
    team2_def_yards = extract_stat(stats2, "totalYardsOpponent", key="statAverage")

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


def plot_player_comparison(players, stat_type, top_n):
    """Display a bar chart comparing top players for a given statistic.

    Parameters
    ----------
    players : list
        Combined list of player dictionaries from both teams.
    stat_type : str
        The statistic key to compare (e.g., ``rushing.yards``).
    top_n : int
        Number of top players to display.
    """

    # Extract (player_name, value) tuples for the requested stat
    stats = extract_player_stats(players, stat_type)

    if not stats:
        print(f"No player stats found for stat type '{stat_type}'.")
        return

    # Sort players by stat value in descending order and take the top N
    top_players = sorted(stats, key=lambda x: x[1], reverse=True)[:top_n]

    names = [name for name, _ in top_players]
    values = [value for _, value in top_players]

    fig = go.Figure([go.Bar(x=names, y=values)])
    fig.update_layout(
        title=f"Top {len(top_players)} Players by {stat_type}",
        xaxis_title="Player",
        yaxis_title=stat_type,
    )

    fig.show()
