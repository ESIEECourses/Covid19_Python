from dash import Dash, html, dcc
from carte import Carte
from Graphe import Graphe
from Graphe2 import Graphe2  # Importez votre classe Graphe2

class NavigatorDashBoard:
    def __init__(self):
        self.carte = Carte()
        self.graphe = Graphe()
        self.graphe2 = Graphe2()

    def createDashApplication(self):
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
                                        #html.Img(
                                        #    src='https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F20b888aa-395d-4188-8a72-e06cc211f5de_498x278.gif',
                                        #    style={'height': '100px', 'width': '150px'}
                                        #)
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
                                dcc.Graph(figure=self.graphe.get_dash())
                            ]
                        ),
                        html.Div(
                            style={'height':'25%', 'width': '90%', 'margin-right': '5%', 'margin-left':'2%', 'border': '5px solid gray'},
                            children=[
                                dcc.Graph(figure=self.graphe2.get_dash2())
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
