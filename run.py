from random import randint
from termcolor import colored

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
            print(colored(f"{self.name}'s Board:", "green"))
        else:
            print(colored("Computer's Board:", "green"))
        for row in self.board:
            if self.type == "player":
                print(colored(" ".join(row).replace("S", "@"), "green").replace("*", "@").replace("x", "X"))
            else:
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
                x = int(input(colored("Enter the x-coordinate (0-4): \n", "yellow")))
                y = int(input(colored("Enter the y-coordinate (0-4): \n", "yellow")))
                if self.validate_coordinates(x, y) and self.is_valid_guess(x, y):
                    valid_guess = True
                else:
                    print(colored("Invalid guess. Try again.", "red"))
            except ValueError:
                print(colored("Invalid input. Please enter valid coordinates.", "red"))
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
        if (x, y) in self.guesses:
            print(colored("Coordinates repeated, ", "red"))
            return False
        return True


def populate_board(board):
    """
    Populates the board with ships.
    """
    board.add_ships()


def make_guess(computer_board, player_board):
    """
    Makes a guess on the board and updates the scores.
    """
    print(colored("Player's Turn", "cyan"))
    print("-" * 14)
    player_board.print()
    x, y = player_board.user_guess()

    if (x, y) in computer_board.ships:
        print(colored(f"Player guessed: ({x}, {y}). Player got a hit!", "green"))
        scores["player"] += 1
        computer_board.board[x][y] = "*"
    else:
        print(colored(f"Player guessed: ({x}, {y}). Player missed this time.", "red"))
        player_board.board[x][y] = "x"

    print("")

    print(colored("Computer's Turn", "cyan"))
    print("-" * 16)
    computer_board.print()
    x, y = computer_board.computer_guess()

    if (x, y) in player_board.ships:
        print(colored(f"Computer guessed: ({x}, {y}). Computer got a hit!", "green"))
        scores["computer"] += 1
        player_board.board[x][y] = "*"
    else:
        print(colored(f"Computer guessed: ({x}, {y}). Computer missed this time.", "red"))
        computer_board.board[x][y] = "X"

    print("")

    print(colored(f"After this round, the scores are: Player: {scores['player']}, Computer: {scores['computer']}", "magenta"))
    print("")

    print(colored(player_board.name + "'s Board:", "cyan"))
    player_board.print()

    print("")

    print(colored("Computer's Board:", "cyan"))
    computer_board.print()

    print("")


def play_game(computer_board, player_board):
    """
    Plays the game by alternating turns between the computer and the player.
    """
    print(colored("Battleships Game", "magenta"))
    print(colored("Player: ", "magenta") + player_board.name)
    print(colored("Computer: ", "magenta") + computer_board.name)
    print("")

    while scores["computer"] < player_board.num_ships and scores["player"] < computer_board.num_ships:
        make_guess(computer_board, player_board)
        print(colored(f"After this round, the scores are: Player: {scores['player']}, Computer: {scores['computer']}", "magenta"))
        print("")
        choice = input(colored("-----------------------------------\nPress any key to continue or 'n' to quit: ", "yellow"))
        if choice.lower() == "n":
            break

    print(colored("Game Over", "cyan"))
    if scores["player"] == computer_board.num_ships:
        print(colored("Congratulations! You won!", "green"))
    else:
        print(colored("Better luck next time. The computer won.", "red"))

    print(colored(f"After this round, the scores are: Player: {scores['player']}, Computer: {scores['computer']}", "magenta"))
    print("")


def start_new_game():
    """
    Game instructions. Start new game. Sets the board size and number of ships,
    resets the scores and initializes the boards.
    """
    
    print(colored("Welcome to Super Battleships!", "cyan"))
    show_instructions = input(colored("Do you want to see the game instructions? (yes/no): ", "yellow"))
    if show_instructions.lower() == "yes":
        print(colored("How to Play\n"
                      "To play the game:\n"
                      "1. Enter your name when prompted.\n"
                      "2. The game will display both the player's board and the computer's board.\n"
                      "3. The player will take turns guessing the coordinates to attack the computer's ships.\n"
                      "4. Enter the x and y coordinates for your guess when prompted.\n"
                      "5. The game will indicate whether the guess was a hit or a miss.\n"
                      "6. The computer will then take its turn and randomly guess coordinates on the player's board.\n"
                      "7. The game will display the updated scores and the boards after each round.\n"
                      "8. Continue taking turns until either the player or the computer sinks all the ships.\n"
                      "9. The game will declare the winner and display the final scores.\n", "cyan"))

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0

    print(colored("-" * 35, "cyan"))
    print(colored("Welcome to SUPER BATTLESHIPS!!", "magenta"))
    print(colored("Board Size: 5. Number of ships: 4", "magenta"))
    print(colored("Top left corner is row 0, col: 0", "magenta"))
    print(colored("-" * 35, "cyan"))

    player_name = ""
    while not player_name.isalpha() or not player_name:
        player_name = input(colored("Enter your name: \n", "yellow"))
        if not player_name.isalpha():
            print(colored("Invalid input. Please enter alphabetic characters only.", "red"))
        elif not player_name:
            print(colored("Invalid input. Please enter a non-empty name.", "red"))
    print(colored("-" * 35, "cyan"))

    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    populate_board(computer_board)
    populate_board(player_board)

    print(colored("Your Board:", "cyan"))
    player_board.print()

    print("\n" + colored("Computer's Board:", "cyan"))
    computer_board.print()

    print(colored("-" * 35, "cyan"))

    play_game(computer_board, player_board)

    print(colored("-" * 35, "cyan"))
    choice = input(colored("Press any key to continue or 'n' to quit: ", "yellow"))
    if choice.lower() == "n":
        return
    print(colored("-" * 35, "cyan"))
    start_new_game()


start_new_game()
