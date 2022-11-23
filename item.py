class Item:
    """
    Creates an item and how that item could be interacted with
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look_at(self):
        """
        Fictionally interesting explanation of feature or object
        """
        return self.description

    def __repr__(self):
        return self.name
