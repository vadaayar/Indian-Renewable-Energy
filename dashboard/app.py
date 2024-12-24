from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Dash app
app = Dash(__name__)

# Placeholder data (you can replace it with real data later)
data_overview = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Installed Capacity (GW)": [75, 90, 100, 115, 135],
    "Renewable Share (%)": [20, 25, 30, 35, 40],
    "Carbon Reduction (MT)": [50, 60, 70, 85, 95],
    "Hydro Capacity (GW)": [30, 32, 33, 35, 37],
    "Solar Capacity (GW)": [20, 30, 40, 50, 60],
    "Wind Capacity (GW)": [25, 28, 27, 30, 33],
})

state_data = pd.DataFrame({
    "State": ["Tamil Nadu", "Karnataka", "Rajasthan", "Gujarat", "Maharashtra"],
    "Installed Capacity (GW)": [12.5, 11.8, 10.2, 9.5, 8.7],
    "Solar Contribution (%)": [60, 55, 70, 65, 50],
    "Wind Contribution (%)": [40, 45, 30, 35, 50],
    "Potential Capacity (GW)": [20, 18, 25, 22, 15],
})

global_comparison = pd.DataFrame({
    "Region": ["India", "China", "USA", "EU", "Rest of World"],
    "Installed Capacity (GW)": [135, 1060, 900, 650, 1500],
    "Share of Global (%)": [8, 50, 30, 25, 87],
})

future_targets = pd.DataFrame({
    "Year": [2025, 2030, 2035, 2040],
    "Projected Capacity (GW)": [175, 250, 350, 500],
    "Solar Target (GW)": [80, 120, 180, 250],
    "Wind Target (GW)": [50, 80, 110, 150],
})

policy_data = pd.DataFrame({
    "Policy": ["National Solar Mission", "Wind Power Initiative", "Green Energy Corridor", "Offshore Wind Policy"],
    "Year Launched": [2010, 2005, 2013, 2015],
    "Key Goal": [
        "100 GW of solar capacity by 2022.",
        "Develop wind capacity in high-potential zones.",
        "Strengthen transmission for renewable energy.",
        "Develop offshore wind farms with 5 GW capacity."
    ],
})

heatmap_data = pd.DataFrame({
    "State": ["Tamil Nadu", "Karnataka", "Rajasthan", "Gujarat", "Maharashtra"],
    "Solar Potential (GW)": [20, 18, 25, 22, 15],
    "Wind Potential (GW)": [15, 12, 10, 8, 10],
}).set_index("State")

# Visualizations
fig1 = px.bar(data_overview, x="Year", y="Installed Capacity (GW)", title="Installed Capacity Over the Years")
fig2 = px.line(data_overview, x="Year", y="Renewable Share (%)", title="Renewable Share in Energy Mix")
fig3 = px.bar(data_overview, x="Year", y=["Hydro Capacity (GW)", "Solar Capacity (GW)", "Wind Capacity (GW)"],
              title="Source-Wise Capacity Growth", barmode="stack")
fig4 = px.pie(data_overview, names="Year", values="Carbon Reduction (MT)", title="Carbon Reduction by Year")
fig5 = px.bar(state_data, x="State", y=["Solar Contribution (%)", "Wind Contribution (%)"],
              title="State-Wise Renewable Contributions", barmode="group")
fig6 = px.imshow(heatmap_data, title="State-Wise Renewable Potential Heatmap")
fig7 = px.bar(global_comparison, x="Region", y="Installed Capacity (GW)", title="Global Renewable Capacity Comparison")
fig8 = px.line(future_targets, x="Year", y="Projected Capacity (GW)", title="Future Renewable Energy Targets")
fig9 = px.bar(policy_data, x="Policy", y="Year Launched", title="Major Renewable Energy Policies")

# Stacked Area Chart
fig10 = go.Figure()
fig10.add_trace(go.Scatter(
    x=data_overview["Year"],
    y=data_overview["Solar Capacity (GW)"],
    mode='lines',
    name='Solar Capacity',
    stackgroup='one'
))
fig10.add_trace(go.Scatter(
    x=data_overview["Year"],
    y=data_overview["Wind Capacity (GW)"],
    mode='lines',
    name='Wind Capacity',
    stackgroup='one'
))
fig10.add_trace(go.Scatter(
    x=data_overview["Year"],
    y=data_overview["Hydro Capacity (GW)"],
    mode='lines',
    name='Hydro Capacity',
    stackgroup='one'
))
fig10.update_layout(
    title="Source-Wise Renewable Energy Mix Over Time",
    xaxis_title="Year",
    yaxis_title="Installed Capacity (GW)",
    showlegend=True
)

# App Layout
app.layout = html.Div([
    html.H1("Comprehensive Renewable Energy Dashboard", style={"textAlign": "center", "marginBottom": "40px"}),

    html.Div([
        html.H2("Introduction"),
        html.P(
            "India is leading the charge towards renewable energy with ambitious goals and significant progress. "
            "This dashboard provides a comprehensive view of India's renewable energy journey, including installed capacity, "
            "state-wise contributions, global comparisons, carbon reduction impacts, and future targets."
        ),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Installed Capacity Over Time"),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Source-Wise Capacity Growth"),
        dcc.Graph(figure=fig3),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("State-Wise Renewable Energy Contributions"),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Global Renewable Energy Comparison"),
        dcc.Graph(figure=fig7),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Future Renewable Energy Targets"),
        dcc.Graph(figure=fig8),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Key Renewable Energy Policies"),
        dcc.Graph(figure=fig9),
    ], style={"marginBottom": "40px"}),

    html.Div([
        html.H2("Source-Wise Renewable Energy Mix"),
        dcc.Graph(figure=fig10),
    ], style={"marginBottom": "40px"}),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)






















