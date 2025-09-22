# Just like tkinter for desktop app

import dearpygui.dearpygui as dpg

dpg.create_context()
with dpg.window(label="Demo Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Click Me")
dpg.create_viewport(title='Lol Title')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
