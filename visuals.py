import plotly.graph_objects as go

def plot_team_comparison(team1, team2, stats1, stats2):
    team1_off = get_ppg(stats1)
    team1_def = get_ppg_allowed(stats1)

    team2_off = get_ppg(stats2)
    team2_def = get_ppg_allowed(stats2)

    categories = ['Offensive PPG', 'Defensive PPG Allowed']
    team1_values = [team1_off, team1_def]
    team2_values = [team2_off, team2_def]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=categories, y=team1_values, name=team1))
    fig.add_trace(go.Bar(x=categories, y=team2_values, name=team2))

    fig.update_layout(
        title='Team Stat Comparison',
        barmode='group',
        xaxis_title='Category',
        yaxis_title='Points Per Game',
    )
    fig.show()

def plot_win_probability(team1, team2, score1, score2):
    if score1 == score2:
        win_probs = [50, 50]
    else:
        total = score1 + score2
        win_probs = [round(score1 / total * 100, 1), round(score2 / total * 100, 1)]

    labels = [team1, team2]
    colors = ['royalblue', 'crimson']

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=win_probs,
        hole=.4,
        marker=dict(colors=colors),
        hoverinfo='label+percent',
        textinfo='label+percent'
    )])

    fig.update_layout(
        title='Win Probability Estimate',
    )

    fig.show()

def get_ppg(stats):
    total_yards = get_stat(stats, "totalYards")
    games = get_stat(stats, "games")
    return round((total_yards / games) / 10, 1) if games > 0 else 0.0

def get_ppg_allowed(stats):
    allowed_yards = get_stat(stats, "totalYardsOpponent")
    games = get_stat(stats, "games")
    return round((allowed_yards / games) / 10, 1) if games > 0 else 0.0

def get_stat(stat_list, stat_name):
    for stat in stat_list:
        if stat.get("statName") == stat_name:
            return float(stat.get("statValue", 0.0))
    return 0.0


