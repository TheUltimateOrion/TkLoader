import json
import __main__
from tkinter import Button, Entry, Label, Tk, Widget, ttk

from tkloader.constants import IGNORE, LOAD_FILENOTFOUND, LOAD_WIDGETERROR, SUCCESS, WIDGET_INVALID
from tkloader.errors.eventerror import EventError
from tkloader.errors.widgeterror import WidgetError
from tkloader.logging.Logger import Logger

class Loader:
    
    __root: Tk | Widget

    def __init__(self, root: Tk | Widget) -> None:
        Logger.info("Initializing JSON Loader")
        self.__root = root

    def load(self, file: str) -> int:
        try:
            Logger.info("Loading JSON File...")
            with open(file, errors=IGNORE) as _f:
                _loaded = json.loads(_f.read())
                self.__loaded = _loaded
                self.__initWindow()
                self.__addWidgets()
                _f.close()
        except FileNotFoundError:
            Logger.error("Cannot open JSON File...", exc_info=True)
            exit(LOAD_FILENOTFOUND)
        return SUCCESS

    def __initWindow(self) -> int:
        Logger.info("Initialzing Window")
        loaded = self.__loaded
        _window: dict[str, any] 
        try: 
            _window = loaded['Window']
            self.__root.title(_window["Title"])
            self.__root.resizable(_window['IsResizable'][0], _window['IsResizable'][1])
            self.__root.geometry(f"{_window['Size_x']}x{_window['Size_y']}")
        except KeyError: Logger.warning("Window options not found, using defaults")
        return SUCCESS

    def __addWidgets(self) -> int:
        Logger.info("Loading widgets")        
        for _obj in self.__loaded["Widgets"]:
            if _obj == "Window": continue
            obj = self.__loaded["Widgets"][_obj]
            try:
                obj['TTK']
            except KeyError:
                obj = obj | {'TTK': True}
            match obj["Type"]:
                case "Label":
                    _label: Label | ttk.Label 
                    if obj["TTK"] == True:
                        _label = ttk.Label(self.__root, text=obj["Text"])
                    else:
                        _label = Label(self.__root, text=obj["Text"])
                    _label.pack()
                case "Button":
                    _button: Button | ttk.Button
                    if obj["TTK"] == True:
                        _button = ttk.Button(self.__root, text=obj["Text"])
                    else:
                        _button = Button(self.__root, text=obj["Text"])
                    try:
                        obj['Bind']
                        self.__bind(_button, obj)
                    except KeyError: pass
                    _button.pack()
                case "Entry":
                    _entry: Entry | ttk.Entry
                    if obj["TTK"] == True:
                        _entry = ttk.Entry(self.__root)
                    else:
                        _entry = Entry(self.__root)
                    _entry.pack()
                case _:
                    raise WidgetError(obj["Type"])
        return SUCCESS

    def __bind(self, button: Button | ttk.Button, obj: dict[str, any]) -> int:
        Logger.info("Binding actions...")
        try:
            button.config(command=eval(f"__main__.{obj['Bind']}"))
        except AttributeError:
            raise EventError("Event listener in JSON File is pointing to a null method")
        Logger.info("TkLoader has successfully loaded the JSON File")
        return SUCCESS