from dash import Dash, html, dcc
from carte import Carte
from Graphe import Graphe

class NavigatorDashBoard:

    def __init__(self):
        self.carte = Carte()
        self.graphe = Graphe()

    def createDashApplication(self):
        self.app = Dash(__name__)

        self.app.layout = html.Div(
            id='app-container',
            children=[
                html.H2(children='DashBoard Covid-19', style={'textAlign': 'center', 'color': 'white'}),
                html.Br(),
                html.H4(children='Représentation géographique du total de décès par département en France', style={'font-size': '24px', 'textAlign': 'center', 'color': 'white'}),
                html.Iframe(srcDoc=self.carte.get_map().get_root().render(), width='40%', height='600px' ),
                html.Br(),
                html.Br(),
                html.Br(),
                dcc.Graph(figure=self.graphe.get_dash())
            ],
            style={'height': '100vh', 'backgroundColor': '#0d0d26'},
        )

        # Charge le fichier CSS
        self.app.css.append_css({'external_url': '/assets/styles.css'})

        return self.app
