from dash import Dash, html
import pandas as pd

# Lit le fichier CSV avec le délimiteur ';'
df = pd.read_csv('data/data_covid19.csv', delimiter=';')

# Supprime les lignes avec des valeurs manquantes
df = df.dropna()

# Crée une fonction pour générer le tableau HTML
def generate_table(dataframe):
    table_rows = []

    # Crée la première ligne avec les noms de colonne
    header_row = [html.Th('Columns')] + [html.Th(col) for col in dataframe.columns]
    table_rows.append(html.Tr(header_row))

    # Crée les lignes avec les valeurs
    for i in range(min(2000, len(dataframe))):
        row_data = [html.Th('Row ' + str(i + 1))] + [html.Td(data) for data in dataframe.iloc[i]]
        table_rows.append(html.Tr(row_data))

    return html.Table([
        html.Thead(table_rows[0]),  # Utilise la première ligne comme en-tête
        html.Tbody(table_rows[1:])  # Utilise le reste comme corps
    ])

# Crée l'application Dash
app = Dash(__name__)

# Définit la mise en page de l'application
app.layout = html.Div([
    html.H4(children='Les 10 premières lignes de chaque colonne'),
    generate_table(df)
])

# Exécute l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
