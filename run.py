from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size, the name of the ships,
    the player's name and the board type (player board or computer board).
    Methods for adding ships, guesses and printing board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.baord = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """
        Print the board grid.
        """
        for row in self.baord:
            print(" ".join(row))
    
    def add_ships(self):
        """
        Randomly places the computer's fleet of battleships on the grid.
        """
        for _ in range(self.num_ships):
            ship_placed = False
            while not ship_placed:
                x = self.get_random_coordinate()
                y = self.get_random_coordinate()
                if self.board[x][y] == ".":
                    self.board[x][y] = "S"
                    self.ships.append((x, y))
                    ship_placed = True