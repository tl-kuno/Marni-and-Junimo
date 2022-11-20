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
    file = open("rooms/living_room.p",'rb')


    # # Room ID: 1
    # # Room: Basement
    # # Object List: Mushrooms
    # # Feature List: Mouse, Suitcase
    # # Direction: [N: None, E: None , S: Living Room, W: None]
    file = open("rooms/basement.p",'rb')


    # # Room ID: 2
    # # Room: Kitchen
    # # Object List: Wooden Spoon, Blueberries
    # # Feature List: Refrigerator, Ants
    # # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    file = open("rooms/kitchen.p", "rb")


    # # Room ID: 3
    # # Room: Pantry
    # # Object List: Dog Treats
    # # Feature List: Shelves, Cleaning Supplies
    # # Direction: [N: None, E: None, S: Kitchen, W: None]
    file = open("rooms/pantry.p", "rb")


    # # Room ID: 4
    # # Room: Bedroom
    # # Object List: None
    # # Feature List: Blanket, Window
    # # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    file = open("rooms/bedroom.p", "rb")


    # # Room ID: 5
    # # Room: Bathroom
    # # Object List: Towel, Soap
    # # Feature List: Sink, Bathtub
    # # Direction: [N: None, E: None, S: Bedroom, W: None]
    file = open("rooms/bathroom.p", "rb")



    # # Room ID: 6
    # # Room: Porch
    # # Object List: None
    # # Feature List: Rocking Chair, Dirt pile
    # # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    file = open("rooms/porch.p", "rb")


    # # Room ID: 7
    # # Room: Alley
    # # Object List: Umbrella, Football Helmet
    # # Feature List: Raccoon, Guitar
    # # Direction: [N: None, E: Porch, S: None, W: None]
    file = open("rooms/alley.p", "rb")


    # # Room ID: 8
    # # Room: Roof
    # # Object List: None
    # # Feature List: Birds, neighborhood
    # # Direction: [N: Porch, E: None, S: None, W: None]
    file = open("rooms/roof.p", "rb")


    # # Room ID: 9
    # # Room: Park
    # # Object List: ?
    # # Feature List: Table, Friends
    # # Direction: [N: None, E: None, S: None, W: Porch]
    # # TODO: implement a final game state, based on items acquired
    file = open("rooms/park.p", "rb")

    # ------

    unpickled_living_room = pickle.load(file)
    unpickled_basement = pickle.load(file)
    unpickled_kitchen = pickle.load(file)
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
    room_list.append(unpickled_kitchen)
    room_list.append(unpicked_pantry)
    room_list.append(unpickled_bedroom)
    room_list.append(unpickled_bathroom)
    room_list.append(unpickled_porch)
    room_list.append(unpickled_alley)
    room_list.append(unpickled_roof)
    room_list.append(unpickled_park)

    return room_list
