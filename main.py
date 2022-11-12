from room import Room
from item import Item
from character import Character
from messages import messages
from feature import Feature
from nav import Direction
from verb import VerbClass, verb_dict


def newgame():
    # this is where we do all of the things!!!
    # placeholder return statement, but the server
    # is expecting a returned string
    return messages['intro']


def handle_user_input(command):     # noqa: C901
    command = command.strip().lower()
    if command == "inv":
        return player.show_inventory()
    # "grab red scarf" --> ["grab", "red scarf"]
    input_components = command.split(maxsplit=1)
    verb = input_components[0]
    if len(input_components) > 1:
        noun = input_components[1].strip()

    # determine our verb class
    verb_class = -1
    if verb not in verb_dict:
        # check if this is one of our exits or directions
        if command not in player.location.direction_dict:
            return "invalid command, try again..."
        verb_class = VerbClass.MOVE_PRIME
    else:
        verb_class = verb_dict[verb]    # returns verb_class enum

    # handle each verb class
    if verb_class == VerbClass.MOVE:
        return player.move(noun, room_list)
    if verb_class == VerbClass.MOVE_PRIME:
        return player.move(command, room_list)
    if verb_class == VerbClass.TAKE:
        return player.take(noun)
    if verb_class == VerbClass.DROP:
        return player.drop(noun)
    if verb_class == VerbClass.EAT:
        # return player.eat(noun)
        pass
    if verb_class == VerbClass.READ:
        # return player.read(noun)
        pass
    if verb_class == VerbClass.NAP:
        # return player.nap(noun)
        pass
    if verb_class == VerbClass.SCRATCH:
        # return player.scratch(noun)
        pass
    if verb_class == VerbClass.USE:
        return player.use(noun)
    if verb_class == VerbClass.INVITE:
        # return player.invite(noun)
        pass
    if verb_class == VerbClass.TALK:
        # return player.talk(noun)
        pass
    if verb_class == VerbClass.WEAR:
        # return player.wear(noun)
        pass
    if verb_class == VerbClass.LISTEN:
        # return player.listen(noun)
        pass
    if verb_class == VerbClass.LOOK:
        return player.location.long_description

    return "verb [{}] not yet supported...".format(verb)


