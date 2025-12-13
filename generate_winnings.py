import plotly.graph_objects as go

groups = ["Bookmakers", "Gamblers"]
winnings = [15000, 12000]  # Hypothetical

fig = go.Figure(data=go.Bar(x=groups, y=winnings, marker_color=["blue", "red"]))

fig.update_layout(
    title="Winnings Comparison",
    xaxis_title="Group",
    yaxis_title="Amount Won ($)",
    hovermode="x",
)

# Add hover
fig.update_traces(hovertemplate="Group: %{x}<br>Won: $%{y}")

fig.write_html('./_plots/winnings_plot.html', include_plotlyjs='cdn')
