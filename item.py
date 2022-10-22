class Item:
    """
    Creates an item and how that item could be interacted with
    """
    def __init__(self, name, description, can_pick_up, can_drop):
        self.name = name
        self.description = description
        self.can_pick_up = can_pick_up
        self.can_drop = can_drop

    def look_at(self):
        """
        Fictionally interesting explanation of feature or object
        """
        return self.description

    def __repr__(self):
        return self.item_name
