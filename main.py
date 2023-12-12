from dash import Dash, html
import pandas as pd

# Lire le fichier CSV avec le délimiteur ';'
df = pd.read_csv('data/data_covid19.csv', delimiter=';')


# Créer une fonction pour générer le tableau HTML
def generate_table(dataframe):
    table_rows = []

    # Créer la première ligne avec les noms de colonne
    header_row = [html.Th('Columns')] + [html.Th(col) for col in dataframe.columns]
    table_rows.append(html.Tr(header_row))

    # Créer les lignes avec les valeurs
    for i in range(
            min(10, len(dataframe))):  # Afficher les 10 premières lignes ou moins si la dataframe est plus petite
        row_data = [html.Th('Row ' + str(i + 1))] + [html.Td(data) for data in dataframe.iloc[i]]
        table_rows.append(html.Tr(row_data))

    return html.Table([
        html.Thead(table_rows[0]),  # Utiliser la première ligne comme en-tête
        html.Tbody(table_rows[1:])  # Utiliser le reste comme corps
    ])


# Créer l'application Dash
app = Dash(__name__)

# Définir la mise en page de l'application
app.layout = html.Div([
    html.H4(children='Les 10 premières lignes de chaque colonne'),
    generate_table(df)
])

# Exécuter l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
