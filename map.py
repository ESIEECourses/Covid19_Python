import pandas as pd
import folium
import numpy as np
from branca.colormap import LinearColormap

class Map:
    """
    Cette classe permet de créer une carte géographique qui représente les décès liées au Covid-19 par département en France

    Atibuts :
        centre_lat ( float ) : Latitude de centre de la carte
        centre_lon ( float ) : Longitude du centre de la carte
        map_bounds ( list ) : Cordonnées max de la carte
        min_decès ( int ) : Le minimum de décès dans les données
        max_decès ( int ) : Le maximum de décès dans les données
        colormap : Couleurs pour représenter le niveau de décès
    """
    def __init__(self):
        """
        Initialisation d'une carte qui représente les décès liés au Covid-19 par département en France
        """
        self.df = pd.read_csv('data/covid19_deaths.csv', delimiter=';')
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
        """
        Ajouts des marqueurs représentant les décès par département à la carte
        :return:
        """
        for index, row in self.df.iterrows():
            radius = np.log1p(row['Total Décès']) * 1.5
            radius = max(radius, 3)
            radius = min(radius, 10)

            color = self.colormap(row['Total Décès'])

            tooltip_text = f"{row['Nom département']} - Total Décès: {row['Total Décès']}"

            folium.CircleMarker(
                location=[float(coord) for coord in row['geo_point_2d'].split(', ')],
                radius=radius,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                tooltip=tooltip_text
            ).add_to(self.m)

    def get_map(self):
        """
        Retourne la carte
        """
        return self.m
