import pandas as pd
import plotly.express as px

class Histogram:
    """
    Cette classe représente un histogramme qui affiche les données des doses n°1 du Covid-19 en fonction des âges

    Attributs :
        isSecondDash (bool) : Indique la deuxième partie du dashboard ( partie des graphes )
        data : Contient les données des doses n°1 du Covid-19
        filtered_data : Filtrage des données
        columnFilter (str) : Nom de la colonne dans la date filtrée
        forDisplayY (str) : Axe des ordonnées dans le graphique
        forDisplayX (str) : Axe des abscises dans le graphique
        colorDash (str) : Couleur des barres dans le graphique

    Méthodes :
        __init__(self, isSecondDash) : Initialise l'objet Histogramme
        get_dash(self) : Renvoie l'objet graphique
    """
    def __init__(self, isSecondDash):
        self.isSecondDash = isSecondDash

        self.data = pd.read_csv('data/covid19_doses.csv', delimiter=';')
        self.data = self.data.dropna()

        self.filtered_data = self.data[self.data['Valeur de la variable'] != 0]

        if not isSecondDash:
            self.columnFilter = 'Nombre cumulé de doses n°1'
            self.forDisplayY = "Pourcentage de doses n°1"
            self.forDisplayX = "Pourcentage de doses n°1 par tranche d'âges"
            self.colorDash = "blue"

        else:
            self.columnFilter = 'Nombre cumulé de vaccinations complètes (doses n°2)'
            self.forDisplayY = "Pourcentage de doses n°2"
            self.forDisplayX = "Pourcentage de doses n°2 par tranche d'âges"
            self.colorDash = "red"

        self.grouped_data = self.filtered_data.groupby((self.filtered_data['Valeur de la variable'] // 10) * 10)[self.columnFilter].sum().reset_index()

        self.total_doses = self.grouped_data[self.columnFilter].sum()
        self.grouped_data['Pourcentage'] = (self.grouped_data[self.columnFilter] / self.total_doses) * 100

        # Intervalles pour chaque tranche
        self.grouped_data['Intervalles'] = self.grouped_data['Valeur de la variable'].astype(str) + '-' + (self.grouped_data['Valeur de la variable'] + 9).astype(str)
        # Arrondir le pourcentage
        self.grouped_data['Pourcentage'] = self.grouped_data['Pourcentage'].round(2)

        self.fig = px.bar(self.grouped_data, x='Intervalles', y='Pourcentage',
                          labels={"Pourcentage": self.forDisplayY, "Intervalles": "Tranches d'âges"},
                          title=self.forDisplayX,
                            color = 'Intervalles',  # Utilisation du paramètre 'color' pour spécifier la couleur par barre
                            color_discrete_sequence = [self.colorDash]  # Changer la couleur des barres ici
                          )

        self.fig.update_traces(texttemplate='%{y:f}%', textposition='outside')

        self.fig.update_layout(
            margin=dict(l=50, r=20, t=50, b=50),  # Ajuste les marges
        )

    def get_dash(self):
        return self.fig
