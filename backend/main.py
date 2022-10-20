from Room import Room
from Item import Item


def test_function(command):
    num_chars = "odd"
    if len(command) % 2 == 0:
        num_chars = "even"
    output = "Your string has an " + num_chars + " number of characters"
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
    blueberries = Item("Blueberries",
                       "These blueberries were freshly picked yesterday from"
                       " the Johnson Family Blueberry Orchard. These will make"
                       " an amazing addition to the picnic!\n",
                       True,
                       True)

    # Item Name: Mushrooms
    # Can Pick Up: Yes
    # Can Drop: Yes
    mushrooms = Item("Mushrooms", "These fresh mushrooms must have "
                     "been growing in the dark cool basement for months. They"
                     "are almost as large as your head! They will taste "
                     "amazing at a picnic.\n",
                     True,
                     True)

    # Item Name: Dog Treats
    # Can Pick Up: Yes
    # Can Drop: Yes
    dog_treats = Item("Dog Treats", "Groovy Snacks Dog Treats are some "
                      "of your absolute favorites. These ones are chicken "
                      "& bacon flavored. They're the perfect crunchy, savory "
                      "treat for a sunny picnic.\n",
                      True,
                      True)

    # Item Name: Towel
    # Can Pick Up: Yes
    # Can Drop: Yes
    towel = Item("Towel",
                 "This light blue towel is freshly washed, and smells like"
                 " lemon and lavender. It's the same color as the clear blue"
                 " sky outside, and would work well as a picnic blanket for "
                 "today.\n",
                 True,
                 True)

    # Item Name: Umbrella
    # Can Pick Up: Yes
    # Can Drop: Yes
    umbrella = Item("Umbrella",
                    "This simple yellow umbrella looks like a rubber duck when"
                    " it's opened. It's cute and lightweight, but will easily "
                    "keep the sun off of you at a picnic.\n",
                    True,
                    True)

    # Item Name: Letter
    # Can Pick Up: Yes
    # Can Drop: Yes
    letter = Item("Letter",
                  "This letter is written in the familiar handwriting "
                  "of your best friend, Junimo. It reads \n\"Good morning"
                  " Marnie! I hope you had a great nap! The day is beautiful "
                  "outside, and I've decided to throw a picnic! You are "
                  "cordially invited to join us at Henderson Park this "
                  "afternoon. Everybody is asked to bring three different"
                  " snacks, a picnic blanket, and an umbrella. (If you're "
                  "unable to find everything, that's OK too!)\nYour friend"
                  ",\nJunimo the cat\n",
                  True,
                  True)

    # Item Name: Wooden Spoon
    # Can Pick Up: Yes
    # Can Drop: Yes
    wooden_spoon = Item("Wooden Spoon",
                        "This sturdy wooden spoon is rarely used by the "
                        "humans here. It looks really strong though, "
                        "and could probably be useful for propping something"
                        " open.\n",
                        True,
                        True)

    # Item Name: Football Helmet
    # Can Pick Up: Yes
    # Can Drop: Yes
    football_helmet = Item("Football Helmet",
                           "This old, beaten up football helmet is "
                           "much too small for the humans in the house to "
                           "wear anymore. It could pretty easily fit on your "
                           "head though! It would be really helpful to use"
                           " this to push open a stuck door.\n",
                           True,
                           True)

    # Item Name: Soap
    # Can Pick Up: Yes
    # Can Drop: Yes
    soap = Item("Soap",
                "This bar of handsoap has a bright scent of orange citrus"
                ". This would be really useful to clean up an animal after"
                " a day of playing in dirt.\n",
                True,
                True)

    # Item Name: Flashlight
    # Can Pick Up: Yes
    # Can Drop: Yes
    flashlight = Item("Flashlight",
                      "This old clunky flashlight still works,despite "
                      "not having been used in many months. The batteries "
                      "are still in good condition, and the light is bright"
                      " enough to illuminate any dark spaces around the "
                      "house.",
                      True,
                      True)

    # Item Name: Rocking Chair
    # Can Pick Up: No
    # Can Drop: No
    rocking_chair = Item("Rocking Chair",
                         "This is the human's favorite rocking chair. It has"
                         " a strong wooden frame and a well worn but "
                         "comfortable blue cushion. There's a warm wool"
                         " blanket draped over the back for any chilly "
                         "evenings.\n",
                         False,
                         False)

    # -----------------------------------------------------
    # -                     Create Rooms                  -
    # -----------------------------------------------------

    # Room ID: 0
    # Room: Living Room
    # Object List: Flashlight, Letter
    # Direction: [N: Basement, E: Bedroom , S: Porch, W: Kitchen]
    room_list.append(Room(
        0,
        "Living Room",
        "You are in a warm, cozy living room. Sunlight pours through the "
        "windows, lighting up familiar sofa in the center of the room. "
        "There are no signs of humans around here, just the soft sound "
        "of the trees rustling in the breeze outside. You stretch your "
        "paws and arch your back, slowly waking up from a relaxing nap. "
        "You suddenly realize that a letter has been placed on "
        "the pillow in front of you.\nTo the North of you, you can see "
        "the door to the basement.\nTo the East, you can see the closed"
        " door to the bedroom.\nTo the South, you can see the front door"
        " that leads to the porch outside.\nTo the West, you see the"
        " doorway to the kitchen.\n",
        "You are in the comfortable living room in the center of the house. "
        "A large comfortable sofa sits in the center of the room.\n"
        "To the North of you, you can see the door to the basement."
        "\nTo the East, you can see the closed door to the bedroom."
        "\nTo the South, you can see the front door that leads to "
        "the porch outside.\nTo the West, you see the doorway to "
        "the kitchen.\n",
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
        "You make your way down the creaky wooden stairs into the "
        "cold basement. Cobwebs line the handrail as you decend "
        "into the dimly lit room. "
        "The humans clearly don't come down here very often. "
        "Beneath the stairs you can smell the distinct scent of ripe, "
        "delicious violet mushrooms. These would be an excellent snack "
        "for your friends at the picnic!\nThe only way out of the basement"
        " is South, which takes you back to the Living Room.\n",
        "The cold, dark basement is eerily quiet. Only a small amount of light"
        " peeks in from the doorway upstairs. Beneath the stairway a patch "
        "of ripe, tasty mushrooms are growing. \nThe only way out of the "
        "basement is South, back to the living room.\n",
        [mushrooms],
        [None, None, 0, None]))

    # Room ID: 2
    # Room: Kitchen
    # Object List: Wooden Spoon, Blueberries
    # Direction: [N: Pantry, E: Living Room, S: None, W: None]
    room_list.append(Room(
        2,
        "Kitchen",
        "You stand in the brightly lit kitchen. The white tile floor glistens "
        "brightly, and rumbling sound of the running dishwasher fills the "
        "room. The humans must have been clumsy earlier, because a thick "
        "wooden ladle has rolled under the table in the center of the room."
        " On the sleek marble countertops, you can see the corner of a "
        "plastic container of scrumptious, freshly picked blueberries! "
        "These would be perfect for a picnic!\nThe door to the pantry is"
        " ajar to the North of you.\nThe open doorway to the living room "
        "is to the East.\n",
        "You find yourself in the brightly lit kitchen. \nTo the North, you "
        "can see the pantry door.\nTo the East, you can see the doorway to "
        "the living room.\n",
        [wooden_spoon, blueberries],
        [3, 0, None, None]))

    # Room ID: 3
    # Room: Pantry
    # Object List: Dog Treats
    # Direction: [N: None, E: None, S: Kitchen, W: None]
    room_list.append(Room(
        3,
        "Pantry",
        "You stand in the well-stocked pantry, looking at shelves packed "
        "floor to ceiling with human food. Boxes of Poptarts and other "
        "processed food sit on the middle shelves, but these are no good"
        " for animals to eat. There"
        " are plenty of dried food in tricky jars and tupperware that would"
        " be impossible to get into without thumbs. Luckily, there is a "
        "cabinet full of yummy kibble situated on the bottom shelf in front "
        "of you The door is really heavy, and swings closed quickly. You "
        "will need something strong to prop it open in order to stock up on"
        " the tasty snacks.\nTo the "
        "South, you can see the kitchen.\n",
        "You stand in the well-stocked pantry, looking at shelves packed floor"
        " to ceiling with human food. There is a bin full of kibble on the "
        "bottom shelf in front of you. \nTo the South, you can see the "
        "kitchen.\n",
        [dog_treats],
        [None, None, 2, None]))

    # Room ID: 4
    # Room: Bedroom
    # Object List: Football Helmet
    # Direction: [N: Bathroom, E: None, S: None, W: Living Room]
    room_list.append(Room(
        4,
        "Bedroom",
        "You stand in the human's bedroom, at the foot of their mattress. "
        "Framed photos of smiling humans are hung up on each wall. A "
        "sunbeam cuts through the window, highlighting a tempting "
        "napping spot in the balled up, fuzzy green blanket on the "
        "human's bed. You can hear the sound of birds chirping from "
        "right outside. \nTo the North, you can see the open doorway "
        "to the bathroom.\n",
        "You are in the bedroom. A sunny spot on the bed looks like the "
        "perfect location to take a nice long mid-day nap. To the "
        "North, you can see the open doorway to the bathroom.\n",
        [football_helmet],
        [5, None, None, 0]))

    # Room ID: 5
    # Room: Bathroom
    # Object List: Towel, Soap
    # Direction: [N: None, E: None, S: Bedroom, W: None]
    room_list.append(Room(
        5,
        "Bathroom",
        "You stand in the well-maintained bathroom. Blue and green tiles line"
        " the floor, and you can smell citrus-scented cleaners that the "
        "humans used this morning. The drip-drip-drip sound of the sink "
        "echos in the small room. On the side of the bathtub you can see "
        "a bar of fresh, unscented soap. Hanging on a nearby rack is a "
        "red-and-white checkered towel, which would look amazing as a "
        "picnic blanket!\nTo the South, you can see the bedroom\n",
        "You stand in the clean bathroom. You can see a bar of soap on the "
        "side of the bathtub. There is a checkered towel hanging on a rack,"
        " which would look amazing as a picnic blanket!\nTo the South, "
        "you can see the bedroom\n",
        [towel, soap],
        [None, None, 4, None]))

    # Room ID: 6
    # Room: Porch
    # Object List: Rocking Chair
    # Direction: [N: Living Room, E: Park, S: Roof, W: Alley]
    room_list.append(Room(
        6,
        "Porch",
        "You are standing on the front porch, looking out to the "
        "neighborhood in front of you. The fresh air feels good"
        " on your furry face as you take in the sights around "
        "you. Your favorite rocking chair is next to you on the"
        " porch, with a light grey blanket draped over the back. "
        "The gentle sound of wind chimes fills the air as a cool "
        "breeze passes by you. \nTo the West, you can see the alley.\n"
        "To the East, you can see the park where your friends are "
        "waiting for you.\nTo the North, you can use the Front Door"
        " to go to the living room.\nOn the South side of the porch "
        "is a gutter that you can climb to the roof.\n",
        "You are standing on the front porch, looking out to the "
        "neighborhood in front of you. Your favorite rocking chair "
        "is next to you.\nTo the West, you can see the alley.\n"
        "To the East, you can see the park where your friends are "
        "waiting for you.\nTo the North, you can use the Front Door"
        " to go to the living room.\nOn the South side of the porch "
        "is a gutter that you can climb to the roof.\n",
        [rocking_chair],
        [0, 9, 8, 7]))

    # Room ID: 7
    # Room: Alley
    # Object List: Umbrella
    # Direction: [N: None, E: Porch, S: None, W: None]
    room_list.append(Room(
        7,
        "Alley",
        "You are standing in the dimly lit alley behind the house. The p"
        "ower lines hang above your head, and your paws plod along the "
        "cold pavement. You find yourself next to the trashcan, and find"
        " a football helmet lying on its side. Behind the recycling bin,"
        " you can see a small raccoon, covered in dirt. He seems to be "
        "hiding something behind his back, and offers to make a trade if "
        "you can help him get cleaned up.\nTo the East, you can see the "
        "porch\n",
        "You are standing in the dimly lit alley behind the house. You find "
        "yourself next to the trashcan, and find a football helmet lying "
        "on its side. Behind the recycling bin, you can see a small "
        "raccoon, covered in dirt. He seems to be hiding something "
        "behind his back, and offers to make a trade if you can help him"
        " get cleaned up.\nTo the East, you can see the porch\n",
        [umbrella],
        [None, 6, None, None]))

    # Room ID: 8
    # Room: Roof
    # Object List: ?
    # Direction: [N: Porch, E: None, S: None, W: None]
    room_list.append(Room(
        8,
        "Roof",
        "You find yourself standing on the roof of your one-story "
        "house. You can see a pair of squirrels chasing each other"
        " in the nearby branches. A small flock of hungry looking "
        "birds circles overhead. Their simple nest is perched right"
        " at the edge of the roof, looking comfortable enough for a "
        "napping spot. \nTo the North, you can climb the gutter back "
        "to the porch.\n",
        "You find yourself standing on the roof of your one-story "
        "house. A simple nest is perched right"
        " at the edge of the roof, looking comfortable enough for a "
        "napping spot. \nTo the North, you can climb the gutter back "
        "to the porch.\n",
        [],
        [6, None, None, None]))

    # Room ID: 9
    # Room: Park
    # Object List: ?
    # Direction: [N: None, E: None, S: None, W: None]
    # TODO: implement a final game state, based on items acquired
    room_list.append(Room(
        9,
        "Park",
        "Long Description",
        "Short Description",
        [],
        [None, None, None, None]))
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
