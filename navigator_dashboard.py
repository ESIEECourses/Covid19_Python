from dash import Dash, html

class NavigatorDashBoard:

    def __init__(self, carte):
        self.carte = carte

    def createDashApplication(self):
        self.app = Dash(__name__)

        self.app.layout = html.Div([
            html.H4(children='Carte des décès par département'),
            # dcc.Graph to display the Carte
            html.Iframe(srcDoc=self.carte.get_map().get_root().render(), width='40%', height='600px')
        ])


