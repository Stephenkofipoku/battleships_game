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
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """
        Print the board grid.
        """
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row).replace("S", "." if self.type == "player" else " "))
    
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


def make_guess(board):
    """
    Makes a guess on the board and updates the scores.
    """
    x, y = board.user_guess()
    if (x, y) in board.ships:
        print("Hit!")
        scores[board.type] += 1
    else:
        print("Miss!")


def play_game(computer_board, player_board):
    """
    Plays the game by alternating turns between the computer and the player.
    """
    print("Battleships Game")
    print("Player: ", player_board.name)
    print("Computer: ", computer_board.name)
    print("")

    while scores["computer"] < player_board.num_ships and scores["player"] < computer_board.num_ships:
        print("Player's Turn")
        print("--------------")
        make_guess(computer_board)
        print("Player's Score: ", scores["player"])
        print("")

        if scores["player"] == computer_board.num_ships:
            break

        print("Computer's Turn")
        print("----------------")
        make_guess(player_board)
        print("Computer's Score: ", scores["computer"])
        print("")

    print("Game Over")
    if scores["player"] == computer_board.num_ships:
        print("Congratulations! You won!")
    else:
        print("Better luck next time. The computer won.")


def start_new_game():
    """
    Start new game. Sets the board size and number of ships,
    resets the socres and initialises the boards.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    
    print("-" * 35)
    print("Welcome to SUPER BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row 0, col: 0")
    print("-" * 35)
    
    player_name = input("Enter your name: \n")
    print("-" * 35)
    
    computer_board = Board(size, num_ships, player_name, "computer")
    player_board = Board(size, num_ships, player_name, "player")
    
    populate_board(computer_board)
    populate_board(player_board)
    
    play_game(computer_board, player_board)


start_new_game()  