def init_room_list_and_items():
    # list of all the rooms
    room_list = []

    # -----------------------------------------------------
    # -                      Create Items                 -
    # -----------------------------------------------------

    # Item Name: Blueberries
    # Can Pick Up: Yes
    # Can Drop: Yes
    blueberries = Item("blueberries",
                       messages['blueberries'],
                       True,
                       True)

    # Item Name: Mushrooms
    # Can Pick Up: Yes
    # Can Drop: Yes
    mushrooms = Item("mushrooms",
                     messages['mushrooms'],
                     True,
                     True)

    # Item Name: Dog Treats
    # Can Pick Up: Yes
    # Can Drop: Yes
    dog_treats = Item("dog treats",
                      messages['dog treats'],
                      True,
                      True)

    # Item Name: Towel
    # Can Pick Up: Yes
    # Can Drop: Yes
    towel = Item("towel",
                 messages['towel'],
                 True,
                 True)

    # Item Name: Umbrella
    # Can Pick Up: Yes
    # Can Drop: Yes
    umbrella = Item("umbrella",
                    messages['umbrella'],
                    True,
                    True)

    # Item Name: Letter
    # Can Pick Up: Yes
    # Can Drop: Yes
    letter = Item("letter",
                  messages['letter'],
                  True,
                  True)

    # Item Name: Wooden Spoon
    # Can Pick Up: Yes
    # Can Drop: Yes
    wooden_spoon = Item("wooden spoon",
                        messages['wooden spoon'],
                        True,
                        True)

    # Item Name: Football Helmet
    # Can Pick Up: Yes
    # Can Drop: Yes
    football_helmet = Item("football helmet",
                           messages['football helmet'],
                           True,
                           True)

    # Item Name: Soap
    # Can Pick Up: Yes
    # Can Drop: Yes
    soap = Item("soap",
                messages['soap'],
                True,
                True)

    # Item Name: Flashlight
    # Can Pick Up: Yes
    # Can Drop: Yes
    flashlight = Item("flashlight",
                      messages['flashlight'],
                      True,
                      True)

    # -----------------------------------------------------
    # -                      Create Features               -
    # -----------------------------------------------------

    # Feature Name: Sofa
    sofa = Feature("sofa", messages['sofa'])

    # Feature Name: TV
    tv = Feature("tv", messages['tv'])

    # Feature Name: Mouse
    mouse = Feature("mouse", messages['mouse'])

    # Feature Name: Suitcase
    suitcase = Feature("suitcase", messages['suitcase'])

    # Feature Name: Refrigerator
    refrigerator = Feature("refrigerator", messages['refrigerator'])

    # Feature Name: Ants
    ants = Feature("ants", messages['ants'])

    # Feature Name: shelves
    shelves = Feature("shelves", messages['shelves'])

    # Feature Name: Treat bin
    cleaning_supplies = Feature("Cleaning Supplies",
                                messages['cleaning supplies'])

    # Feature Name: Blanket
    blanket = Feature("blanket", messages['blanket'])

    # Feature Name: window
    window = Feature("window", messages['window'])

    # Feature Name: sink
    sink = Feature("sink", messages['sink'])

    # Feature Name: bathtub
    bathtub = Feature("bathtub", messages['bathtub'])

    # Feature Name: Rocking Chair
    rocking_chair = Feature("rocking chair", messages['rocking chair'])

    # Feature Name: Dirt pile
    dirt_pile = Feature("dirt pile", messages['dirt pile'])

    # Feature Name: Raccoon
    raccoon = Feature("raccoon", messages['raccoon'])

    # Feature Name: Guitar
    guitar = Feature("guitar", messages['guitar'])

    # Feature Name: Birds
    birds = Feature("birds", messages['birds'])

    # Feature Name: Neighborhood
    neighborhood = Feature("neighborhood", messages['neighborhood'])

    # Feature Name: Table
    table = Feature("table", messages['table'])

    # Feature Name: Friends
    # TODO write a func to give result based on collected items & animals??
    friends = Feature("friends",
                      "END GAME!")

    # -----------------------------------------------------
    # -                     Create Rooms                  -
    # -----------------------------------------------------

    # Room ID: 0
    # Room: Living Room
    # Object List: Flashlight, Letter
    # Feature List: Sofa, TV
    # Direction: [N: Basement, E: Bedroom , S: Porch, W: Kitchen]
    # Custom Exit: smelly staircase
    room_list.append(Room(
        0,
        "Living Room",
        messages["living room.long"],
        messages["living room.short"],
        [flashlight, letter],
        [sofa, tv],
        [1, 4, 6, 2],
        {
            "creaky wooden stairs": Direction.NORTH,
            "creaky stairs": Direction.NORTH,
            "wooden stairs": Direction.NORTH,
            "stairs": Direction.NORTH,
            "creaky wooden staircase": Direction.NORTH,
            "creaky staircase": Direction.NORTH,
            "wooden staircase": Direction.NORTH,
            "staircase": Direction.NORTH
        }))

    # Room ID: 1
    # Room: Basement
    # Object List: Mushrooms
    # Feature List: Mouse, Suitcase
    # Direction: [N: None, E: None , S: Living Room, W: None]
    room_list.append(Room(
        1,
        "Basement",
        messages["basement.long"],
        messages["basement.short"],
        [mushrooms],
        [mouse, suitcase],
        [None, None, 0, None],
        {
            "creaky wooden stairs": Direction.SOUTH,
            "creaky stairs": Direction.SOUTH,
            "wooden stairs": Direction.SOUTH,
            "stairs": Direction.SOUTH,
            "creaky wooden staircase": Direction.SOUTH,
            "creaky staircase": Direction.SOUTH,
            "wooden staircase": Direction.SOUTH,
            "staircase": Direction.SOUTH
        }))

    # Room ID: 2
    # Room: Kitchen
    # Object List: Wooden Spoon, Blueberries
    # Feature List: Refrigerator, Ants
    # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    room_list.append(Room(
        2,
        "Kitchen",
        messages["kitchen.long"],
        messages["kitchen.short"],
        [wooden_spoon, blueberries],
        [refrigerator, ants],
        [3, 0, None, None]))

    # Room ID: 3
    # Room: Pantry
    # Object List: Dog Treats
    # Feature List: Shelves, Cleaning Supplies
    # Direction: [N: None, E: None, S: Kitchen, W: None]
    room_list.append(Room(
        3,
        "Pantry",
        messages["pantry.long"],
        messages["pantry.short"],
        [dog_treats],
        [shelves, cleaning_supplies],
        [None, None, 2, None]))

    # Room ID: 4
    # Room: Bedroom
    # Object List: None
    # Feature List: Blanket, Window
    # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    room_list.append(Room(
        4,
        "Bedroom",
        messages["bedroom.long"],
        messages["bedroom.short"],
        [],
        [blanket, window],
        [5, None, None, 0]))

    # Room ID: 5
    # Room: Bathroom
    # Object List: Towel, Soap
    # Feature List: Sink, Bathtub
    # Direction: [N: None, E: None, S: Bedroom, W: None]
    room_list.append(Room(
        5,
        "Bathroom",
        messages["bathroom.long"],
        messages["bathroom.short"],
        [towel, soap],
        [sink, bathtub],
        [None, None, 4, None]))

    # Room ID: 6
    # Room: Porch
    # Object List: None
    # Feature List: Rocking Chair, Dirt pile
    # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    room_list.append(Room(
        6,
        "Porch",
        messages["porch.long"],
        messages["porch.short"],
        [],
        [rocking_chair, dirt_pile],
        [0, 9, 8, 7]))

    # Room ID: 7
    # Room: Alley
    # Object List: Umbrella, Football Helmet
    # Feature List: Raccoon, Guitar
    # Direction: [N: None, E: Porch, S: None, W: None]
    room_list.append(Room(
        7,
        "Alley",
        messages["alley.long"],
        messages["alley.short"],
        [umbrella, football_helmet],
        [raccoon, guitar],
        [None, 6, None, None]))

    # Room ID: 8
    # Room: Roof
    # Object List: None
    # Feature List: Birds, neighborhood
    # Direction: [N: Porch, E: None, S: None, W: None]
    room_list.append(Room(
        8,
        "Roof",
        messages["roof.long"],
        messages["roof.short"],
        [],
        [birds, neighborhood],
        [6, None, None, None]))

    # Room ID: 9
    # Room: Park
    # Object List: ?
    # Feature List: Table, Friends
    # Direction: [N: None, E: None, S: None, W: Porch]
    # TODO: implement a final game state, based on items acquired
    room_list.append(Room(
        9,
        "Park",
        messages["park.long"],
        messages["park.short"],
        [],
        [table, friends],
        [None, None, None, 6]))
    return room_list


def main():
    """
    Main function
    """
    # stores items picked up in inventory
    # inventory = []

    # for room in room_list:
    #     print(room.long_description)
    # print(inventory)

    while True:
        response = input("Enter instructions: ").lower()
        if "quit" in response:
            print("\nThanks for playing. Quitting...\n")
            break
        print()
        print(handle_user_input(response))


room_list = init_room_list_and_items()
player = Character("Player 1", location=room_list[0])

if __name__ == "__main__":
    main()
