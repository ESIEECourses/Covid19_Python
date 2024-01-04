from dash import Dash, html, dcc
from map import Map
from histogram import Histogram

class DashBoard:
    """
    Cette classe représente le tableau de bord pour visualiser les différentes données sur le Covid-19

    Attributs :
        carte = Instance de la classe Map qui permet l'affichage de la carte à droite
        histogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme de gauche sur les doses n°1
        histogram2 = Instance de la classe Histogram2 qui permet l'affichage de l'histogramme de droite sur les dose n°2
    """
    def __init__(self):
        """
        Initialisation du Dashboard en implémentant une carte et les deux histogrammes
        """
        self.carte = Map()
        self.histogram = Histogram(False)
        self.histogram2 = Histogram(True)

    def createDashApplication(self):
        """
        Création de l'application Dash pour afficher les données du Covid-19

        Retourne:
            Dash : Object qui représente l'application Dashboard
        """
        self.app = Dash(__name__)

        self.app.layout = html.Div(
            id='app-container',
            children=[
                html.Nav(
                    className='navbar',
                    children=[
                        html.Nav(
                            className='navbar',
                            children=[
                                html.Div(
                                    className='navbar-container',
                                    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center',
                                           'color': 'white'},
                                    children=[
                                        html.H2(children='DashBoard Covid-19', style={'text-align': 'center'}),
                                    ]
                                )
                            ]
                        ),
                        html.Br(),
                        html.Div(
                            style={'display': 'flex'},
                            children=[
                                html.Img(
                                    src='https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20210920061756/ri/1000/picture/2021/9/History-of-Covid-Infographic.gif',
                                    style={'height': '615px', 'width': '30%', 'margin-left':'5%'}
                                ),
                                html.Iframe(srcDoc=self.carte.get_map().get_root().render(), height='600px')
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div(
                    style={'display': 'flex', 'flexDirection': 'row'},
                    children=[
                        html.Div(
                            style={'height':'25%', 'width': '90%', 'margin-left': '5%', 'border': '5px solid gray'},
                            children=[
                                dcc.Graph(figure=self.histogram.get_dash())
                            ]
                        ),
                        html.Div(
                            style={'height':'25%', 'width': '90%', 'margin-right': '5%', 'margin-left':'2%', 'border': '5px solid gray'},
                            children=[
                                dcc.Graph(figure=self.histogram2.get_dash())
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Br(),
                html.Br(),
            ],
            style={'backgroundColor': '#0d0d26'},  # Ajout d'un fond pour la démo
        )

        # Charge le fichier CSS
        self.app.css.append_css({'external_url': '/assets/styles.css'})

        return self.app
