from room import Room
from item import Item
from feature import Feature
from messages import messages
from nav import Direction
from roomlist import init_room_list_and_items
from verb import VerbClass, verb_dict
import os
import pickle
import json

home_dir = os.path.dirname(__file__)
users_dir = os.path.join(home_dir, "game_data/users")

def create_load_name_array(ip_address):
    load_games = []
    for filename in os.listdir(users_dir):
        split_file_ext = filename.split(".p")
        identifiers = split_file_ext[0].split("-")
        if identifiers[1] == ip_address:
            load_games.append(identifiers[0])
    return load_games


class Character:
    """
    Character class for Picnic Quest
    """
    def __init__(self, key, ip_address, identifier,
                 inventory=[], location=None):
        self.messages = self.init_messages()
        self.key = key
        self.inventory = inventory  # Holds objects of items in inventory
        self._save_inventory = inventory
        self.helmet = False     # Helmet can push open bedroom door
        self._save_helmet = False
        self.light = False      # Flashlight can light up basement
        self._save_light = False
        self.invited = []       # Holds names of invited animals
        self._save_invited = []
        self.identifier = identifier
        self.ip_address = ip_address
        self._save_ip_address = None
        self.room_list = init_room_list_and_items()
        self._save_room_list = init_room_list_and_items()

        self.location = self.room_list[0]    # Object of current location
        self._save_location_id = 0

    def __repr__(self):
        return f"{self.name}\nLocation: {self.location}\n\
        Inventory: {[item.name for item in self.inventory]}"

    def init_messages(self):
        dir = os.path.dirname(__file__)
        file_path = os.path.join(dir, "game_data/messages.json")
        message_instance = open(file_path, "r+")
        messages = json.load(message_instance)
        return messages['messages'][0]

    def newgame(self):
        self.inventory = []
        self.invited = []
        self.light = False
        self.helmet = False

        self.room_list = init_room_list_and_items()
        self.location = self.room_list[0]
        return messages['intro']

    def handle_user_input(self, command):     # noqa: C901
        noun = ""
        command = command.strip().lower()
        if len(command) == 0:
            return "You didnt say anything!"

        if command == "inventory":
            return self.show_inventory()

        if command == "guestlist":
            return self.show_guests()

        if command == "help":
            return self.messages.get("help")

        # Changed maxsplit to 2 to handle 'look at'
        input_components = command.split(maxsplit=2)
        verb = input_components[0]

        # Allow 'look at' to identify correct verb
        if verb == 'look' and len(input_components) > 2:
            if input_components[1] == 'at':
                noun = input_components[2].strip()
                verb = 'look at'
        # Allow 'nap on' to identify correct verb
        if verb == 'nap' and len(input_components) > 2:
            if input_components[1] == 'on':
                noun = input_components[2].strip()
                verb = 'nap on'
        # Allow 'pick up' to identify correct verb
        if verb == 'pick' and len(input_components) > 2:
            if input_components[1] == 'up':
                noun = input_components[2].strip()
                verb = 'pick up'
        # For one word verb commands
        elif len(input_components) > 1 and verb != 'look at' and verb != 'nap on':
            noun = command.split(maxsplit=1)[1].strip()

        # determine our verb class
        verb_class = -1
        if verb not in verb_dict:
            # check if this is one of our exits or directions
            if command not in self.location.direction_dict:
                return "invalid command, try again..."
            verb_class = VerbClass.MOVE_PRIME
        else:
            verb_class = verb_dict[verb]    # returns verb_class enum
            if verb_class != VerbClass.LOOK and len(input_components) == 1:
                if verb_class != VerbClass.SAVE and len(input_components) == 1:
                    if verb_class != VerbClass.LOAD and len(input_components) == 1:
                        return f"{verb} requires a noun argument"

        # handle each verb class
        if verb_class == VerbClass.MOVE:
            return self.move(noun, self.room_list)
        if verb_class == VerbClass.MOVE_PRIME:
            return self.move(command, self.room_list)
        if verb_class == VerbClass.TAKE:
            return self.take(noun)
        if verb_class == VerbClass.DROP:
            return self.drop(noun)
        if verb_class == VerbClass.EAT:
            return self.eat(noun)
        if verb_class == VerbClass.READ:
            return self.read(noun)
        if verb_class == VerbClass.NAP:
            return self.nap(noun)
        if verb_class == VerbClass.SCRATCH:
            return self.scratch(noun)
        if verb_class == VerbClass.USE:
            return self.use(noun)
        if verb_class == VerbClass.INVITE:
            return self.invite(noun)
        if verb_class == VerbClass.TALK:
            return self.talk(noun)
        if verb_class == VerbClass.WEAR:
            return self.wear(noun)
        if verb_class == VerbClass.LISTEN:
            return self.listen(noun)
        if verb_class == VerbClass.LOOK:
            return self.location.long_description
        if verb_class == VerbClass.LOOK_AT:
            return self.look_at(noun)
        if verb_class == VerbClass.SAVE:
            return self.savegame()
        if verb_class == VerbClass.LOAD:
            # Need to send a confirmation prompt?
            return self.loadgame(noun)

        return "verb [{}] not yet supported...".format(verb)

    def savegame(self):
        filename = self.key + "-" + self.ip_address + ".pickle"
        full_path = users_dir + "/" + filename
        pq_data = open(full_path, "wb")
        pickle.dump(self, pq_data)
        pq_data.close()

        # # Saves current character stats to private values
        # self._save_inventory = self.inventory[:]
        # self._save_invited = self.invited[:]
        # self._save_helmet = self.helmet
        # self._save_light = self.light

        # self._save_room_list = deepcopy(self.room_list)
        # self._save_location_id = self.room_list.index(self.location)
        # print(self._save_location_id)
        # print(self.room_list[self._save_location_id])

        return "Saved your game!"

    def loadgame(self, noun=""):
               
        list_games_string = "Be careful, your current progress will not be saved!\nTo abort enter any command."\
                            "\n\nWhich username would you like to load?\n"
        no_games = "Hmm, it looks like there are no games to load."
        saved_games = create_load_name_array(self.ip_address)
        print("The noun is " + noun)
        if len(saved_games) > 0 and noun == "":
            for game in saved_games:
                list_games_string = list_games_string  + "\n  " + game
            list_games_string += "\n\nType ' loadgame username ' to select a game to load..."
            return(list_games_string)
        elif noun in saved_games:
            identifier = noun + "-" + self.ip_address
        elif noun != "":
            return("Username not found")
        else:
            return(no_games)


        # # swaps current stats with saved stats
        # self.inventory = self._save_inventory[:]
        # self.helmet = self._save_helmet
        # self.light = self._save_light
        # self.invited = self._save_invited[:]
        # # Flip this?
        # self.room_list = deepcopy(self._save_room_list)
        # self.location = self.room_list[self._save_location_id]

        # return "Loaded your game!"

    def set_location(self, location):
        self.location = location

    def show_inventory(self):
        res = "Inventory: "
        if len(self.inventory) == 0:
            res += "None"
        else:
            for item in self.inventory:
                res += "\n" + item.name
        return res

    def show_guests(self):
        res = "Guest List: "
        if len(self.invited) == 0:
            res += "None"
        else:
            for invite in self.invited:
                res += "\n"+ invite
        return res

    def in_object_list(self, o_list, target_name):
        o_idx = -1
        for i in range(len(o_list)):
            if target_name.lower() == o_list[i].name.lower():
                o_idx = i
                break
        return o_idx

    # flake8: noqa: C901
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

    def move(self, direction, room_list):   # noqa: C901
        direction = direction.lower()
        if direction not in self.location.direction_dict:
            return "No Exit: {}".format(direction)
        direction_category = self.location.direction_dict[direction]
        if direction_category == Direction.NORTH:
            # Check for basement block
            if self.location.room_name == 'Living Room':
                if not self.light:
                    return messages['basement.block']
            # move north
            if self.location.north() is not None:
                self.location.visited = True
                self.location = room_list[self.location.north()]
                return self.location.get_description()
        elif direction_category == Direction.EAST:
            # Check for bedroom block
            if self.location.room_name == 'Living Room':
                if not self.helmet:
                    return messages['bedroom.block']
            # move east
            if self.location.east() is not None:
                self.location.visited = True
                self.location = room_list[self.location.east()]
                return self.location.get_description()
        elif direction_category == Direction.SOUTH:
            # move south
            if self.location.south() is not None:
                self.location.visited = True
                self.location = room_list[self.location.south()]
                return self.location.get_description()
        elif direction_category == Direction.WEST:
            # move west
            if self.location.west() is not None:
                self.location.visited = True
                self.location = room_list[self.location.west()]
                return self.location.get_description()
        else:
            return "invalid direction enum, bad config"
        return "Cannot go to the {}!".format(direction)

    def take(self, target):
        # Retrieves object if item in room exists with the name 'target'
        object_idx = self.in_object_list(self.location.object_list, target)
        # check if we found a valid item
        if object_idx == -1:
            return "I don't think the humans would appreciate you trying to take that.\n"
        # remove object from room
        target_object = self.location.object_list.pop(object_idx)
        # add item to inventory
        self.inventory.append(target_object)
        return f"You picked up the {target_object.name}.\n"

    def look_at(self, target_name):
        # Retrieves object if item in room exists with the name 'target'
        target = self.retrieve_object_from_game(target_name)

        # If found, return message
        if target is not None:
            if target.name == 'friends':
                if self.location.room_name == "Roof":
                    return "Your friends are waiting for you! Hurry up and meet them."
                self.num_items = len(self.inventory)
                self.num_guests = len(self.invited)
                msg = "You make your way to the park, where all of your friends are "\
                      "there waiting for you.\n\nCongratulations!\nYou've completed Picnic Quest!\nYou have brought "
                msg += str(self.calc_inv())
                msg += " out of 5 picnic items.\nYou have invited "
                msg += str(self.num_guests)
                msg += " out of 4 guests to the picnic. Well done!\n"
                return msg
            return self.messages.get(target.name, f'cant look at {target.name}')
        return f"cant find {target_name}"

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
            return f"There is no {target_name} here to eat."
        return self.messages.get(f"{target.name}.eat", "You can't eat that, sorry.")

    def read(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to read."
        return self.messages.get(f"{target.name}.read", "There is nothing here to read.")

    def nap(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to nap on."
        return self.messages.get(f"{target.name}.nap", "You can't nap here, unfortunately.")

    def scratch(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to scratch."
        return self.messages.get(f"{target.name}.scratch", "You can't scratch that, unfortunately.")

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
        if target.name == "football helmet":
            self.helmet = True
            return self.messages.get("football helmet.use")
        # Using spoon
        if target.name == "wooden spoon":
            self.treats = self.retrieve_object_from_game('dog treats')
            if self.treats is not None:
                return self.messages.get('wooden spoon.use')
        # Using soap on raccoon
        if target.name == "soap":
            if self.location.room_name == "Alley":
                self.inventory.append(Item("umbrella", self.messages['umbrella']))
                return self.messages.get('soap.use')

            return "Maybe you should save that soap for someone who really needs it."
        # Using letter
        if target.name == 'letter':
            return messages.get('letter')
        # Invalid command
        return f"There is no {target.name} here to use."

    def invite(self, target_name):       # noqa: C901
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to invite."

        # Invite the mouse
        if target.name == 'mouse' and self.location.room_name == 'Basement':
            # Error check
            if "mouse" not in self.invited:
                self.invited.append('mouse')
                return self.messages.get('mouse.invite')
            return "You have already invited the mouse."

        # Invite the ants
        if target.name == 'ants' and self.location.room_name == 'Kitchen':
            if 'ants' not in self.invited:
                self.invited.append('ants')
                return self.messages.get('ants.invite')
            return "You have already invited the ants."

        # Invite the raccoon
        if target.name == 'raccoon' and self.location.room_name == 'Alley':
            if "raccoon" not in self.invited:
                self.invited.append('raccoon')
                return self.messages.get('raccoon.invite')
            return "You have already invited the raccoon."

        # Invite the birds
        if target.name == 'birds' and self.location.room_name == 'Roof':
            if "birds" not in self.invited:
                self.invited.append('birds')
                return self.messages.get('birds.invite')
            return "You have already invited the birds."
        # Invalid
        return f"There is no {target.name} here to invite."

    def talk(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to talk to."
        return self.messages.get(f"{target.name}.talk", "You can't talk to that, unfortunately.")

    def wear(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to wear."
        if target.name == 'football helmet':
            self.helmet = True
        return messages.get(f"{target.name}.wear", "You can't wear that, unfortunately.")

    def listen(self, target_name):
        # Error handling
        target = self.retrieve_object_from_game(target_name)
        if target is None:
            return f"There is no {target_name} here to listen to."
        return self.messages.get(f"{target.name}.listen", "Nothing to listen to here.")

    def calc_inv(self):
        # Returns the number of picnic items in player inventory
        res = 0
        needed = ['blueberries', 'mushrooms', 'dog treats', 'towel', 'umbrella']
        for item in self.inventory:
            if item.name in needed:
                res += 1
        return res


# if __name__ == "__main__":
    # jacket = Item('Jacket', "A Jacket")
    # backpack = Item("Backpack", "a backpack")
    # mouse = Feature('mouse', 'hes a mouse')
    # zoo = Room(
    #     9,
    #     "Basement",
    #     self.messages["park.long"],
    #     self.messages["park.short"],
    #     object_list=[jacket, backpack],
    #     feature_list=[mouse],
    #     directions=[None, None, None, 6])
    # home = Room(
    #     1,
    #     "home",
    #     self.messages["park.long"],
    #     self.messages["park.short"],
    #     [],
    #     [],
    #     [None, None, None, 6])
    # hank = Character("Hank", [], zoo)
    # print(hank)
    # hank.show_inventory()
    # # hank.set_location(home)
    # hank.take(jacket)
    # hank.take(backpack)
    # hank.show_inventory()
    # hank.show_guests()
    # hank.invite(mouse)
    # hank.show_guests()
    # print(hank)
    # # hank.load()
    # # hank.endgame()
