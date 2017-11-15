from creational_patterns.models import *

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
