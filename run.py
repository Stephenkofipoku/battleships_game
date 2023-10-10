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
    
    def user_guess(self):
        """
        Takes user input for the grid coordinates to call shots at the computer's ships.
        Validates the input and returns the coordinates.
        """
        valid_guess = False
        while not valid_guess:
            x = int(input("Enter the x-coordinate: "))
            y = int(input("Enter the y-coordinate: "))
            if 0 <= x < self.size and 0 <= y < self.size and (x, y) not in self.guesses:
                valid_guess = True
            else:
                print("Invalid guess. Try again.")
        self.guesses.append((x, y))
        return (x, y)
    
    def get_random_coordinate(self):
        """
        Returns a random integer between 0 and size.
        """
        return randint(0, self.size - 1)

    def validate_coordinates(self, x, y):
        """
        Validates the coordinates to ensure they are within the board size.
        """
        return 0 <= x < self.size and 0 <= y < self.size

    def is_valid_guess(self, x, y):
        """
        Checks if the guess has already been made.
        """
        return (x, y) not in self.guesses

def populate_board(board):
    """
    Populates the board with ships.
    """
    board.add_ships()
