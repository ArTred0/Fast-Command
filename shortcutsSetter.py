import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import json


def clear_all():
    title_ent.delete(0, 'end')
    command_ent.delete(0, 'end')
    wd_ent.delete(0, 'end')


def validate_length(text, action):
    return action == 0 or len(text) <= 20


def insert_chosen(e):
    title = shortcuts.get()
    if title == 'Add new':
            clear_all()
            savebtn.configure(state='normal')
    for sc in data['choices']:

        if sc['title'] == title:
            clear_all()
            title_ent.insert(0, sc['title'])
            command_ent.insert(0, ''.join(sc['command']))
            wd_ent.insert(0, sc['wd'])
            savebtn.configure(state='normal')
            delbtn.configure(state='normal')


def save():
    title = title_ent.get()
    cmd = command_ent.get()
    wd = wd_ent.get()
    if not (title and cmd):
        mb.showerror('Error', 'Fields "Title" and "Command" are required!')
        return
    if shortcuts.get() == 'Add new':
        if title_ent.get() == 'Add new':
            mb.showerror('Error', 'You cannot create shortcut named "Add new"')
            return
        else:
            shortcut = {
                'title': title,
                'command': cmd,
                'wd': wd,
            }
            data['choices'].append(shortcut)
    else:
        prev = shortcuts.get()
        for c in data['choices']:
            if c['title'] == prev:
                c['title'] = title
                c['command'] = cmd
                c['wd'] = wd
    with open('choices.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    clear_all()
    vals = [v['title'] for v in data['choices']]
    vals.insert(0, 'Add new')
    shortcuts.configure(values=vals)
    shortcuts.set('Choose shortcut')
    savebtn.configure(state='disabled')
    delbtn.configure(state='disabled')


def delete():
    answ = mb.askyesno('Deleting', f'Are you sure you want delete "{shortcuts.get()}" shortcut?')
    if answ:
        for c in data['choices']:
            if c['title'] == shortcuts.get():
                data['choices'].remove(c)
                with open('choices.json', 'w') as file:
                    file.write(json.dumps(data, indent=4))
                clear_all()
                vals = [v['title'] for v in data['choices']]
                shortcuts.configure(values=vals)
                shortcuts.set('Choose shortcut')
                savebtn.configure(state='disabled')
                delbtn.configure(state='disabled')


FONT = ('Roboto', 11)
root = tk.Tk()
root.title('Shortcuts settings')
root.attributes('-toolwindow', True)
root.attributes('-topmost', True)
with open('choices.json', 'r') as file:
    data = json.loads(file.read())
    vals = [v['title'] for v in data['choices']]
    vals.insert(0, 'Add new')

shortcuts = ttk.Combobox(root, values=vals, state='readonly', font=FONT)
shortcuts.bind('<<ComboboxSelected>>', insert_chosen)
shortcuts.pack(padx=10, pady=10, anchor='w')
shortcuts.set('Choose shortcut')

tk.Label(root, text='Title in the menu:', font=FONT).pack(padx=10, anchor='w')

vcmd = (root.register(validate_length), '%P', '%d')
title_ent = tk.Entry(root, font=FONT, width=25, validate='key', validatecommand=vcmd)
title_ent.pack(padx=10, pady=10, anchor='w')

tk.Label(root, text='Command:', font=FONT).pack(padx=10, anchor='w')

command_ent = tk.Entry(root, font=FONT, width=50)
command_ent.pack(padx=10, pady=10, fill='x')

tk.Label(root, text='Working directory:', font=FONT).pack(padx=10, anchor='w')

wd_ent = tk.Entry(root, font=FONT, width=50)
wd_ent.pack(padx=10, pady=10, fill='x')

savebtn = tk.Button(root, text='Save', font=FONT, command=save, state='disabled')
savebtn.pack(padx=10, pady=10, fill='x')

delbtn = tk.Button(root, text='Delete', font=FONT, command=delete, state='disabled')
delbtn.pack(padx=10, pady=10, fill='x')

root.mainloop()