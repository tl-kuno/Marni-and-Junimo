class Room:
    """
    Creates a full room environment
    """
    def __init__(self, room_id, room_name, long_description, short_description, object_list, directions):
        self.room_id = room_id
        self.room_name = room_name
        self.long_description = long_description
        self.short_description = short_description
        self.object_list = object_list
        self.directions = directions  # [North, East, South, West]

    def north(self):
        """
        Direction to the north, use in search for an entrance/exit
        """
        return self.directions[0]

    def east(self):
        """
        Direction to the east, use in search for an entrance/exit
        """
        return self.directions[1]

    def south(self):
        """
        Direction to the south, use in search for an entrance/exit
        """
        return self.directions[2]

    def west(self):
        """
        Direction to the west, use in search for an entrance/exit
        """
        return self.directions[3]

    def look(self):
        """
        repeats the long form explanation
        """
        print(self.long_description)

    def __repr__(self):
        """
        Display the name of the room, exits in the room, and items in the room
        """
        return "\nName: {}, Exits: {}, Items: {}".format(self.room_name, self.directions, self.object_list)


class Item:
    """
    Creates an item and how that item could be interacted with
    """
    def __init__(self, item_name, description, can_pick_up, can_drop):
        self.item_name = item_name
        self.description = description
        self.can_pick_up = can_pick_up
        self.can_drop = can_drop

    def look_at(self):
        """
        Fictionally interesting explanation of feature or object
        """
        print(self.description)

    def __repr__(self):
        return self.item_name


def main():
    """
    Main function
    """
    # stores items picked up in inventory
    inventory = []
    # list of all the rooms
    room_list = []

# -----------------------------------------------------
# -                      Items                        -
# -----------------------------------------------------

    # Item Name: Blueberries
    # Can Pick Up: Yes
    # Can Drop: Yes
    blueberries = Item("Blueberries", "Description", True, True)

    # Item Name: Mushrooms
    # Can Pick Up: Yes
    # Can Drop: Yes
    mushrooms = Item("Mushrooms", "Description", True, True)

    # Item Name: Dog Treats
    # Can Pick Up: Yes
    # Can Drop: Yes
    dog_treats = Item("Dog Treats", "Description", True, True)

    # Item Name: Towel
    # Can Pick Up: Yes
    # Can Drop: Yes
    towel = Item("Towel", "Description", True, True)

    # Item Name: Umbrella
    # Can Pick Up: Yes
    # Can Drop: Yes
    umbrella = Item("Umbrella", "Description", True, True)

    # Item Name: Letter
    # Can Pick Up: Yes
    # Can Drop: Yes
    letter = Item("Letter", "Description", True, False)

    # Item Name: Wooden Spoon
    # Can Pick Up: Yes
    # Can Drop: Yes
    wooden_spoon = Item("Wooden Spoon", "Description", True, True)

    # Item Name: Football Helmet
    # Can Pick Up: Yes
    # Can Drop: Yes
    football_helmet = Item("Football Helmet", "Description", True, True)

    # Item Name: Soap
    # Can Pick Up: Yes
    # Can Drop: Yes
    soap = Item("Soap", "Description", True, True)

    # Item Name: Flashlight
    # Can Pick Up: Yes
    # Can Drop: Yes
    flashlight = Item("Flashlight", "Description", True, True)

    # Item Name: Rocking Chair
    # Can Pick Up: No
    # Can Drop: No
    rocking_chair = Item("Rocking Chair", "Description", False, False)

# -----------------------------------------------------
# -                      Rooms                        -
# -----------------------------------------------------

    # Room ID: 0
    # Room: Living Room
    # Object List: Flashlight, Letter
    # Direction: [N: Kitchen, E: None , S: None, W: Basement]
    room_list.append(Room(
        0,
        "Living Room",
        "Long Description",
        "Short Description",
        [flashlight, letter],
        [2, None, None, 1]))

    # Room ID: 1
    # Room: Basement
    # Object List: Mushrooms
    # Direction: [N: None, E: None , S: Living Room, W: None]
    room_list.append(Room(
        1,
        "Basement",
        "Long Description",
        "Short Description",
        [mushrooms],
        [None, None, 0, None]))

    # Room ID: 2
    # Room: Kitchen
    # Object List: Wooden Spoon, Blueberries
    # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    room_list.append(Room(
        2,
        "Kitchen",
        "Long Description",
        "Short Description",
        [wooden_spoon, blueberries],
        [3, 0, None, None]))

    # Room ID: 3
    # Room: Pantry
    # Object List: Dog Treats
    # Direction: [N: None, E: None, S: Kitchen, W: None]
    room_list.append(Room(
        3,
        "Pantry",
        "Long Description",
        "Short Description",
        [dog_treats],
        [None, None, 2, None]))

    # Room ID: 4
    # Room: Bedroom
    # Object List: Football Helmet
    # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    room_list.append(Room(
        4,
        "Bedroom",
        "Long Description",
        "Short Description",
        [football_helmet],
        [5, None, None, 0]))

    # Room ID: 5
    # Room: Bathroom
    # Object List: Towel, Soap
    # Direction: [N: None, E: None, S: Bedroom, W: None]
    room_list.append(Room(
        5,
        "Bathroom",
        "Long Description",
        "Short Description",
        [towel, soap],
        [None, None, 4, None]))

    # Room ID: 6
    # Room: Porch
    # Object List: Rocking Chair
    # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    room_list.append(Room(
        6,
        "Porch",
        "Long Description",
        "Short Description",
        [rocking_chair],
        [0, 9, 8, 7]))

    # Room ID: 7
    # Room: Alley
    # Object List: Umbrella
    # Direction: [N: None, E: Porch, S: None, W: None]
    room_list.append(Room(
        7,
        "Alley",
        "Long Description",
        "Short Description",
        [umbrella],
        [None, 6, None, None]))

    # Room ID: 8
    # Room: Roof
    # Object List: ?
    # Direction: [N: Porch, E: None, S: None, W: None]
    room_list.append(Room(
        8,
        "Roof",
        "Long Description",
        "Short Description",
        [],
        [6, None, None, None]))

    # Room ID: 9
    # Room: Park
    # Object List: ?
    # Direction: [N: None, E: None, S: None, W: None]
    room_list.append(Room(
        9,
        "Park",
        "Long Description",
        "Short Description",
        [],
        [None, None, None, None]))

# -----------------------------------------------------
# -                      Test                         -
# -----------------------------------------------------

    print(room_list)

    # current_room = room_list[0]

    # # move north
    # if current_room.north() is None:
    #     print("Cannot go north!")
    # else:
    #     current_room = room_list[current_room.north()]


if __name__ == "__main__":
    main()
