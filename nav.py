from enum import Enum

class Direction(Enum):
  NORTH = 0
  EAST = 1
  SOUTH = 2
  WEST = 3

def move(direction, player, room_list):
    direction = direction.lower()
    if direction not in player.location.direction_dict:
        return "No Exit: {}".format(direction)
    direction_category = player.location.direction_dict[direction]
    if direction_category == Direction.NORTH:
        # move north
        if player.location.north() is not None:
            player.set_location(room_list[player.location.north()])
            return player.location.short_description
    elif direction_category == Direction.EAST:
        # move east
        if player.location.east() is not None:
            player.set_location(room_list[player.location.east()])
            return player.location.short_description
    elif direction_category == Direction.SOUTH:
        # move south
        if player.location.south() is not None:
            player.set_location(room_list[player.location.south()])
            return player.location.short_description
    elif direction_category == Direction.WEST:
        # move west
        if player.location.west() is not None:
            player.set_location(room_list[player.location.west()])
            return player.location.short_description
    else:
        return "invalid direction enum, bad config"
    return "Cannot go to the {}!".format(direction)

def clean_and_move(response, player, room_list):
    # removes surrounding white space
    direction = response.strip()
    return move(direction, player, room_list)
