import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import dash
import dash_core_components as dcc
import dash_html_components as html

# Carga y preparación de datos
df = pd.read_csv('input/hourly-energy-consumption/test.csv')

# Análisis de tendencias y patrones
df.plot(kind='line', x='date', y='demand')
plt.show()

# Desarrollo del modelo de predicción
X = df[['date']]
y = df['demand']
model = LinearRegression()
model.fit(X, y)

# Creación de la interfaz visual
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Demand Prediction'),
    dcc.Graph(id='demand-graph'),
    dcc.Slider(id='date-slider', min=df['date'].min(), max=df['date'].max(), value=df['date'].max())
])

@app.callback(
    dash.dependencies.Output('demand-graph', 'figure'),
    [dash.dependencies.Input('date-slider', 'value')]
)
def update_graph(date_value):
    # Actualiza la gráfica con la demanda histórica y la predicción futura
    fig = go.Figure(data=[go.Scatter(x=df['date'], y=df['demand'])])
    fig.add_trace(go.Scatter(x=[date_value], y=[model.predict([[date_value]])[0]]))
    return fig

if _name_ == '_main_':
    app.run_server()