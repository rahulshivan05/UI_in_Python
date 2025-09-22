# import remi.gui as gui
# from remi import App, start


# class MyApp(App):
#     def main(self):
#         # Create a container (e.g., VBox for vertical arrangement)
#         main_container = gui.VBox(width=300, height=100)

#         # Create a label widget
#         hello_label = gui.Label("Hello, REMI!")

#         # Add the label to the container
#         main_container.append(hello_label)

#         # Return the root widget of your application
#         return main_container


# if __name__ == '__main__':
#     # Start the REMI application
#     # start_browser=True will automatically open the browser
#     start(MyApp, start_browser=True)


import remi.gui as gui
from remi import start, App


class MyApp(App):
    def main(self):
        btn = gui.Button('Click me')
        btn.onclick.do(lambda x: btn.set_text('Clicked!'))
        return btn


start(MyApp)
