# from room import Room
from item import Item
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
        self.helmet = False     # Helmet can push open bedroom door
        self.light = False      # Flashlight can light up basement
        self.invited = []

    def __repr__(self):
        return f"{self.name}\nLocation: {self.location}\n\
        Inventory: {[item.name for item in self.inventory]}"

    def set_location(self, location):
        self.location = location

    # #####################################
    #                VERBS                #
    #  To be used for Features and Items  #
    # #####################################

    def take(self, target):
        # Adds item to inventory and sends confirmation
        if target not in self.location.object_list:
            return f"There is no {target.name} to pick up.\n"
        self.inventory.append(target)
        return f"You picked up the {target.name}.\n"

    def drop(self, item):
        # Drops item in current room, and returns success message
        # If item is not in inventory returns error message
        if item in self.inventory:
            self.inventory.remove(item)
            self.location.object_list.append(item)
            return (f"You dropped the {item.name} in "
                    f"the {self.location.room_name}")
        else:
            return f"You don't have {item.name} in your inventory"

    def eat(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to eat."
        return messages.get(f"{target.name}.eat", "You can't eat that, sorry.")

    def read(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to read."
        return messages.get(f"{target.name}.read", "There is nothing here to read.")

    def nap(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to nap on."
        return messages.get(f"{target.name}.nap", "You can't nap here, unfortunately.")

    def scratch(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to scratch."
        return messages.get(f"{target.name}.scratch", "You can't scratch that, unfortunately.")
    
    def use(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to use."
        # Using flashlight
        if target.name == "flashlight":
            self.light = True
            return messages.get("flashlight.use")
        # Using helmet
        if target.name == "helmet":
            self.helmet = True
            return messages.get("helmet.use")
        # Using spoon
        if target.name == "wooden spoon":
            if self.location.room_name == 'Pantry':
                self.inventory.append(Item("dog treats",
                                           messages['dog_treats'],
                                           True,
                                           True))
                return messages.get('wooden spoon.use')
        # Using soap on raccoon
        if target.name == "soap":
            if self.location.room_name == "Alley":
                self.inventory.append(Item("umbrella", messages['umbrella'], True, True))
        # Using letter
        if target.name == 'letter':
            return messages.get('letter')
        # Invalid command
        return f"There is no {target.name} here to use."

    def invite(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to invite."

        # Invite the mouse
        if target.name == 'mouse' and self.location.room_name == 'Basement':
            self.invited.append('mouse')
            return messages.get('mouse.invite')

        # Invite the ants
        if target.name == 'ants' and self.location.room_name == 'Kitchen':
            self.invited.append('ants')
            return messages.get('ants.invite')

        # Invite the raccoon
        if target.name == 'raccoon' and self.location.room_name == 'Alley':
            self.invited.append('raccoon')
            return messages.get('raccoon.invite')

        # Invite the birds
        if target.name == 'birds' and self.location.room_name == 'Roof':
            self.invited.append('birds')
            return messages.get('birds.invite')

        # Invalid
        return f"There is no {target.name} here to invite."

    def talk(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to talk to."
        return messages.get(f"{target.name}.talk", "You can't talk to that, unfortunately.")

    def wear(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to wear."
        if target.name == 'football helmet':
            self.helmet = True
        return messages.get(f"{target.name}.wear", "You can't wear that, unfortunately.")

    def listen(self, target):
        # Error handling
        if target not in self.inventory:
            if target not in self.location.object_list:
                if target not in self.location.feature_list:
                    return f"There is no {target.name} here to listen to."
        return messages.get(f"{target.name}.listen", "Nothing to listen to here.")

    # def give(self, target):
    #     # TODO - do we wanna do a receiver for this? Review this with team...
    #     # Error handling
    #     if target not in self.inventory:
    #         if target not in self.location.object_list:
    #             if target not in self.location.feature_list:
    #                 return f"There is no {target.name} here to give."
    #     pass

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
