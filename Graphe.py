import pandas as pd
import plotly.express as px

class Graphe:
    def __init__(self):
        self.data = pd.read_csv('data/Covid.csv', delimiter=';')
        self.data = self.data.dropna()

        self.filtered_data = self.data[self.data['Valeur de la variable'] != 0]

        self.grouped_data = self.filtered_data.groupby((self.filtered_data['Valeur de la variable'] // 10) * 10)['Nombre cumulé de doses n°1'].sum().reset_index()

        self.total_doses = self.grouped_data['Nombre cumulé de doses n°1'].sum()
        self.grouped_data['Pourcentage'] = (self.grouped_data['Nombre cumulé de doses n°1'] / self.total_doses) * 100

        # Intervalles pour chaque tranche
        self.grouped_data['Intervalles'] = self.grouped_data['Valeur de la variable'].astype(str) + '-' + (self.grouped_data['Valeur de la variable'] + 9).astype(str)
        # Arrondir le pourcentage
        self.grouped_data['Pourcentage'] = self.grouped_data['Pourcentage'].round(2)

        self.fig = px.bar(self.grouped_data, x='Intervalles', y='Pourcentage',
                     labels={"Pourcentage": "Pourcentage de doses n°1 ", "Intervalles": "Tranches d'âges "},
                     title="Pourcentage de doses n°1 par tranche d'âges")

        self.fig.update_traces(texttemplate='%{y:f}%', textposition='outside')


    def get_dash(self):
        return self.fig
