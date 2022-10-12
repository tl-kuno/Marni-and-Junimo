def test_function():
    sample = "I made it to the other file."
    return sample


class Room:
    """
    Creates a full room environment
    """
    def __init__(self, room_id, room_name, long_description,
                 short_description, object_list, directions):
        self.room_id = room_id
        self.room_name = room_name
        self.long_description = long_description
        self.short_description = short_description
        self.object_list = object_list
        self.directions = directions  # [North, East, South, West]
        self.visited = False        # Show full description only on first visit

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
        return "\nName: {}, Exits: {}, Items: {}".format(
            self.room_name, self.directions, self.object_list)


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
        "You are in a warm, cozy living room. Sunlight pours through the \
            windows, lighting up familiar sofa in the center of the room.\
            There are no signs of humans around here, just the soft sound \
            of the trees rustling in the breeze outside. You stretch your \
            paws and arch your back, slowly waking up from a relaxing nap. \
            You suddenly realize that a letter has been placed on \
            the pillow in front of you.\nTo the North of you, you can see \
            the door to the basement.\nTo the East, you can see the closed\
             door to the bedroom.\nTo the South, you can see the front door\
             that leads to the porch outside.\nTo the West, you see the\
             doorway to the kitchen.\n",
        "You are in the comfortable living room in the center of the house. \
            A large comfortable sofa sits in the center of the room.\n\
            To the North of you, you can see the door to the basement.\
            \nTo the East, you can see the closed door to the bedroom.\
            \nTo the South, you can see the front door that leads to \
            the porch outside.\nTo the West, you see the doorway to \
            the kitchen.\n",
        # Add sofa as an object to search and find flashlight?
        [flashlight, letter],
        [1, 4, 6, 2]))

    # Room ID: 1
    # Room: Basement
    # Object List: Mushrooms
    # Direction: [N: None, E: None , S: Living Room, W: None]
    room_list.append(Room(
        1,
        "Basement",
        "You make your way down the creaky wooden stairs into the \
            cold basement. Cobwebs line the handrail as you decend \
            into the dimly lit room. \
            The humans clearly don't come down here very often. \
            Beneath the stairs you can smell the distinct scent of ripe, \
            delicious violet mushrooms. These would be an excellent snack \
            for your friends at the picnic!\nThe only way out of the basement\
             is South, which takes you back to the Living Room.\n",
        "The cold, dark basement is eerily quiet. Only a small amount of light\
             peeks in from the doorway upstairs. Beneath the stairway a patch \
            of ripe, tasty mushrooms are growing. \nThe only way out of the \
            basement is South, back to the living room.\n",
        [mushrooms],
        [None, None, 0, None]))

    # Room ID: 2
    # Room: Kitchen
    # Object List: Wooden Spoon, Blueberries
    # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    room_list.append(Room(
        2,
        "Kitchen",
        "You stand in the brightly lit kitchen. The white tile floor glistens \
            brightly, and rumbling sound of the running dishwasher fills the \
            room. The humans must have been clumsy earlier, because a thick \
            wooden ladle has rolled under the table in the center of the room.\
             On the sleek marble countertops, you can see the corner of a \
            plastic container of scrumptious, freshly picked blueberries! \
            These would be perfect for a picnic!\nThe door to the pantry is\
             ajar to the North of you.\nThe open doorway to the living room \
            is to the East.\n",
        "You find yourself in the brightly lit kitchen. \nTo the North, you \
            can see the pantry door.\nTo the East, you can see the doorway to \
            the living room.\n",
        [wooden_spoon, blueberries],
        [3, 0, None, None]))

    # Room ID: 3
    # Room: Pantry
    # Object List: Dog Treats
    # Direction: [N: None, E: None, S: Kitchen, W: None]
    room_list.append(Room(
        3,
        "Pantry",
        "You stand in the well-stocked pantry, looking at shelves packed \
            floor to ceiling with human food. Boxes of Poptarts and other \
            processed food sit on the middle shelves, but these are no There\
             are plenty of dried food in tricky jars and tupperware that would\
             be impossible to get into without thumbs. Luckily, there is a bin\
             full of yummy kibble situated on the bottom shelf in front of \
            you The lid is really heavy, so you will need something strong to \
            prop it open in order to stock up on the tasty snacks.\nTo the \
            South, you can see the kitchen.\n",
        "You stand in the well-stocked pantry, looking at shelves packed floor\
             to ceiling with human food. There is a bin full of kibble on the \
            bottom shelf in front of you. \nTo the South, you can see the \
            kitchen.\n",
        [dog_treats],
        [None, None, 2, None]))

    # Room ID: 4
    # Room: Bedroom
    # Object List: Football Helmet
    # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    room_list.append(Room(
        4,
        "Bedroom",
        "You stand in the human's bedroom, at the foot of their mattress. \
            Framed photos of smiling humans are hung up on each wall. A \
            sunbeam cuts through the window, highlighting a tempting \
            napping spot in the balled up, fuzzy green blanket on the \
            human's bed. You can hear the sound of birds chirping from \
            right outside. \nTo the North, you can see the open doorway \
            to the bathroom.\n",
        "You are in the bedroom. A sunny spot on the bed looks like the \
            perfect location to take a nice long mid-day nap. To the \
            North, you can see the open doorway to the bathroom.\n",
        [football_helmet],
        [5, None, None, 0]))

    # Room ID: 5
    # Room: Bathroom
    # Object List: Towel, Soap
    # Direction: [N: None, E: None, S: Bedroom, W: None]
    room_list.append(Room(
        5,
        "Bathroom",
        "You stand in the well-maintained bathroom. Blue and green tiles line\
             the floor, and you can smell citrus-scented cleaners that the \
            humans used this morning. The drip-drip-drip sound of the sink \
            echos in the small room. On the side of the bathtub you can see \
            a bar of fresh, unscented soap. Hanging on a nearby rack is a \
            red-and-white checkered towel, which would look amazing as a \
            picnic blanket!\nTo the South, you can see the bedroom\n",
        "You stand in the clean bathroom. You can see a bar of soap on the \
            side of the bathtub. There is a checkered towel hanging on a rack,\
             which would look amazing as a picnic blanket!\nTo the South, \
            you can see the bedroom\n",
        [towel, soap],
        [None, None, 4, None]))

    # Room ID: 6
    # Room: Porch
    # Object List: Rocking Chair
    # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    room_list.append(Room(
        6,
        "Porch",
        "You are standing on the front porch, looking out to the \
            neighborhood in front of you. The fresh air feels good\
             on your furry face as you take in the sights around \
            you. Your favorite rocking chair is next to you on the\
             porch, with a light grey blanket draped over the back. \
            The gentle sound of wind chimes fills the air as a cool \
            breeze passes by you. \nTo the West, you can see the alley.\n\
            To the East, you can see the park where your friends are \
            waiting for you.\nTo the North, you can use the Front Door\
             to go to the living room.\nOn the South side of the porch \
            is a gutter that you can climb to the roof.\n"
        "You are standing on the front porch, looking out to the \
            neighborhood in front of you. Your favorite rocking chair \
            is next to you.\nTo the West, you can see the alley.\n\
            To the East, you can see the park where your friends are \
            waiting for you.\nTo the North, you can use the Front Door\
             to go to the living room.\nOn the South side of the porch \
            is a gutter that you can climb to the roof.\n",
        [rocking_chair],
        [0, 9, 8, 7]))

    # Room ID: 7
    # Room: Alley
    # Object List: Umbrella
    # Direction: [N: None, E: Porch, S: None, W: None]
    room_list.append(Room(
        7,
        "Alley",
        "You are standing in the dimly lit alley behind the house. The p\
            ower lines hang above your head, and your paws plod along the \
            cold pavement. You find yourself next to the trashcan, and find\
             a football helmet lying on its side. Behind the recycling bin,\
             you can see a small raccoon, covered in dirt. He seems to be \
            hiding something behind his back, and offers to make a trade if \
            you can help him get cleaned up.\nTo the East, you can see the \
            porch\n",
        "You are standing in the dimly lit alley behind the house. You find \
            yourself next to the trashcan, and find a football helmet lying \
            on its side. Behind the recycling bin, you can see a small \
            raccoon, covered in dirt. He seems to be hiding something \
            behind his back, and offers to make a trade if you can help him\
             get cleaned up.\nTo the East, you can see the porch\n",
        [umbrella],
        [None, 6, None, None]))

    # Room ID: 8
    # Room: Roof
    # Object List: ?
    # Direction: [N: Porch, E: None, S: None, W: None]
    room_list.append(Room(
        8,
        "Roof",
        "You find yourself standing on the roof of your one-story \
            house. You can see a pair of squirrels chasing each other\
             in the nearby branches. A small flock of hungry looking \
            birds circles overhead. Their simple nest is perched right\
             at the edge of the roof, looking comfortable enough for a \
            napping spot. \nTo the North, you can climb the gutter back \
            to the porch.\n",
        "You find yourself standing on the roof of your one-story \
            house. A simple nest is perched right\
             at the edge of the roof, looking comfortable enough for a \
            napping spot. \nTo the North, you can climb the gutter back \
            to the porch.\n",
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
    print(inventory)
    # current_room = room_list[0]

    # # move north
    # if current_room.north() is None:
    #     print("Cannot go north!")
    # else:
    #     current_room = room_list[current_room.north()]


if __name__ == "__main__":
    main()
