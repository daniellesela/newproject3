import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Create sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [4, 2, 7, 5]
})

# Setup the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Sample Dashboard"),
    dcc.Graph(
        id='example-bar',
        figure=px.bar(df, x="Category", y="Value", title="Bar Chart Example")
    ),
    html.P("This is a simple dashboard example using Dash and Plotly.")
])

if __name__ == "__main__":
    app.run_server(debug=True)