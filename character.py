# from Room import Room
# from Item import Item
# import json
from messages import messages


class Character:
    """
    Character class for Picnic Quest
    """
    def __init__(self, name, inventory=None, location=None):
        self.name = name
        self.inventory = inventory
        self.location = location

    def __repr__(self):
        return f"{self.name}\nLocation: {self.location}\n\
        Inventory: {[item.name for item in self.inventory]}"

    def add_item(self, item):
        # Adds item to inventory and sends confirmation
        # TODO does this response work here?
        self.inventory.append(item)
        return f"You picked up {item.name}"

    def drop_item(self, item):
        # Drops item in current room, and returns success message
        # If item is not in inventory returns error message
        if item in self.inventory:
            self.inventory.remove(item)
            self.location.object_list.append(item)
            return (f"You dropped the {item.name} in "
                    f"the {self.location.room_name}")

        else:
            return f"You don't have {item.name} in your inventory"

    def set_location(self, location):
        self.location = location

    # #####################################
    #                VERBS                #
    #  To be used for Features and Items  #
    # #####################################   

    def eat(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to eat."
        return messages.get(f"{target.name}.eat", "You can't eat that, sorry.")

    def read(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to read."
        return messages.get(f"{target.name}.read", "There is nothing here to read.")
    
    def nap(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to nap on."
        return messages.get(f"{target.name}.nap", "You can't nap here, unfortunately.")
    
    def give(self, target):
        # TODO - do we wanna do a receiver for this? Review this with team...
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to give."
        pass
    
    def use(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to use."
        pass
    
    def invite(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to invite."
        pass
    
    def talk(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to talk to."
        pass
    
    def wear(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to wear."
        pass
    
    def drop(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to drop."
        pass
    
    def scratch(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target} here to scratch."
        pass
    
    # def save(self):
    #     """
    #     Creates JSON file of current character.
    #     Saves into Character Saves folder
    #     Returns True if save was successful, False otherwise
    #     TODO - Is there a better way to store a saved character?
    #     """
    #     # Creats json file of all class features
    #     char_save = json.dumps(self.__dict__)

    #     with open("./backend/SaveFiles/temp.json", 'w') as f:
    #         f.write(char_save)
    #         return True

    # def load(self):
    #     """
    #     Loads the save file and deletes current state
    #     TODO - Implement a confirmation with user before completing the load
    #     TODO - Update the copying feature here if we add Character attributes
    #     """
    #     # First confirm with user. Send a y/n question, maybe?

    #     # read temp.json and update class
    #     with open("./backend/SaveFiles/temp.json", 'r') as f:
    #         new_char = json.load(f)

    #         # Replace attributes with saved attributes
    #         self.name = new_char["name"]
    #         self.inventory = new_char["inventory"]
    #         self.location = new_char["location"]


if __name__ == "__main__":
    hank = Character("Hank", ["Keys"], "The Zoo")
    print(hank)
    hank.set_location("Home")
    hank.add_item("Jacket")
    hank.add_item("backpack")
    print(hank)
    hank.load()
    print(hank)
