import pandas as pd
import folium
import numpy as np
from branca.colormap import LinearColormap
from dash import Dash, html

class Carte:
    def __init__(self):
        self.df = pd.read_csv('data/data_covid19.csv', delimiter=';')
        self.df = self.df.dropna()

        self.centre_lat, self.centre_lon = 46.6031, 1.8883
        self.map_bounds = [[41, -5], [51, 9]]

        self.min_decès = self.df['Total Décès'].min()
        self.max_decès = self.df['Total Décès'].max()

        self.colormap = LinearColormap(colors=['orange', 'darkorange', 'red'],
                                       index=[self.min_decès, (self.min_decès + self.max_decès) / 2, self.max_decès],
                                       vmin=self.min_decès, vmax=self.max_decès)

        self.m = folium.Map(location=[self.centre_lat, self.centre_lon], zoom_start=6,
                            max_bounds=True, min_zoom=6, max_zoom=10, bounds=self.map_bounds)

        self.add_markers()

    def add_markers(self):
        for index, row in self.df.iterrows():
            radius = np.log1p(row['Total Décès']) * 1.5
            radius = max(radius, 3)
            radius = min(radius, 10)

            color = self.colormap(row['Total Décès'])

            folium.CircleMarker(
                location=[float(coord) for coord in row['geo_point_2d'].split(', ')],
                radius=radius,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=row['Nom département'] + '<br>Total Décès: ' + str(row['Total Décès'])
            ).add_to(self.m)

    def get_map(self):
        return self.m


# Crée l'application Dash
app = Dash(__name__)

# Crée une instance de la classe Carte
ma_carte = Carte()

# Mise en page de l'application avec une largeur fixe de 40%
app.layout = html.Div([
    html.H4(children='Carte des décès par département'),
    # dcc.Graph pour afficher la carte
    html.Iframe(srcDoc=ma_carte.get_map().get_root().render(), width='40%', height='600px')
])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
