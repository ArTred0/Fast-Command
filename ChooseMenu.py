import tkinter as tk
from tkinter.messagebox import showerror
from subprocess import Popen, DETACHED_PROCESS
import ctypes
from math import ceil
import json
from os import startfile
# import re
# import os
from keyboard import hook_key

from controlable_widgets_grid import WidgetsGrid


def __create_bg_frame():
    return tk.Frame(master=root_container, bg='#28282F')


def __create_label(parent, text):
    return tk.Label(master=parent, text=text, font=('Roboto', 14), bg='#28282F', fg='#f7f7f7', padx=5, pady=5)


def __init_cell(label, bg, row, col, choice_dict, ind):
    WidgetsGrid(label, bg, row, col, lambda: execute(choice_dict['choices'][ind]['title'],
                                                     choice_dict['choices'][ind]['command'],
                                                     choice_dict['choices'][ind]['wd']))


def steal_focus():
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(root.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

    root.focus_set()


def set_geometry():
    width = root.winfo_width()
    height = root.winfo_height()
    root.geometry(f'{width}x{height}+{int(root.winfo_screenwidth() / 2 - width / 2)}+{int(root.winfo_screenheight() / 2 - height / 2)}')


def stop(ev=None):
    raise SystemExit


def settings(ev=None):
    startfile('shortcutsSetter.py')
    stop()


def execute(title: str,
            command: list,
            wd: str):

    print(f'{command=}\n{wd=}')
    try:
        if not wd:
            Popen(command.split(), creationflags=DETACHED_PROCESS)
        else:
            Popen(command.split(), cwd=wd, creationflags=DETACHED_PROCESS)
        root.destroy()
    except Exception as exc:
        showerror(str(exc), f'Error occurred while executing shortcut "{title}". Сheck that its command spelled correctly and try again.')


set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event

alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002

root = tk.Tk()
root['bg'] = '#7f7f7f'
root.overrideredirect(True)
root.attributes('-topmost', True)
root.bind('<FocusOut>', stop)
root.bind('<Escape>', stop)
hook_key('s', settings)

root_container = tk.Frame(bg='#28282F', padx=20, pady=20)
root_container.grid(row=0, column=0, padx=3, pady=3)
WidgetsGrid.root = root_container
WidgetsGrid.highlightColor = '#FFFFFF'


with open('choices.json', 'r') as file:
    choices: dict = json.loads(file.read())
    if len(choices['choices']) <= 4:
        cols = 2
    elif len(choices['choices']) <= 9:
        cols = 3
    elif len(choices['choices']) <= 16:
        cols = 4
    rows = ceil(len(choices['choices'])/cols)

    for row in range(rows):
        for col in range(cols):
            try:
                bg = __create_bg_frame()
                bg.grid(row=row, column=col, padx=10, pady=10)
                label = __create_label(bg, choices['choices'][row * cols + col]['title'])
                label.pack(padx=3, pady=3)
                __init_cell(label, bg, row, col, choices, row * cols + col)
            except IndexError:
                break


root.grid_rowconfigure('all', weight=1)
root.grid_columnconfigure('all', weight=1)

root_container.grid_rowconfigure('all', weight=1)
root_container.grid_columnconfigure('all', weight=1)

WidgetsGrid.track(root)

root.after(10, steal_focus)
root.after(10, set_geometry)

root.mainloop()
