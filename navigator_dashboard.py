from dash import Dash, html
from carte import Carte

class NavigatorDashBoard:

    def __init__(self):
        self.carte = Carte()

    def createDashApplication(self):
        self.app = Dash(__name__)

        self.app.layout = html.Div(
            id='app-container',
            children=[
                html.H2(children='DashBoard Covid-19', style={'textAlign': 'center', 'color': 'white'}),
                html.Br(),
                html.H4(children='Représentation géographique du total de décès par départementen France', style={'textAlign': 'center', 'color': 'white'}),
                # dcc.Graph to display the Carte
                html.Iframe(srcDoc=self.carte.get_map().get_root().render(), width='40%', height='600px')
            ],
            style={'height': '100vh'},  # Darker Blue color
        )

        # Charge le fichier CSS
        self.app.css.append_css({'external_url': '/assets/styles.css'})

        return self.app
