class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def use_item(self, index, target):
        item = self.items.pop(index)
        if item.style == 'heal':
            target.hp += item.value
        elif item.style == 'damage':
            target.hp -= item.value
            
    def __str__(self):
        if len(self.items) == 0:
            return 'пусто'
        return ', '.join([item.name for item in self.items])