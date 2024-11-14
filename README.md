# What is it?
It's an app that allows you to open a menu, using a hotkey, and choose a shortcut in GUI to quickly execute saved command. It allows user not to open cmd every time he need to use it to execute command he uses often like opening some apps or anything else

# How to use it?

## Opening the menu
Firstly you need to launch main app (KPTracker) in background and when you will need it, just press Ctrl+Shift+Alt+U and here you go, you can navigate in this menu using Up, Down, Left and Right keys or just choose it using a mouse.

## Settings
When you will decide to create or change existing shortcut just press "S" key while in menu, and here you go.

To create new one choose "Add new" in a dropdown menu and enter its title that will be displayed in the menu, command of this shortcut (like that ones you enter in CMD) and, if you need it (optionally), a working directory (wd) for this command and then press Save button.

To change existing one choose it in the dropdown menu, change properties you want and press Save button.

To delete shortcut choose it in the dropdown and press Delete button in the bottom of the window.

# Restrictions
1) You can create up to 16 shortcuts, not more
2) To use this project you must install "keyboard" package for python global interpreter and, if you have multiple versions of python, make sure that when you type "python" in cmd you see right version of it with keyboard package
3) To make it start automatically after logging in to the system you should manually create shortcut for KPTracker.py in Startup directory that is located in - C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
