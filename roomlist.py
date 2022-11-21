import pickle


def init_room_list_and_items():
    # list of all the rooms
    room_list = []

    # # -----------------------------------------------------
    # # -                     Open Rooms                    -
    # # -----------------------------------------------------

    # # Room ID: 0
    # # Room: Living Room
    # # Object List: Flashlight, Letter
    # # Feature List: Sofa, TV
    # # Direction: [N: Basement, E: Bedroom , S: Porch, W: Kitchen]
    # # Custom Exit: smelly staircase
    p_lr = open("living_room.p", "rb")
    unpickled_living_room = pickle.load(p_lr)
    p_lr.close()

    # # Room ID: 1
    # # Room: Basement
    # # Object List: Mushrooms
    # # Feature List: Mouse, Suitcase
    # # Direction: [N: None, E: None , S: Living Room, W: None]
    p_base = open("basement.p", "rb")
    unpickled_basement = pickle.load(p_base)
    p_base.close()

    # # Room ID: 2
    # # Room: Kitchen
    # # Object List: Wooden Spoon, Blueberries
    # # Feature List: Refrigerator, Ants
    # # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    p_kit = open("kitchen.p", "rb")
    unpicked_kitchen = pickle.load(p_kit)
    p_kit.close()

    # # Room ID: 3
    # # Room: Pantry
    # # Object List: Dog Treats
    # # Feature List: Shelves, Cleaning Supplies
    # # Direction: [N: None, E: None, S: Kitchen, W: None]
    p_pan = open("pantry.p", "rb")
    unpicked_pantry = pickle.load(p_pan)
    p_pan.close()

    # # Room ID: 4
    # # Room: Bedroom
    # # Object List: None
    # # Feature List: Blanket, Window
    # # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    p_bed = open("bedroom.p", "rb")
    unpickled_bedroom = pickle.load(p_bed)
    p_bed.close()

    # # Room ID: 5
    # # Room: Bathroom
    # # Object List: Towel, Soap
    # # Feature List: Sink, Bathtub
    # # Direction: [N: None, E: None, S: Bedroom, W: None]
    p_bath = open("bathroom.p", "rb")
    unpickled_bathroom = pickle.load(p_bath)
    p_bath.close()

    # # Room ID: 6
    # # Room: Porch
    # # Object List: None
    # # Feature List: Rocking Chair, Dirt pile
    # # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    p_por = open("porch.p", "rb")
    unpickled_porch = pickle.load(p_por)
    p_por.close()

    # # Room ID: 7
    # # Room: Alley
    # # Object List: Umbrella, Football Helmet
    # # Feature List: Raccoon, Guitar
    # # Direction: [N: None, E: Porch, S: None, W: None]
    p_all = open("alley.p", "rb")
    unpickled_alley = pickle.load(p_all)
    p_all.close()

    # # Room ID: 8
    # # Room: Roof
    # # Object List: None
    # # Feature List: Birds, neighborhood
    # # Direction: [N: Porch, E: None, S: None, W: None]
    p_roof = open("roof.p", "rb")
    unpickled_roof = pickle.load(p_roof)
    p_roof.close()

    # # Room ID: 9
    # # Room: Park
    # # Object List: ?
    # # Feature List: Table, Friends
    # # Direction: [N: None, E: None, S: None, W: Porch]
    # # TODO: implement a final game state, based on items acquired
    p_park = open("park.p", "rb")
    unpickled_park = pickle.load(p_park)
    p_park.close()

    # # -----------------------------------------------------
    # # -              Append Room Lists                    -
    # # -----------------------------------------------------

    room_list.append(unpickled_living_room)
    room_list.append(unpickled_basement)
    room_list.append(unpicked_kitchen)
    room_list.append(unpicked_pantry)
    room_list.append(unpickled_bedroom)
    room_list.append(unpickled_bathroom)
    room_list.append(unpickled_porch)
    room_list.append(unpickled_alley)
    room_list.append(unpickled_roof)
    room_list.append(unpickled_park)

    return room_list
