import pandas as pd
import plotly.express as px

class Graphe2:
    def __init__(self):
        self.data = pd.read_csv('data/Covid.csv', delimiter=';')
        self.data = self.data.dropna()

        self.filtered_data = self.data[self.data['Valeur de la variable'] != 0]

        self.grouped_data = self.filtered_data.groupby((self.filtered_data['Valeur de la variable'] // 10) * 10)['Nombre cumulé de vaccinations complètes (doses n°2)'].sum().reset_index()

        self.total_doses = self.grouped_data['Nombre cumulé de vaccinations complètes (doses n°2)'].sum()
        self.grouped_data['Pourcentage'] = (self.grouped_data['Nombre cumulé de vaccinations complètes (doses n°2)'] / self.total_doses) * 100

        # Intervalles pour chaque tranche
        self.grouped_data['Intervalles'] = self.grouped_data['Valeur de la variable'].astype(str) + '-' + (self.grouped_data['Valeur de la variable'] + 9).astype(str)
        # Arrondir le pourcentage
        self.grouped_data['Pourcentage'] = self.grouped_data['Pourcentage'].round(2)

        # Changer la couleur des barres (par exemple, en rouge)
        self.fig = px.bar(self.grouped_data, x='Intervalles', y='Pourcentage',
                          labels={"Pourcentage": "Pourcentage de doses n°2", "Intervalles": "Tranches d'âges"},
                          title="Pourcentage de doses n°2 par tranche d'âges",
                          color='Intervalles',  # Utilisation du paramètre 'color' pour spécifier la couleur par barre
                          color_discrete_sequence=['red']  # Changer la couleur des barres ici
                          )

        self.fig.update_traces(texttemplate='%{y:f}%', textposition='outside')

        self.fig.update_layout(
            margin=dict(l=50, r=20, t=50, b=50),  # Ajuste les marges
        )

    def get_dash2(self):
        return self.fig
