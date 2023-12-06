from dash import Dash, html
import pandas as pd

# Lire le fichier CSV avec le délimiteur ';'
df = pd.read_csv('/Users/kayanthan/PycharmProjects/Covid19_Python/data/data_covid19.csv', delimiter=';')

# Créer une fonction pour générer le tableau HTML
def generate_table(dataframe):
    table_rows = []
    for col in dataframe.columns:
        table_rows.append(
            html.Tr([
                html.Th(col),
                *[html.Td(data) for data in dataframe[col].head(10)]
                # Afficher les 10 premières valeurs de chaque colonne
            ])
        )

    return html.Table([
        html.Thead(html.Tr([html.Th('Columns')] + [html.Th('Row ' + str(i + 1)) for i in range(10)])),
        html.Tbody(table_rows)
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
