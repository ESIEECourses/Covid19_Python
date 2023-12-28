from dash import Dash, html, dcc
from dashboard import DashBoard

class Main:
    def main(self):
        dashboard = DashBoard()
        app = dashboard.createDashApplication()

        app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
