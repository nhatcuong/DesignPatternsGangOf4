from enum import Enum


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def opposite(self):
        ns = [Direction.NORTH, Direction.SOUTH]
        ew = [Direction.EAST, Direction.WEST]
        for opposites in (ns, ew):
            if self in opposites:
                opposites.remove(self)
                return opposites.pop()
        raise ValueError



class MapSite:
    def enter(self):
        raise NotImplementedError


class Room(MapSite):
    def __init__(self, room_no):
        self._room_no = room_no
        self._sides = [None] * 4

    def get_side(self, direction):
        return self._sides[direction.value]

    def set_side(self, direction, map_site):
        self._sides[direction.value] = map_site

    def get_no(self):
        return self._room_no

    def get_doors(self):
        return [site for site in self._sides if isinstance(site, Door)]


class Wall(MapSite):
    pass


class Door(MapSite):
    def __init__(self, room1, room2):
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def other_side_room(self, room):
        if self._room1 == room:
            return self._room2
        if self._room2 == room:
            return self._room1
        raise ValueError('door {} is not by room {}'.format(self, room))


class Maze:
    def __init__(self):
        self.room_dict = dict()

    def add_room(self, room):
        self.room_dict[room.get_no()] = room

    def get_room(self, no):
        try:
            return self.room_dict[no]
        except KeyError:
            raise ValueError('Maze {} does not have room no {}'.format(self, no))


def create_maze():  #create a maze with 2 rooms and a door in between
    maze = Maze()
    room1 = Room(1)
    room2 = Room(2)
    door = Door(room1, room2)
    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, Wall())
    room1.set_side(Direction.EAST, door)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.SOUTH, Wall())
    room1.set_side(Direction.WEST, door)
    room1.set_side(Direction.EAST, Wall())

    print('maze created')
    return maze


if __name__ == "__main__":
    create_maze()
