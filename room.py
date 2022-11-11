from nav import Direction


class Room:
    """
    Creates a full room environment
    """
    def __init__(self, room_id, room_name, long_description,
                 short_description, object_list, feature_list, directions, custom_exits={}):
        self.room_id = room_id
        self.room_name = room_name
        self.long_description = long_description
        self.short_description = short_description
        self.object_list = object_list
        self.directions = directions  # [North, East, South, West]
        self.feature_list = feature_list
        self.visited = False        # Show full description only on first visit
        self.direction_dict = {
            "north": Direction.NORTH,
            "east": Direction.EAST,
            "south": Direction.SOUTH,
            "west": Direction.WEST
        }
        self.direction_dict.update(custom_exits)


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
