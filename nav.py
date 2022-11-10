def move(direction, player, room_list):
    direction = direction.lower()
    if direction == "north":
        # move north
        if player.location.north() is None:
            return "Cannot go north!"
        player.set_location(room_list[player.location.north()])
        return player.location.short_description
    elif direction == "east":
        # move east
        if player.location.east() is None:
            return ("Cannot go east!")
        player.set_location(room_list[player.location.east()])
        return player.location.short_description
    elif direction == "south":
        # move south
        if player.location.south() is None:
            return ("Cannot go south!")
        player.set_location(room_list[player.location.south()])
        return player.location.short_description
    elif direction == "west":
        # move west
        if player.location.west() is None:
            return ("Cannot go west!")
        player.set_location(room_list[player.location.west()])
        return player.location.short_description
    return "invalid direction..."


def clean_and_move(response, player, room_list):
    # removes all words after the direction
    direction = response.split()[0]
    # removes surrounding white space
    direction = direction.strip()
    return move(direction, player, room_list)
