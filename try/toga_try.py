import toga
from toga.style import Pack


def say_hello(widget):
    print("Hello!")


def build(app):
    btn = toga.Button("Say Hello", on_press=say_hello, style=Pack(padding=20))
    return toga.Box(children=[btn])


app = toga.App("My App", "tenantapp.space", startup=build)
app.main_loop()
