from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from base64 import b64encode
from species_info import species_info 

# Create the graph
G = nx.DiGraph()
edges = [
    ("Crown Hominoidea", "Hominidae"),
    ("Hominidae", "Intermediate1"),
    ("Intermediate1", "Intermediate2"),
    ("Intermediate2", "Homo"),
    ("Homo", "Homo sp. (Denisovan)"),
    ("Homo", "Intermediate3"),
    ("Intermediate3", "Homo neanderthalensis"),
    ("Intermediate3", "Homo sapiens"),
    ("Intermediate2", "Pan"),
    ("Pan", "Pan paniscus"),
    ("Pan", "Pan troglodytes"),
    ("Intermediate1", "Gorilla gorilla"),
    ("Hominidae", "Pongo"),
    ("Pongo", "Pongo abelii"),
    ("Pongo", "Pongo pygmaeus"),
    ("Crown Hominoidea", "Hylobatidae"),
    ("Hylobatidae", "Intermediate4"),
    ("Intermediate4", "Intermediate5"),
    ("Intermediate5", "Intermediate6"),
    ("Intermediate6", "Hylobates agilis"),
    ("Intermediate6", "Hylobates lar"),
    ("Intermediate5", "Hylobates pileatus"),
    ("Intermediate4", "Symphalangus syndactylus"),
    ("Hylobatidae", "Nomascus siki")
]
G.add_edges_from(edges)

# Node positions
pos = {
    "Crown Hominoidea": (0, 0),
    "Hominidae": (1, 2),
    "Intermediate1": (2, 3.5),
    "Intermediate2": (3, 4),
    "Homo": (4, 5),
    "Intermediate3": (5, 5.3),
    "Homo sp. (Denisovan)": (6, 4.6),
    "Homo neanderthalensis": (6, 5.1),
    "Homo sapiens": (6, 5.5),
    "Pan": (4, 3.5),
    "Pan paniscus": (6, 4),
    "Pan troglodytes": (6, 3),
    "Gorilla gorilla": (6, 2.25),
    "Pongo": (2, 1),
    "Pongo abelii": (6, 1.5),
    "Pongo pygmaeus": (6, 0.5),
    "Hylobatidae": (1, -0.6),
    "Intermediate4": (2, -1.2),
    "Intermediate5": (3, -0.8),
    "Intermediate6": (4, -0.6),
    "Hylobates agilis": (6, -0.2),
    "Hylobates lar": (6, -1.1),
    "Hylobates pileatus": (6, -1.5),
    "Symphalangus syndactylus": (6, -2.5),
    "Nomascus siki": (6, -3)
}
divergence_times = {
    "Crown Hominoidea": 22.32, 
    "Hominidae": 17.29,
    "Intermediate1": 10.63,
    "Intermediate2": 7.65,
    "Homo": 1.39,
    "Intermediate3": 0.68,
    "Homo sp. (Denisovan)": 0,
    "Homo neanderthalensis": 0,
    "Homo sapiens": 0,
    "Pan": 2.98,
    "Pan paniscus": 0,
    "Pan troglodytes": 0,
    "Gorilla gorilla": 0,
    "Pongo": 4.2,
    "Pongo abelii": 0,
    "Pongo pygmaeus": 0,
    "Hylobatidae": 18.0,
    "Intermediate4": 7.42,
    "Intermediate5": 4.06,
    "Intermediate6": 3.14,
    "Hylobates agilis": 0,
    "Hylobates lar": 0,
    "Hylobates pileatus": 0,
    "Symphalangus syndactylus": 0,
    "Nomascus siki": 0
}
pos = {node: (divergence_times[node], y) for node, (_, y) in pos.items()}
# Create edge coordinates
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

for node in G.nodes():
    if node not in species_info and node in divergence_times:
        species_info[node] = {
            "divergence_date": divergence_times[node],
            "is_internal": True
        }

node_x = []
node_y = []
node_text = []
node_sizes = []
node_colors = []
node_symbols = []

# List of internal nodes
internal_nodes = [
    "Hominidae", "Intermediate1", "Intermediate2", 
    "Homo", "Intermediate3", "Pan", "Pongo", "Hylobatidae", 
    "Intermediate4", "Intermediate5", "Intermediate6"
]

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node if node not in internal_nodes else "")
    node_sizes.append(15)  
    node_colors.append('#2E86C1')  
    node_symbols.append('circle')  

fig = go.Figure()

# Update the node trace
fig.add_trace(
    go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            symbol=node_symbols,
            line=dict(width=1, color='rgb(250, 250, 250)'),
        ),
        text=node_text,
        textposition="middle right",
        hovertemplate='<br>Click for more information<extra></extra>',
        customdata=list(G.nodes()),
    )
)

for time in range(0, 26, 5):  
    fig.add_shape(
        type="line",
        x0=time,
        x1=time,
        y0=-3.5,
        y1=6.5,
        line=dict(
            color="rgb(200, 200, 200)",
            width=1,
            dash="dash",
        )
    )

# Add edges
fig.add_trace(
    go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=1.5, color='rgb(50, 50, 50)'),
        hoverinfo='none'
    )
)


fig.update_layout(
    title="",
    showlegend=False,
    hovermode='closest',
    margin=dict(b=40, l=5, r=5, t=40),
    width=800,
    height=800,
    plot_bgcolor='white',
    xaxis=dict(
        title="Millions of Years Ago",
        showgrid=False,
        zeroline=False,
        range=[25, -8],  # Reverse axis to show older times on left
        tickmode='array',
        ticktext=[str(i) for i in range(25, -1, -5)],
        tickvals=list(range(25, -1, -5)),
        tickangle=0,
        showline=True,
        linewidth=1,
        linecolor='black',
    )
)

