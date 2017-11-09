"""
    I added some contraints so that the builder makes sens.
    - When added, a room must specify an adjacent room
    - This adjacent room is mandatory, except for the first room
"""


from creational_patterns.control import Wall, Door, Room, Maze, Direction
from itertools import product


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
        self._current_maze.add_room(room)

    def build_adjacent_room(self,room_no, referent_room_no, direction_from_referent_room):
        room = Room(room_no)
        referent_room = self._current_maze.get_room(referent_room_no)
        adjacent_site = referent_room.get_side(direction_from_referent_room)
        room.set_side(direction_from_referent_room.opposite(), adjacent_site)
        for direction in list(Direction):
            if direction != direction_from_referent_room.opposite():
                room.set_side(direction, Wall())
        self._current_maze.add_room(room)

    @staticmethod
    def common_wall(room1, room2):
        for d1, d2 in product(list(Direction), list(Direction)):
            side_room1 = room1.get_side(d1)
            side_room2 = room2.get_side(d2)
            if side_room1 == side_room2:
                return d1
        return None

    def build_door(self, room_no1, room_no2):
        assert room_no1 != room_no2
        room1 = self._current_maze.get_room(room_no1)
        room2 = self._current_maze.get_room(room_no2)
        common_wall_direction = self.common_wall(room1, room2)
        if common_wall_direction:
            door = Door(room1, room2)
            room1.set_side(common_wall_direction, door)
            room2.set_side(common_wall_direction.opposite(), door)
        else:
            assert False, 'no common wall for rooms {} and {}'.format(room_no1, room_no2)

    def get_maze_presentation(self):
        return self._current_maze


def build_simple_maze(builder):
    builder.build_maze()
    builder.build_room(1, None, None)
    builder.build_room(2, 1, Direction.NORTH)
    builder.build_door(room_no1=1, room_no2=2)
    return builder.get_maze_presentation()


if __name__ == "__main__":
    standard_maze_representation = build_simple_maze(StandardMazeBuilder())
    room1 = standard_maze_representation.get_room(1)
    room2 = standard_maze_representation.get_room(2)
    north_room1 = room1.get_side(Direction.NORTH)
    south_room2 = room2.get_side(Direction.SOUTH)
    assert isinstance(north_room1, Door)
    assert south_room2 == north_room1
    print(standard_maze_representation)







