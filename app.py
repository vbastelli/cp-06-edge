import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER_MQTT = "34.203.196.154"
BROKER_PORT = 1883
TOPICO_LUMINOSITY = "/TEF/device011/attrs/l"
TOPICO_TEMPERATURE = "/TEF/device011/attrs/t"
TOPICO_HUMIDITY = "/TEF/device011/attrs/h"
DASH_HOST = "127.0.0.1"  # Para rodar localmente

luminosity_values = []
temperature_values = []
humidity_values = []
timestamps = []

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Visualizador de Dados do Sensor'),
    dcc.Graph(id='combined-graph'),
    dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0)
])

@app.callback(
    Output('combined-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_combined_graph(n_intervals):
    fig = go.Figure()

    if timestamps:
        if luminosity_values:
            fig.add_trace(go.Scatter(
                x=timestamps,
                y=luminosity_values,
                mode='lines+markers',
                name='Luminosidade',
                line=dict(color='orange')
            ))
        if temperature_values:
            fig.add_trace(go.Scatter(
                x=timestamps,
                y=temperature_values,
                mode='lines+markers',
                name='Temperatura',
                line=dict(color='red')
            ))
        if humidity_values:
            fig.add_trace(go.Scatter(
                x=timestamps,
                y=humidity_values,
                mode='lines+markers',
                name='Umidade',
                line=dict(color='blue')
            ))

    fig.update_layout(
        title='Dados do Sensor ao Longo do Tempo',
        xaxis_title='Timestamp',
        yaxis_title='Valores do Sensor',
        hovermode='closest'
    )

    return fig

def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao Broker MQTT com código de resultado {rc}")
    client.subscribe(TOPICO_LUMINOSITY)
    client.subscribe(TOPICO_TEMPERATURE)
    client.subscribe(TOPICO_HUMIDITY)

def on_message(client, userdata, msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if msg.topic == TOPICO_LUMINOSITY:
        luminosity_values.append(float(msg.payload.decode()))
    elif msg.topic == TOPICO_TEMPERATURE:
        temperature_values.append(float(msg.payload.decode()))
    elif msg.topic == TOPICO_HUMIDITY:
        humidity_values.append(float(msg.payload.decode()))
    
    if len(timestamps) < max(len(luminosity_values), len(temperature_values), len(humidity_values)):
        timestamps.append(timestamp)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_MQTT, BROKER_PORT, 60)

if __name__ == '__main__':
    client.loop_start()  # Inicia o loop MQTT em segundo plano
    app.run_server(debug=True, host=DASH_HOST, port=8050)
