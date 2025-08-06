import plotly.graph_objects as go
import random

def plot_team_comparison(team1, team2, stats1, stats2):
    def get_stat(stats, name):
        for stat in stats:
            if stat.get("statName") == name:
                return stat.get("statValue", 0.0)
        return 0.0

    categories = ["totalYards", "netPassingYards", "rushingYards", "turnovers", "thirdDownConversions"]
    labels = ["Total Yards", "Passing Yards", "Rushing Yards", "Turnovers", "3rd Down Conversions"]

    team1_vals = [get_stat(stats1, stat) for stat in categories]
    team2_vals = [get_stat(stats2, stat) for stat in categories]

    fig = go.Figure(data=[
        go.Bar(name=team1, x=labels, y=team1_vals),
        go.Bar(name=team2, x=labels, y=team2_vals)
    ])
    fig.update_layout(
        title="Team Stat Comparison",
        barmode='group'
    )
    fig.show()

def plot_win_probabilities(team1, team2, prob1, prob2):
    fig = go.Figure(data=[
        go.Pie(labels=[team1, team2], values=[prob1, prob2], hole=0.4)
    ])
    fig.update_layout(title="Win Probability")
    fig.show()

def plot_headlines_and_players(team1, team2):
    def generate_fake_players(team):
        first_names = ["Mike", "Chris", "Jordan", "Taylor", "Alex", "Ryan", "Nick", "James"]
        last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Moore", "Taylor", "Anderson"]
        return [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(3)]

    team1_players = generate_fake_players(team1)
    team2_players = generate_fake_players(team2)

    fig = go.Figure()

    fig.add_trace(go.Table(
        header=dict(values=[f"{team1} Headlines", f"{team2} Headlines"]),
        cells=dict(values=[
            team1_players,
            team2_players
        ])
    ))

    fig.update_layout(title="Headline Players")
    fig.show()
