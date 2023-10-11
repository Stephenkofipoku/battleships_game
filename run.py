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
        if self.type == "player":
            print(f"{self.name}'s Board:")
        else:
            print("Computer's Board:")
        for row in self.board:
            print(" ".join(row).replace("S", "@" if self.type == "player" else ".").replace("*", "@").replace("x", "X"))

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

    def computer_guess(self):
        """
        Generates computer's guess by randomly selecting coordinates.
        """
        valid_guess = False
        while not valid_guess:
            x = self.get_random_coordinate()
            y = self.get_random_coordinate()
            if (x, y) not in self.guesses:
                valid_guess = True
        self.guesses.append((x, y))
        return (x, y)

    def user_guess(self):
        """
        Takes user input for the grid coordinates to call shots at the computer's ships.
        Validates the input and returns the coordinates.
        """
        valid_guess = False
        while not valid_guess:
            try:
                x = int(input("Enter the x-coordinate (0-9): \n"))
                y = int(input("Enter the y-coordinate (0-9): \n"))
                if self.validate_coordinates(x, y) and self.is_valid_guess(x, y):
                    valid_guess = True
                else:
                    print("Invalid guess. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid coordinates.")
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


def make_guess(computer_board, player_board):
    """
    Makes a guess on the board and updates the scores.
    """
    print("Player's Turn")
    print("--------------")
    player_board.print()
    x, y = player_board.user_guess()

    if (x, y) in computer_board.ships:
        print(f"Player guessed: ({x}, {y}). Player got a hit!")
        scores["player"] += 1
        computer_board.board[x][y] = "*"
    else:
        print(f"Player guessed: ({x}, {y}). Player missed this time.")
        player_board.board[x][y] = "x"

    print("")

    print("Computer's Turn")
    print("----------------")
    computer_board.print()
    x, y = computer_board.computer_guess()

    if (x, y) in player_board.ships:
        print(f"Computer guessed: ({x}, {y}). Computer got a hit!")
        scores["computer"] += 1
        player_board.board[x][y] = "*"
    else:
        print(f"Computer guessed: ({x}, {y}). Computer missed this time.")
        computer_board.board[x][y] = "X"

    print("")

    print("After this round, the scores are: Player:", scores["player"], "Computer:", scores["computer"])
    print("")

    print(player_board.name + "'s Board:")
    player_board.print()

    print("")

    print("Computer's Board:")
    computer_board.print()

    print("")

    return


def play_game(computer_board, player_board):
    """
    Plays the game by alternating turns between the computer and the player.
    """
    print("Battleships Game")
    print("Player: ", player_board.name)
    print("Computer: ", computer_board.name)
    print("")

    while scores["computer"] < player_board.num_ships and scores["player"] < computer_board.num_ships:
        make_guess(computer_board, player_board)
        print(f"After this round, the scores are: Player: {scores['player']}. Computer: {scores['computer']}")
        print("")
        choice = input("-----------------------------------\nPress any key to continue or 'n' to quit: ")
        if choice.lower() == "n":
            break

    print("Game Over")
    if scores["player"] == computer_board.num_ships:
        print("Congratulations! You won!")
    else:
        print("Better luck next time. The computer won.")

    print(f"After this round, the scores are: Player: {scores['player']}. Computer: {scores['computer']}")
    print("")


def start_new_game():
    """
    Start new game. Sets the board size and number of ships,
    resets the scores and initializes the boards.
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

    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    populate_board(computer_board)
    populate_board(player_board)

    print("Your Board:")
    player_board.print()

    print("\nComputer's Board:")
    computer_board.print()

    print("-" * 35)

    play_game(computer_board, player_board)

    print("-" * 35)
    choice = input("Press any key to continue or 'n' to quit: ")
    if choice.lower() != "n":
        start_new_game()
    print("-" * 35)


start_new_game()