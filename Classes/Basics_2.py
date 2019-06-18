class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    pass

-----------------------------------------
class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    def add_item(self,item):   # this line satisfy the need of overriding the "add_item" function in child class
        super().add_item(item)  # this line calls super(), which regains the functionality defined in parent class.
        self.slots.sort()


