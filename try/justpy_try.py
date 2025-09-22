import justpy as jp


def hello():
    wp = jp.WebPage()
    jp.Div(text='Hello, world!', classes='text-xl', a=wp)
    return wp


jp.justpy(hello)
