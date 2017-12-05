"""
I will suffix all class prototype-related with Pr, eg: MazePr
"""

from creational_patterns._models import *
from creational_patterns.abstract_factory import MazeFactory


class MazePr(Maze):
    def clone(self):
        result = MazePr()
        result.room_dict = self.room_dict
        return result

    def initialize(self):
        pass

prototype_maze = MazePr()


class DoorPr(Door):
    def clone(self):
        result = DoorPr(None, None)
        return result

    def initialize(self, room1, room2):
        self._room1 = room1
        self._room2 = room2

prototype_door = DoorPr(None, None)


class WallPr(Wall):
    def clone(self):
        result = WallPr()
        return result

    def initialize(self):
        pass

prototype_wall = WallPr()


class RoomPr(Room):
    def clone(self):
        result = RoomPr(0)
        result._sides = [None] * 4
        return result

    def initialize(self, room_no):
        self._room_no = room_no

prototype_room = RoomPr(0)


class EnchantedRoomPr(RoomPr, EnchantedRoom):
    def clone(self):
        result = EnchantedRoomPr(0)
        result._sides = [None] * 4
        return result

prototype_room_enchanted = EnchantedRoomPr(0)


class MazePrototypeFactory(MazeFactory):
    def __init__(self, maze, wall, room, door):
        self._prototype_maze = maze
        self._prototype_wall = wall
        self._prototype_room = room
        self._prototype_door = door

    def make_maze(self):
        return self._prototype_maze.clone()

    def make_room(self, room_no):
        result = self._prototype_room.clone()
        result.initialize(room_no)
        return result

    def make_wall(self):
        return self._prototype_wall.clone()

    def make_door(self, room1, room2):
        result = self._prototype_door.clone()
        result.initialize(room1, room2)
        return result

if __name__ == "__main__":
    prototype_factory = MazePrototypeFactory(
        prototype_maze, prototype_wall, prototype_room, prototype_door
    )

    room1 = prototype_factory.make_room(1)
    room2 = prototype_factory.make_room(2)
    door = prototype_factory.make_door(room1, room2)
    assert isinstance(door, DoorPr)
    assert isinstance(room1, RoomPr)
    assert room2._room_no == 2
    assert door.other_side_room(room1) == room2
    assert room1 != prototype_room and door != prototype_door

    prototype_factory_enchanted = MazePrototypeFactory(
        prototype_maze, prototype_wall, prototype_room_enchanted, prototype_door
    )
    room3 = prototype_factory_enchanted.make_room(3)
    assert isinstance(room3, EnchantedRoomPr)
    assert hasattr(room3, 'cast_spell')


