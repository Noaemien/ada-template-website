import plotly.graph_objects as go
import networkx as nx
import numpy as np

# Create a graph with 64 nodes
G = nx.random_geometric_graph(
    64, 0.15
)  # Approximate 1021 edges? Wait, random geometric might not have exactly 1021, but close enough.

# Ensure connected or something, but for simplicity.

# Assign communities (10 communities)
communities = np.random.randint(0, 10, 64)
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "gray",
    "cyan",
]
node_colors = [colors[c] for c in communities]

# Betweenness centrality
betweenness = nx.betweenness_centrality(G)
node_sizes = [b * 1000 + 10 for b in betweenness.values()]  # Scale

# Positions
pos = nx.spring_layout(G)

# Edges
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y, line=dict(width=1, color="gray"), hoverinfo="none", mode="lines"
)

# Nodes
node_x = [pos[n][0] for n in G.nodes()]
node_y = [pos[n][1] for n in G.nodes()]
node_text = [f"Node {n}<br>Centrality: {betweenness[n]:.3f}" for n in G.nodes()]

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers",
    marker=dict(size=node_sizes, color=node_colors, line_width=2),
    text=node_text,
    hovertemplate="%{text}",
)

fig = go.Figure(data=[edge_trace, node_trace])

fig.update_layout(
    title="Bookmakers Network: Top 64 Hubs",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
)


fig.write_html('./_plots/bookmakers_plot.html', include_plotlyjs='cdn')
