import plotly.graph_objects as go
import numpy as np

# Hypothetical data
np.random.seed(42)
n_points = 50
efficiency_scores = np.random.uniform(0, 100, n_points)
visit_frequencies = np.random.uniform(1, 100, n_points)
page_names = [f"Page {i}" for i in range(n_points)]
# Make some high efficiency (green) and traps (red)
colors = ["green" if score > 70 else "red" for score in efficiency_scores]
# Specific examples
page_names[0] = "United States"
colors[0] = "green"
efficiency_scores[0] = 95
visit_frequencies[0] = 80
page_names[1] = "Dead End Page"
colors[1] = "red"
efficiency_scores[1] = 10
visit_frequencies[1] = 5

fig = go.Figure(
    data=go.Scatter(
        x=efficiency_scores,
        y=visit_frequencies,
        mode="markers",
        marker=dict(color=colors, size=10),
        text=page_names,
        hovertemplate="Page: %{text}<br>Efficiency: %{x}<br>Visits: %{y}",
    )
)

fig.update_layout(
    title="Efficiency Scatter Plot",
    xaxis_title="Efficiency Score",
    yaxis_title="Visit Frequency",
)

fig.write_html('./_plots/efficiency_plot.html', include_plotlyjs='cdn')
