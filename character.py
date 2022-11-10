from room import Room
from item import Item
from feature import Feature
# import json
from messages import messages


class Character:
    """
    Character class for Picnic Quest
    """
    def __init__(self, name, inventory=[], location=None):
        self.name = name
        self.inventory = inventory  # Holds objects of items in inventory
        self.location = location    # Object of current location
        self.helmet = False     # Helmet can push open bedroom door
        self.light = False      # Flashlight can light up basement
        self.invited = []       # Holds names of invited animals

    def __repr__(self):
        return f"{self.name}\nLocation: {self.location}\n\
        Inventory: {[item.name for item in self.inventory]}"

    def set_location(self, location):
        self.location = location

    def show_inventory(self):
        res = "Inventory: "
        if len(self.inventory) == 0:
            res += "None"
        else:
            for item in self.inventory:
                res += item.name + "\n"
        return res

    def show_guests(self):
        res = "Guest List: "
        if len(self.invited) == 0:
            res += "None"
        else:
            for invite in self.invited:
                res += invite + "\n"
        return res
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

    # Handle endgame
    def endgame(self):
        num_items = len(self.inventory)
        num_guests = len(self.invited)
        msg = f"You make your way to the park, where all of your friends are there waiting for you.\n\
                Congratulations! You've completed Picnic Quest!\nYou have brought {num_items} out of 5 \
                picnic items.\nYou have invited {num_guests} out of 4 guests to the picnic. Well done!\n\
                Type in newgame to start again",
        return msg

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
    jacket = Item('Jacket', "A Jacket", True, True)
    backpack = Item("Backpack", "a backpack", True, True)
    mouse = Feature('mouse', 'hes a mouse')
    zoo = Room(
        9,
        "Basement",
        messages["park.long"],
        messages["park.short"],
        object_list=[jacket, backpack],
        feature_list=[mouse],
        directions=[None, None, None, 6])
    home = Room(
        1,
        "home",
        messages["park.long"],
        messages["park.short"],
        [],
        [],
        [None, None, None, 6])
    hank = Character("Hank", [], zoo)
    print(hank)
    hank.show_inventory()
    # hank.set_location(home)
    hank.take(jacket)
    hank.take(backpack)
    hank.show_inventory()
    hank.show_guests()
    hank.invite(mouse)
    hank.show_guests()
    print(hank)
    # hank.load()
    # hank.endgame()
