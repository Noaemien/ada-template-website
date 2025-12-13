import plotly.graph_objects as go

# Hypothetical data for top 10 pages
pages = [
    "United States",
    "World War II",
    "Earth",
    "Human",
    "France",
    "Germany",
    "London",
    "Paris",
    "Science",
    "History",
]
visits = [150, 120, 100, 90, 80, 70, 60, 50, 40, 30]

fig = go.Figure(data=go.Bar(x=pages, y=visits, marker_color="blue"))

fig.update_layout(
    title="Popularity: Most Visited Pages",
    xaxis_title="Pages",
    yaxis_title="Visit Counts",
    xaxis_tickangle=-45,
)

# Add hover
fig.update_traces(hovertemplate="Page: %{x}<br>Visits: %{y}")

fig.write_html('./_plots/popularity_plot.html', include_plotlyjs='cdn')
