# This is not for me. Because it runs of Terminal and I don't have it.

from textual.app import App
from textual.widgets import Header, Footer


class MyApp(App):
    def compose(self):
        yield Header()
        yield Footer()


MyApp().run()
