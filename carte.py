import pandas as pd
import folium
import numpy as np
from branca.colormap import LinearColormap
from dash import Dash, html

df = pd.read_csv('data/data_covid19.csv', delimiter=';')

# Supprime les lignes avec des valeurs manquantes
df = df.dropna()

# Coordonnées du centre de la France
centre_lat, centre_lon = 46.6031, 1.8883

# Définit les limites de la carte pour la France et ses pays voisins
map_bounds = [[41, -5], [51, 9]]  # [Latitude_min, Longitude_min], [Latitude_max, Longitude_max]

# Trouve la plage du nombre total de décès pour normaliser la taille des cercles
min_decès = df['Total Décès'].min()
max_decès = df['Total Décès'].max()

# Définit une échelle de couleurs personnalisée
colormap = LinearColormap(colors=['orange', 'darkorange', 'red'], index=[min_decès, (min_decès + max_decès) / 2, max_decès],
vmin=min_decès, vmax=max_decès)

# Crée une carte avec folium
m = folium.Map(location=[centre_lat, centre_lon], zoom_start=6, max_bounds=True, min_zoom=6, max_zoom=10, bounds=map_bounds)

# Ajoute des marqueurs pour chaque département
for index, row in df.iterrows():
    # Applique une échelle logarithmique à la taille des cercles
    radius = np.log1p(row['Total Décès']) * 1.5

    # Ajuste la plage des tailles de cercles pour éviter qu'ils ne deviennent trop grands lors du dézoom
    radius = max(radius, 3)  # Taille minimale des cercles
    radius = min(radius, 10)  # Taille maximale des cercles

    # Couleur de la colormap en fonction du nombre de décès
    color = colormap(row['Total Décès'])

    folium.CircleMarker(
        location=[row['geo_point_2d'].split(', ')[0], row['geo_point_2d'].split(', ')[1]],
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=row['Nom département'] + '<br>Total Décès: ' + str(row['Total Décès'])
    ).add_to(m)

# Crée l'application Dash
app = Dash(__name__)

# Mise en page de l'application avec une largeur fixe de 40%
app.layout = html.Div([
    html.H4(children='Carte des décès par département'),
    # dcc.Graph pour afficher la carte
    html.Iframe(srcDoc=m.get_root().render(), width='40%', height='600px')
])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
