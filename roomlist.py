from room import Room
from item import Item
from feature import Feature
from nav import Direction
from messages import messages
import pickle

def init_room_list_and_items():
    # list of all the rooms
    room_list = []

    # -----------------------------------------------------
    # -                      Create Items                 -
    # -----------------------------------------------------

    # Item Name: Blueberries
    blueberries = Item("blueberries",
                       messages['blueberries'])

    # Item Name: Mushrooms
    mushrooms = Item("mushrooms",
                     messages['mushrooms'])

    # Item Name: Dog Treats
    dog_treats = Item("dog treats",
                      messages['dog treats'])

    # Item Name: Towel
    towel = Item("towel",
                 messages['towel'])

    # Item Name: Umbrella
    umbrella = Item("umbrella",
                    messages['umbrella'])

    # Item Name: Letter
    letter = Item("letter",
                  messages['letter'])

    # Item Name: Wooden Spoon
    wooden_spoon = Item("wooden spoon",
                        messages['wooden spoon'])

    # Item Name: Football Helmet
    football_helmet = Item("football helmet",
                           messages['football helmet'])

    # Item Name: Soap
    soap = Item("soap",
                messages['soap'])

    # Item Name: Flashlight
    flashlight = Item("flashlight",
                      messages['flashlight'])

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

    # # -----------------------------------------------------
    # # -                     Create Rooms                  -
    # # -----------------------------------------------------

    # # Room ID: 0
    # # Room: Living Room
    # # Object List: Flashlight, Letter
    # # Feature List: Sofa, TV
    # # Direction: [N: Basement, E: Bedroom , S: Porch, W: Kitchen]
    # # Custom Exit: smelly staircase
    living_room = Room(
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
            "staircase": Direction.NORTH,
            "kitchen": Direction.WEST,
            "bedroom": Direction.EAST,
            "basement": Direction.NORTH,
            "porch": Direction.SOUTH
        })

    # # Room ID: 1
    # # Room: Basement
    # # Object List: Mushrooms
    # # Feature List: Mouse, Suitcase
    # # Direction: [N: None, E: None , S: Living Room, W: None]
    basement = Room(
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
            "staircase": Direction.SOUTH,
            "living room": Direction.SOUTH
        })

    # # Room ID: 2
    # # Room: Kitchen
    # # Object List: Wooden Spoon, Blueberries
    # # Feature List: Refrigerator, Ants
    # # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    kitchen = Room(
        2,
        "Kitchen",
        messages["kitchen.long"],
        messages["kitchen.short"],
        [wooden_spoon, blueberries],
        [refrigerator, ants],
        [3, 0, None, None],
        {
            "pantry": Direction.NORTH,
            "living room": Direction.EAST
        })

    # # Room ID: 3
    # # Room: Pantry
    # # Object List: Dog Treats
    # # Feature List: Shelves, Cleaning Supplies
    # # Direction: [N: None, E: None, S: Kitchen, W: None]
    pantry = Room(
        3,
        "Pantry",
        messages["pantry.long"],
        messages["pantry.short"],
        [dog_treats],
        [shelves, cleaning_supplies],
        [None, None, 2, None],
        {
            "kitchen": Direction.SOUTH
        })

    # # Room ID: 4
    # # Room: Bedroom
    # # Object List: None
    # # Feature List: Blanket, Window
    # # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    bedroom = Room(
        4,
        "Bedroom",
        messages["bedroom.long"],
        messages["bedroom.short"],
        [],
        [blanket, window],
        [5, None, None, 0],
        {
            "living room": Direction.WEST,
            "bathroom": Direction.NORTH
        })

    # # Room ID: 5
    # # Room: Bathroom
    # # Object List: Towel, Soap
    # # Feature List: Sink, Bathtub
    # # Direction: [N: None, E: None, S: Bedroom, W: None]
    bathroom = Room(
        5,
        "Bathroom",
        messages["bathroom.long"],
        messages["bathroom.short"],
        [towel, soap],
        [sink, bathtub],
        [None, None, 4, None],
        {
            "bedroom": Direction.SOUTH
        })

    # # Room ID: 6
    # # Room: Porch
    # # Object List: None
    # # Feature List: Rocking Chair, Dirt pile
    # # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    porch = Room(
        6,
        "Porch",
        messages["porch.long"],
        messages["porch.short"],
        [],
        [rocking_chair, dirt_pile],
        [0, 9, 8, 7],
        {
            "living room": Direction.NORTH,
            "park": Direction.EAST,
            "roof": Direction.SOUTH,
            "alley": Direction.WEST
        })

    # # Room ID: 7
    # # Room: Alley
    # # Object List: Umbrella, Football Helmet
    # # Feature List: Raccoon, Guitar
    # # Direction: [N: None, E: Porch, S: None, W: None]
    alley = Room(
        7,
        "Alley",
        messages["alley.long"],
        messages["alley.short"],
        [umbrella, football_helmet],
        [raccoon, guitar],
        [None, 6, None, None],
        {
            "porch": Direction.EAST
        })

    # # Room ID: 8
    # # Room: Roof
    # # Object List: None
    # # Feature List: Birds, neighborhood
    # # Direction: [N: Porch, E: None, S: None, W: None]
    roof = Room(
        8,
        "Roof",
        messages["roof.long"],
        messages["roof.short"],
        [],
        [birds, neighborhood],
        [6, None, None, None],
        {
            "porch": Direction.NORTH
        })

    # # Room ID: 9
    # # Room: Park
    # # Object List: ?
    # # Feature List: Table, Friends
    # # Direction: [N: None, E: None, S: None, W: Porch]
    # # TODO: implement a final game state, based on items acquired
    park = Room(
        9,
        "Park",
        messages["park.long"],
        messages["park.short"],
        [],
        [table, friends],
        [None, None, None, 6])

    # ------

    filehandler = open("rooms/living_room.p", "wb")
    filehandler = open("rooms/basement.p", "wb")
    filehandler = open("rooms/pantry.p", "wb")
    filehandler = open("rooms/bedroom.p", "wb")
    filehandler = open("rooms/bathroom.p", "wb")
    filehandler = open("rooms/porch.p", "wb")
    filehandler = open("rooms/alley.p", "wb")
    filehandler = open("rooms/roof.p", "wb")
    filehandler = open("rooms/park.p", "wb")

    pickle.dump(living_room, filehandler)
    pickle.dump(basement, filehandler)
    pickle.dump(pantry, filehandler)
    pickle.dump(bedroom, filehandler)
    pickle.dump(bathroom, filehandler)
    pickle.dump(porch, filehandler)
    pickle.dump(alley, filehandler)
    pickle.dump(roof, filehandler)
    pickle.dump(park, filehandler)

    filehandler.close()

    file = open("rooms/living_room.p",'rb')
    file = open("rooms/basement.p",'rb')
    file = open("rooms/pantry.p", "rb")
    file = open("rooms/bedroom.p", "rb")
    file = open("rooms/bathroom.p", "rb")
    file = open("rooms/porch.p", "rb")
    file = open("rooms/alley.p", "rb")
    file = open("rooms/roof.p", "rb")
    file = open("rooms/park.p", "rb")

    unpickled_living_room = pickle.load(file)
    unpickled_basement = pickle.load(file)
    unpicked_pantry = pickle.load(file)
    unpickled_bedroom = pickle.load(file)
    unpickled_bathroom = pickle.load(file)
    unpickled_porch = pickle.load(file)
    unpickled_alley = pickle.load(file)
    unpickled_roof = pickle.load(file)
    unpickled_park = pickle.load(file)

    file.close()

    room_list.append(unpickled_living_room)
    room_list.append(unpickled_basement)
    room_list.append(unpicked_pantry)
    room_list.append(unpickled_bedroom)
    room_list.append(unpickled_bathroom)
    room_list.append(unpickled_porch)
    room_list.append(unpickled_alley)
    room_list.append(unpickled_roof)
    room_list.append(unpickled_park)

    print(room_list)

init_room_list_and_items()