from dash import Dash, html
from carte import Carte
from navigator_dashboard import NavigatorDashBoard

def main():
    carte = Carte()
    navigator_dashboard = NavigatorDashBoard(carte)

    navigator_dashboard.createDashApplication()
    navigator_dashboard.app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
