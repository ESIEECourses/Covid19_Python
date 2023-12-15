from dash import Dash, html
from carte import Carte

class NavigatorDashBoard:

    def __init__(self):
        self.carte = Carte()

    def createDashApplication(self):
        self.app = Dash(__name__)

        self.app.layout = html.Div([
            html.H4(children='DashBoard COVID-19'),
            # dcc.Graph to display the Carte
            html.Iframe(srcDoc=self.carte.get_map().get_root().render(), width='40%', height='600px')
        ])

        return self.app


