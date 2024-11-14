import tkinter
from typing import Callable


class WidgetsGrid:
    current_coord = {
        'col': 0,
        'row': 0,
    }
    widgets = set()
    focused = None
    root: tkinter.Tk = None
    highlightColor: str = None

    def __init__(self,
                 widget: tkinter.Widget,
                 background_frame: tkinter.Widget,
                 row: int,
                 column: int,
                 action: Callable):
        self.__widget = widget
        self.__widget.bind('<Enter>', lambda e: self.__refocus(self))
        self.__bgFrame = background_frame
        self.__row = row
        self.__col = column
        self.__action = action
        self.__widget.bind('<Button-1>', lambda e: self.__action())
        self.__add_widget(self)
        self.__check_focused(self)

    @classmethod
    def __check_focused(cls, instance):
        if not cls.focused:
            cls.focused = instance
            instance.__bgFrame['bg'] = cls.highlightColor

    @classmethod
    def __add_widget(cls, instance):
        cls.widgets.add(instance)

    @classmethod
    def track(cls, window: tkinter.Misc):
        window.bind('<Up>', cls.__up)
        window.bind('<Down>', cls.__down)
        window.bind('<Right>', cls.__right)
        window.bind('<Left>', cls.__left)
        window.bind('<Return>', lambda e: cls.focused.__action())

    @classmethod
    def __check_widget(cls):
        instance = None
        for w in cls.widgets:
            if w.__col == cls.current_coord['col'] and w.__row == cls.current_coord['row']:
                instance = w

        if instance:
            instance.__bgFrame['bg'] = cls.highlightColor
            cls.focused.__bgFrame['bg'] = cls.root['bg']
            cls.focused = instance

        return instance

    @classmethod
    def __up(cls, ev):
        cls.current_coord['row'] -= 1
        if not cls.__check_widget():
            cls.current_coord['row'] += 1

    @classmethod
    def __down(cls, ev):
        cls.current_coord['row'] += 1
        if not cls.__check_widget():
            cls.current_coord['row'] -= 1

    @classmethod
    def __right(cls, ev):
        cls.current_coord['col'] += 1
        if not cls.__check_widget():
            cls.current_coord['col'] -= 1

    @classmethod
    def __left(cls, ev):
        cls.current_coord['col'] -= 1
        if not cls.__check_widget():
            cls.current_coord['col'] += 1

    @classmethod
    def __refocus(cls, instance):
        instance.__bgFrame['bg'] = cls.highlightColor
        cls.focused.__bgFrame['bg'] = cls.root['bg']
        cls.focused = instance
        cls.current_coord = {
            'col': instance.__col,
            'row': instance.__row,
        }
