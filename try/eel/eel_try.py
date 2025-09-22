import eel

eel.init('web')  # folder with your index.html


@eel.expose
def say_hello_py(name):
    print(f'Hello from Python, {name}!')


eel.start('index.html')