fig.update_yaxes(
    showgrid=False, 
    zeroline=False, 
    showticklabels=False,
    range=[-3.5, 6.5]
)


# Create Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Hominoidea Phylogenetic Tree", 
            style={'textAlign': 'center', 'color': '#333', 'padding': '20px'}),
    
    html.Div([
        html.P([
            html.Span("• ", style={'color': '#2E86C1', 'fontSize': '20px'}),
            "Click on any node to view information. Internal nodes show divergence dates, leaf nodes show species details."
        ])
    ], style={
        'backgroundColor': '#f8f9fa',
        'padding': '15px',
        'borderRadius': '5px',
        'marginBottom': '20px',
        'width': '80%',
        'margin': '0 auto'
    }),
    
    # Content wrapper
    html.Div(style={
        'display': 'block',
        'width': '90%',
        'maxWidth': '1200px',
        'margin': '0 auto',
        'position': 'relative'
    }, children=[
        # Graph container
        html.Div([
            dcc.Graph(
                id='phylogenetic-tree',
                figure=fig,
                style={'height': '800px', 'width': '100%'},
                # config={'displayModeBar': False}
            )
        ], style={
            'width': '65%',
            'display': 'inline-block',
            'verticalAlign': 'top'
        }),
        
        # Info panel container
        html.Div([
            html.Div(
                id='click-data',
                children=[
                    html.H3("Node Information", style={'color': '#666'}),
                    html.P("Click on any node to view information.")
                ],
                style={
                    'padding': '20px',
                    'backgroundColor': 'white',
                    'borderRadius': '5px',
                    'border': '1px solid #ddd',
                    'minHeight': '400px'
                }
            )
        ], style={
            'width': '30%',
            'display': 'inline-block',
            'verticalAlign': 'top',
            'marginLeft': '4%'
        })
    ]),
    
    # Sources section
    html.Div([
        html.H3("Sources", 
                style={
                    'color': '#333',
                    'borderBottom': '2px solid #2E86C1',
                    'paddingBottom': '10px',
                    'marginBottom': '15px'
                }),
        html.Div([
            html.P([
                "Pozzi, Luca, James A. Hodgson, Andrew S. Burrell, Kirstin N. Sterner, Ryan L. Raaum, and Todd R. Disotell. ",
                html.Em("\"Primate Phylogenetic Relationships and Divergence Dates Inferred from Complete Mitochondrial Genomes.\" "),
                "Molecular Phylogenetics and Evolution 75 (2014): 165-83."
            ], style={
                'marginBottom': '10px',
                'lineHeight': '1.6',
                'fontSize': '0.9em'
            }),
            html.P([
                "Encyclopedia Britannica."
            ], style={
                'marginBottom': '10px',
                'lineHeight': '1.6',
                'fontSize': '0.9em'
            })
        ], style={
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '5px',
            'border': '1px solid #ddd',
            'marginTop': '20px'
        })
    ], style={
        'width': '90%',
        'maxWidth': '1200px',
        'margin': '40px auto 20px auto',
        'clear': 'both'
    })
], style={
    'backgroundColor': '#f9f9f9',
    'fontFamily': 'Arial, sans-serif',
    'padding': '20px',
    'width': '100%'
})

# Callback for updating info panel
@app.callback(
    Output('click-data', 'children'),
    Input('phylogenetic-tree', 'clickData')
)
def display_click_data(clickData):
    if not clickData:
        return [
            html.H3("Node Information", style={'color': '#666'}),
            html.P("Click on any node to view information.")
        ]
    
    point = clickData['points'][0]
    node_name = point['customdata'] 
    info = species_info.get(node_name, {})

    
    if info.get('is_internal', False):
        return [
            html.H3("Common Ancestor", style={'color': '#333', 'marginBottom': '20px'}),
            html.Div([
                html.P([
                    html.Strong("Divergence Date: "), 
                    html.Span(f"{info['divergence_date']:.2f} million years ago")
                ], style={'marginBottom': '10px'}),
                html.P([
                    html.Strong("Description: "), 
                    html.Span("This is an internal node representing a common ancestor of the descendant species.")
                ], style={'marginBottom': '10px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '15px',
                'borderRadius': '5px'
            })
        ]
    elif info:
        return [
            html.H3(node_name, style={'color': '#333', 'marginBottom': '20px'}),
            html.Div([
                html.Img(
                    src=info.get('image_url', ''),
                    style={
                        'width': '100%',
                        'maxHeight': '200px',
                        'objectFit': 'contain',
                        'marginBottom': '20px',
                        'borderRadius': '5px'
                    }
                ) if info.get('image_url') else None
            ]),
            html.Div([
                html.P([
                    html.Strong("Common name: "), 
                    html.Span(info.get('common_name', 'N/A'))
                ], style={'marginBottom': '10px'}),
                html.P([
                    html.Strong("Distribution: "), 
                    html.Span(info.get('distribution', 'N/A'))
                ], style={'marginBottom': '10px'}),
                html.P([
                    html.Strong("Description: "), 
                    html.Span(info.get('description', 'N/A'))
                ], style={'marginBottom': '10px'}),
                html.P([
                    html.Strong("Key features: "), 
                    html.Span(info.get('features', 'N/A'))
                ], style={'marginBottom': '10px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '15px',
                'borderRadius': '5px'
            })
        ]
    
    return [
        html.H3("No Information Available", style={'color': '#666'}),
        html.P(f"No information available for {node_name}")
    ]


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
