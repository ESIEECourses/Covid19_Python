from dash import Dash, html, dcc
from navigator_dashboard import NavigatorDashBoard

class Main:
    def main(self):
        navigator_dashboard = NavigatorDashBoard()
        app = navigator_dashboard.createDashApplication()

        app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
