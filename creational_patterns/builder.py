"""
    I added some contraints so that the builder makes sens.
    - When added, a room must specify an adjacent room
    - This adjacent room is mandatory, except for the first room
"""


from creational_patterns.control import Wall, Door, Room, Maze, Direction


class MazeBuilder:
    def build_maze(self):
        raise NotImplementedError

    def build_room(self, room_no, referent_room_no, direction_from_referent_room):
        raise NotImplementedError

    def build_door(self, room_no1, room_no2):
        raise NotImplementedError

    def get_maze_presentation(self):
        raise NotImplementedError


class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self._current_maze = None

    def build_maze(self):
        self._current_maze = Maze()

    def build_room(self, room_no, referent_room_no, direction_from_referent_room):
        if not self._current_maze.room_dict:  # first room
            self.build_first_room(room_no)
        else:
            self.build_adjacent_room(room_no, referent_room_no, direction_from_referent_room)

    def build_first_room(self, room_no):
        room = Room(room_no)
        room.set_side(Direction.NORTH, Wall())
        room.set_side(Direction.SOUTH, Wall())
        room.set_side(Direction.EAST, Wall())
        room.set_side(Direction.WEST, Wall())

    def build_adjacent_room(self,room_no, referent_room_no, direction_from_referent_room):
        room = Room(room_no)
        referent_room = self._current_maze.get_room(referent_room_no)
        adjacent_site = referent_room.get_side(direction_from_referent_room)
        room.set_side(direction_from_referent_room.opposite(), adjacent_site)
        for direction in list(Direction):
            if direction != direction_from_referent_room:
                room.set_side(direction, Wall())

    def get_maze_presentation(self):
        return self._current_maze


def build_simple_maze(builder):
    builder.build_maze()
    builder.build_room(1, None, None)
    builder.build_room(2, 1, Direction.NORTH)
    return builder.get_maze_presentation()

print(build_simple_maze(StandardMazeBuilder()))




