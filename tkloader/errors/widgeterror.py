class WidgetError(Exception):
    def __init__(self, widget: str, message: str = "Invalid widget type in JSON file") -> None:
        self.widget = widget
        self.message = message
        super(WidgetError, self).__init__(self.message)

    def __str__(self) -> str:
        return f"{self.widget} -> {self.message}"