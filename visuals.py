import plotly.graph_objects as go

def plot_team_comparison(team1, team2, stats1, stats2):
    categories = ["Total Yards", "Yards Allowed", "Passing Yards", "Rushing Yards"]
    team1_vals = [
        extract_stat(stats1, "totalYards"),
        extract_stat(stats1, "totalYardsOpponent"),
        extract_stat(stats1, "netPassingYards"),
        extract_stat(stats1, "rushingYards")
    ]
    team2_vals = [
        extract_stat(stats2, "totalYards"),
        extract_stat(stats2, "totalYardsOpponent"),
        extract_stat(stats2, "netPassingYards"),
        extract_stat(stats2, "rushingYards")
    ]

    fig = go.Figure(data=[
        go.Bar(name=team1, x=categories, y=team1_vals),
        go.Bar(name=team2, x=categories, y=team2_vals)
    ])
    fig.update_layout(
        title="Team Stat Comparison",
        barmode='group'
    )
    fig.show()

def plot_win_probability(team1, team2, score1, score2):
    total = score1 + score2
    if total == 0:
        probs = [0.5, 0.5]
    else:
        probs = [score1 / total, score2 / total]

    fig = go.Figure(data=[
        go.Pie(labels=[team1, team2], values=probs, hole=0.4)
    ])
    fig.update_layout(title="Win Probability Prediction")
    fig.show()

def plot_headline_board(team1, team2):
    headline = f"{team1} vs {team2}: Clash of the Titans!"
    team1_players = ["QB: J. Smith", "RB: K. Brown", "WR: A. Lee"]
    team2_players = ["QB: D. Johnson", "RB: M. White", "WR: S. Davis"]

    fig = go.Figure()

    # Add headline
    fig.add_trace(go.Scatter(
        x=[0.5],
        y=[1.1],
        text=[f"<b>{headline}</b>"],
        mode="text",
        textfont=dict(size=24),
        showlegend=False
    ))

    # Add player boards
    fig.add_trace(go.Scatter(
        x=[0.25]*3,
        y=[0.8, 0.7, 0.6],
        text=team1_players,
        mode="text",
        textfont=dict(size=18),
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=[0.75]*3,
        y=[0.8, 0.7, 0.6],
        text=team2_players,
        mode="text",
        textfont=dict(size=18),
        showlegend=False
    ))

    fig.update_layout(
        title="Headline & Player Board",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=500,
        margin=dict(l=0, r=0, t=80, b=0)
    )

    fig.show()

def extract_stat(stat_list, stat_name):
    if not isinstance(stat_list, list):
        return 0.0
    for stat in stat_list:
        if isinstance(stat, dict) and stat.get("statName") == stat_name:
            return float(stat.get("statValue", 0.0))
    return 0.0
