from room import Room
from item import Item
from feature import Feature
# import json
from messages import messages
from nav import Direction


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

    def in_object_list(self, o_list, target_name):
        o_idx = -1
        for i in range(len(o_list)):
            if target_name.lower() == o_list[i].name.lower():
                o_idx = i
                break
        return o_idx

    def retrieve_object_from_game(self, target_name):
        """
        Searches and retrieves (but does not remove) an item from player's inventory,
        the current room's object list, or the current rooms feature list with the
        name 'target_name' exists
        """
        target = None
        # check if in inventory
        object_idx = self.in_object_list(self.inventory, target_name)
        # not in inventory
        if object_idx == -1:
            # check if in room
            object_idx = self.in_object_list(self.location.object_list, target_name)
            # not in room
            if object_idx == -1:
                # check if in feature list
                object_idx = self.in_object_list(self.location.feature_list, target_name)
                if object_idx != -1:
                    # found in feature list
                    target = self.location.feature_list[object_idx]
            else:
                # found in room
                target = self.location.object_list[object_idx]
        else:
            # found in inventory
            target = self.inventory[object_idx]
        return target

    # #####################################
    #                VERBS                #
    #  To be used for Features and Items  #
    # #####################################

    def move(self, direction, room_list):
        direction = direction.lower()
        if direction not in self.location.direction_dict:
            return "No Exit: {}".format(direction)
        direction_category = self.location.direction_dict[direction]
        if direction_category == Direction.NORTH:
            # move north
            if self.location.north() is not None:
                self.location = room_list[self.location.north()]
                return self.location.short_description
        elif direction_category == Direction.EAST:
            # move east
            if self.location.east() is not None:
                self.location = room_list[self.location.east()]
                return self.location.short_description
        elif direction_category == Direction.SOUTH:
            # move south
            if self.location.south() is not None:
                self.location = room_list[self.location.south()]
                return self.location.short_description
        elif direction_category == Direction.WEST:
            # move west
            if self.location.west() is not None:
                self.location = room_list[self.location.west()]
                return self.location.short_description
        else:
            return "invalid direction enum, bad config"
        return "Cannot go to the {}!".format(direction)

    def take(self, target):
        # Retrieves object if item in room exists with the name 'target'
        object_idx = self.in_object_list(self.location.object_list, target)
        # check if we found a valid item
        if object_idx == -1:
            return f"There is no {target} to pick up.\n"
        # remove object from room
        target_object = self.location.object_list.pop(object_idx)
        # add item to inventory
        self.inventory.append(target_object)
        return f"You picked up the {target_object.name}.\n"

    def drop(self, item):
        # check if item in inventory with requested name
        object_idx = self.in_object_list(self.inventory, item)
        # check if we found the valid item
        if object_idx == -1:
            return f"You don't have {item} in your inventory"
        # remove item from inventory
        item_object = self.inventory.pop(object_idx)
        # put item in current room
        self.location.object_list.append(item_object)
        return (f"You dropped the {item_object.name} in "
                f"the {self.location.room_name}")

    def eat(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name.name} here to eat."
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

    def use(self, target_name):  # noqa: C901
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to use."
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
