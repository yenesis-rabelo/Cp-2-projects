import random

def run_tic_tac_toe():
    """Runs a Tic-Tac-Toe game where the user plays against the computer."""
    print("Project: Tic-Tac-Toe ProficiencyTest")
    print("This project lets you play Tic-Tac-Toe against the computer.")
    print("What I learned: How intricate and detailed coding was.")
    print("Programming process: A bit challenging.")
    
    # Initialize the game board as a 3x3 grid
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    def print_board():
        """Prints the current state of the board."""
        print("\nCurrent Board:")
        for row in board:
            print("|".join(row))
            print("-" * 5)
    
    def check_winner():
        """Checks if there's a winner or a draw in the game."""
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        if all(cell != " " for row in board for cell in row):
            return "Draw"
        return None
    
    def player_move():
        """Handles the player's move."""
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column from 0-2 separated by space): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("That space is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
    
    def computer_move():
        """Handles the computer's move, selecting a random empty space."""
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == " ":
                board[row][col] = "O"
                break
    
    # Main game loop
    while True:
        print_board()
        player_move()
        if (winner := check_winner()):
            print_board()
            if winner == "X":
                print("Congratulations! You win!")
            elif winner == "O":
                print("Sorry, the computer wins!")
            else:
                print("It's a draw!")
            break
        computer_move()
        if (winner := check_winner()):
            print_board()
            if winner == "X":
                print("Congratulations! You win!")
            elif winner == "O":
                print("Sorry, the computer wins!")
            else:
                print("It's a draw!")
            break
