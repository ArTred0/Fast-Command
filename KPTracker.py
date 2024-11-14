try:
    import keyboard
    from os import startfile
    from json import loads

    def on_press():
        startfile('ChooseMenu.py')


    with open('choices.json', 'r') as file:
        hotkey = loads(file.read())['hotkey']
    keyboard.add_hotkey(hotkey, on_press)
    keyboard.wait()
except BaseException as exc:
    import time
    with open('debug.log', 'a') as log:
        log.write(f'{time.strftime("%d.%m.%Y - %H:%M:%S")}: {repr(exc)}\n')
    exit(-1)
with open('debug.log', 'a') as log:
    log.write(f'{time.strftime("%d.%m.%Y - %H:%M:%S")}: Programm self finished\n')