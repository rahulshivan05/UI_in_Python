# this is good for Desktop and Mobile

import flet as ft


def main(page: ft.Page):
    btn = ft.ElevatedButton(
        text="Click me!", on_click=lambda e: print("Clicked"))
    page.add(btn)


ft.app(target=main)
