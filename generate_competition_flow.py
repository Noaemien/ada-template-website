import plotly.graph_objects as go

# Nodes
nodes = [
    "6000 Entries",
    "Qualifiers (64)",
    "Group Stage",
    "Repechage",
    "Round of 16",
    "Quarter-Finals",
    "Semi-Finals",
    "Final",
    "Winner",
]

node_indices = {node: i for i, node in enumerate(nodes)}

# Links
links = [
    {
        "source": node_indices["6000 Entries"],
        "target": node_indices["Qualifiers (64)"],
        "value": 64,
    },
    {
        "source": node_indices["Qualifiers (64)"],
        "target": node_indices["Group Stage"],
        "value": 64,
    },
    {
        "source": node_indices["Group Stage"],
        "target": node_indices["Round of 16"],
        "value": 8,
    },  # 8 groups, 1 each
    {
        "source": node_indices["Group Stage"],
        "target": node_indices["Repechage"],
        "value": 24,
    },  # 8 groups * 3 = 24
    {
        "source": node_indices["Repechage"],
        "target": node_indices["Round of 16"],
        "value": 8,
    },  # 8 winners
    {
        "source": node_indices["Round of 16"],
        "target": node_indices["Quarter-Finals"],
        "value": 8,
    },
    {
        "source": node_indices["Quarter-Finals"],
        "target": node_indices["Semi-Finals"],
        "value": 4,
    },
    {
        "source": node_indices["Semi-Finals"],
        "target": node_indices["Final"],
        "value": 2,
    },
    {"source": node_indices["Final"], "target": node_indices["Winner"], "value": 1},
]

fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15, thickness=20, line=dict(color="black", width=0.5), label=nodes
            ),
            link=dict(
                source=[link["source"] for link in links],
                target=[link["target"] for link in links],
                value=[link["value"] for link in links],
            ),
        )
    ]
)

fig.update_layout(title_text="Tournament Flow", font_size=10)

fig.write_html('./_plots/competition_flow.html', include_plotlyjs='cdn')
