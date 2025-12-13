import plotly.graph_objects as go
import networkx as nx
import numpy as np

# Create a small graph
G = nx.Graph()
nodes = ["Earth", "Human", "United States", "Science", "History", "Geography"]
G.add_nodes_from(nodes)
edges = [
    ("Earth", "Geography"),
    ("Human", "Science"),
    ("United States", "Geography"),
    ("United States", "History"),
    ("Science", "History"),
]
G.add_edges_from(edges)

# Positions
pos = nx.spring_layout(G)

# Node sizes based on degree (versatility)
node_sizes = [G.degree(n) * 20 for n in G.nodes()]

# Edge colors
edge_colors = ["blue" if "Science" in e else "red" for e in G.edges()]

# Create edges
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y, line=dict(width=2, color="gray"), hoverinfo="none", mode="lines"
)

# Create nodes
node_x = [pos[n][0] for n in G.nodes()]
node_y = [pos[n][1] for n in G.nodes()]

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=list(G.nodes()),
    textposition="top center",
    marker=dict(size=node_sizes, color="lightblue", line_width=2),
    hovertemplate="Node: %{text}<br>Connections: %{marker.size}",
)

fig = go.Figure(data=[edge_trace, node_trace])

fig.update_layout(
    title="Versatility Network",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
)

fig.write_html('./_plots/versatility_plot.html', include_plotlyjs='cdn')
