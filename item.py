class Item:
    def __init__(self, name, style, value):
        self.name = name
        self.style = style
        self.value = value
        
    def __str__(self):
        return f"{self.name} ({self.style} {self.value})"