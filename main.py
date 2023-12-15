from dash import Dash, html
from navigator_dashboard import NavigatorDashBoard

def main():
    navigator_dashboard = NavigatorDashBoard()
    app = navigator_dashboard.createDashApplication()

    app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
