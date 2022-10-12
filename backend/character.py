"""
Character class for Picnic Quest
"""


class Character:

    def __init__(self, name, inventory, location):
        self.name = name
        self.inventory = []
        self.location = None

    def __repr__(self):
        return f"{self.name}\nLocation: {self.location}\n\
            Inventory: {[item for item in self.inventory]}"
