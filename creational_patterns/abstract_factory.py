from creational_patterns._models import *


class MazeFactory:
    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, room_no):
        return Room(room_no)

    def make_door(self, room1, room2):
        return Door(room1, room2)


def abstract_factory_make_maze(factory):
    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    door = factory.make_door(room1, room2)
    maze.add_room(room1)
    maze.add_room(room2)
    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.EAST, door)
    room1.set_side(Direction.WEST, Wall())
    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.EAST, Wall())
    room1.set_side(Direction.WEST, door)
    print('maze created with factory {}'.format(factory))
    return maze


class EnchantedMazeFactory(MazeFactory):
    def make_room(self, room_no):
        return EnchantedRoom(room_no)

    def make_door(self, room1, room2):
        return EnchantedDoor(room1, room2)


if __name__ == "__main__":
    normal_maze = abstract_factory_make_maze(MazeFactory())
    room1 = normal_maze.get_room(1)
    assert type(room1) == Room
    assert all(type(door) == Door for door in room1.get_doors())

    enchanted_maze = abstract_factory_make_maze(EnchantedMazeFactory())
    room1 = enchanted_maze.get_room(1)
    assert type(room1) == EnchantedRoom
    assert all(type(door) == EnchantedDoor for door in room1.get_doors())

