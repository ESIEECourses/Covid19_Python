import pandas as pd
import plotly.express as px

data = pd.read_csv('data/Covid.csv', delimiter=';')

# Filtrer les données où l'âge n'est pas égal à zéro
filtered_data = data[data['Valeur de la variable'] != 0]

# Regrouper les données par tranche de 10 pour l'âge
grouped_data = filtered_data.groupby((filtered_data['Valeur de la variable'] // 10) * 10)['Nombre cumulé de doses n°1'].sum().reset_index()

# Calculer le pourcentage par rapport au total
total_doses = grouped_data['Nombre cumulé de doses n°1'].sum()
grouped_data['Pourcentage'] = (grouped_data['Nombre cumulé de doses n°1'] / total_doses) * 100

# Intervalles pour chaque tranche
grouped_data['Intervalles'] = grouped_data['Valeur de la variable'].astype(str) + '-' + (grouped_data['Valeur de la variable'] + 9).astype(str)
# Arrondir le pourcentage
grouped_data['Pourcentage'] = grouped_data['Pourcentage'].round(2)

fig = px.bar(grouped_data, x='Intervalles', y='Pourcentage',
             labels={"Pourcentage": "Pourcentage de doses n°1 ", "Intervalles": "Tranches d'âges "},
             title="Pourcentage de doses n°1 par tranche d'âges")

# Affiche les pourcentages sur les barres
fig.update_traces(texttemplate='%{y:f}%', textposition='outside')

fig.show()