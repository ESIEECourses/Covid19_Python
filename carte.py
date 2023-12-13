from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/data_covid19.csv', delimiter=';')

# Supprime les lignes avec des valeurs manquantes
df = df.dropna()

# Coordonnées du centre de la France
center_lat, center_lon = 46.6031, 1.8883

# Crée une carte avec Plotly Express
fig = px.scatter_geo(df,
                     lat=df['geo_point_2d'].apply(lambda x: float(x.split(', ')[0])),
                     lon=df['geo_point_2d'].apply(lambda x: float(x.split(', ')[1])),
                     size='Total Décès',  # Utilise la taille pour représenter le nombre de décès
                     color='Total Décès',  # Utilise la couleur pour représenter le nombre de décès
                     hover_name='Nom département',  # Utilise le nom du département pour le survol
                     projection='mercator',  # Utilise la projection 'mercator'
                     height=700,  # Définir la hauteur de la carte
                     template='plotly',  # Utilise le template 'plotly'
                     center={'lat': center_lat, 'lon': center_lon},  # Centre de la carte
                     range_color=[0, df['Total Décès'].max()],  # Échelle des couleurs
                     )
fig.update_geos(
    lonaxis_range=[-5, 20],  # Limite longitudinale de la carte
    lataxis_range=[35, 51],  # Limite latitudinale de la carte
    oceancolor='blue',  # Couleur des océans
)

# Crée l'application Dash
app = Dash(__name__)

# Mise en page de l'application
app.layout = html.Div([
    html.H4(children='Carte des décès par département'),
    # dcc.Graph pour afficher la carte
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
