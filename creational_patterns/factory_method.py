from creational_patterns.models import *


class MazeGame:
    def make_maze(self):
        return Maze()

    def make_room(self, room_no):
        return Room(room_no)

    def make_wall(self):
        return Wall()

    def make_door(self, room1, room2):
        return Door(room1, room2)

    def create_maze(self):
        maze = self.make_maze()
        room1 = self.make_room(1)
        room2 = self.make_room(2)
        door = self.make_door(room1, room2)
        room1.set_side(Direction.NORTH, self.make_wall())
        room1.set_side(Direction.SOUTH, self.make_wall())
        room1.set_side(Direction.EAST, self.make_wall())
        room1.set_side(Direction.WEST, door)
        room2.set_side(Direction.NORTH, self.make_wall())
        room2.set_side(Direction.SOUTH, self.make_wall())
        room2.set_side(Direction.EAST, door)
        room2.set_side(Direction.WEST, self.make_wall())
        maze.add_room(room1)
        maze.add_room(room2)
        return maze


maze = MazeGame().create_maze()
room1 = maze.get_room(1)
room2 = maze.get_room(2)
assert type(room1.get_side(Direction.WEST)) == Door
assert type(room2.get_side(Direction.EAST)) == Door
print(maze)


class EnchantedMazeGame(MazeGame):
    def make_maze(self):
        return EnchantedMaze()

    def make_door(self, room1, room2):
        return EnchantedDoor(room1, room2)

    def make_room(self, room_no):
        return EnchantedRoom(room_no)


maze = EnchantedMazeGame().create_maze()
room1 = maze.get_room(1)
room2 = maze.get_room(2)
assert type(room1) == EnchantedRoom
assert type(room2.get_side(Direction.EAST)) == EnchantedDoor
print(maze)


