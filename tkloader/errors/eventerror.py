class EventError(Exception):
    def __init__(self, obj: dict[str, any], message="Event listener in JSON File is pointing to a null method") -> None:
        self.bind = obj['Bind']
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"{self.bind} -> {self.message}"