from room import Room
from item import Item
from character import Character
from messages import messages
from feature import Feature


def newgame():
    # this is where we do all of the things!!!
    # placeholder return statement, but the server
    # is expecting a returned string
    return "intro string here"


def handle_user_input(command):
    room_list = init_room_list_and_items()
    player = Character("Player 1", location=room_list[0])
    resp_object = check_and_move(command, player.location, room_list)
    output = resp_object.short_description
    return output


def move(direction, current_room, room_list):
    direction = direction.lower()
    if direction == "north":
        # move north
        if current_room.north() is None:
            print("Cannot go north!")
        else:
            current_room = room_list[current_room.north()]
        return current_room
    elif direction == "east":
        # move north
        if current_room.east() is None:
            print("Cannot go east!")
        else:
            current_room = room_list[current_room.east()]
        return current_room
    elif direction == "south":
        # move north
        if current_room.south() is None:
            print("Cannot go south!")
        else:
            current_room = room_list[current_room.south()]
        return current_room
    elif direction == "west":
        # move north
        if current_room.west() is None:
            print("Cannot go west!")
        else:
            current_room = room_list[current_room.west()]
        return current_room
    print("Invalid direction")
    return current_room


def check_and_move(response, cur_room, room_list):
    response = response.lower()
    # finds the first index of the term 'move' if it exists, else -1
    movement_verb = "move"
    idx = response.find(movement_verb)
    if idx != -1:
        # removes everything in the user input
        # up to and including the word 'move'
        direction = response[idx + len(movement_verb):]
        # removes all words after the direction
        direction = direction.split()[0]
        # removes surrounding white space
        direction = direction.strip()
        # print("[{}]".format(direction))
        cur_room = move(direction, cur_room, room_list)
    return cur_room


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
                                messages['cleaning_supplies'])

    # Feature Name: Blanket
    blanket = Feature("blanket", messages['blanket'])

    # Feature Name: window
    window = Feature("window", messages['window'])

    # Feature Name: sink
    sink = Feature("sink", messages['sink'])

    # Feature Name: bathtub
    bathtub = Feature("bathtub", messages['bathtub'])

    # Feature Name: Rocking Chair
    rocking_chair = Feature("rocking chair", messages['rocking_chair'])

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
    room_list.append(Room(
        0,
        "Living Room",
        messages["living room.long"],
        messages["living room.short"],
        [flashlight, letter],
        [sofa, tv],
        [1, 4, 6, 2]))

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
        [None, None, 0, None]))

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

    room_list = init_room_list_and_items()
    cur_room = room_list[0]
    print(cur_room)
    while True:
        response = input("Enter instructions: ").lower()
        if "quit" in response:
            print("\nThanks for playing. Quitting...\n")
            break
        cur_room = check_and_move(response, cur_room, room_list)
        print(cur_room)


if __name__ == "__main__":
    main()
