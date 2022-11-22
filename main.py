# from room import Room
# from item import Item
import pickle
from character import Character
# from messages import messages
# from feature import Feature
# from nav import Direction
# from verb import VerbClass, verb_dict


def main():
    """
    Main function
    """
    # stores items picked up in inventory
    # inventory = []

    # for room in room_list:
    #     print(room.long_description)
    # print(inventory)
    player = Character("Player 1", 1)
    while True:
        response = input("Enter instructions: ").lower()
        if "quit" in response:
            print("\nThanks for playing. Quitting...\n")
            break
        print()
        print(player.handle_user_input(response))


# room_list = init_room_list_and_items()


if __name__ == "__main__":
    main()
    # This is Taylor's I will git rid of it when I am ready
    # users_file_base = {
    #     "saved_games": [],
    # }
    # save_file = open("C:/dev/marni-and-junimo/Marni-and-Junimo/game_data/users.p", "wb")
    # pickle.dump(users_file_base, save_file)
    # save_file.close()
