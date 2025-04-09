# Importing functions from other project files
from simple_calculator import run_simple_calculator
from quiz_game import run_quiz_game
from tic_tac_toe import run_tic_tac_toe
from madilb import run_madilb
from pig_latin import run_pig_latin
from list_of_classes import run_list_of_classes

def main_menu():
    """Displays the main menu with available project options."""
    print("\nWelcome to my project collection!")
    print("Please select a project to run:")
    print("1. Simple Calculator")
    print("2. Quiz Game")
    print("3. Tic-Tac-Toe")
    print("4. Madilb")
    print("5. Pig Latin")
    print("6. List of Classes")
    print("0. Exit")

def project_selection():
    """Allows the user to select and run a project from the main menu."""
    print("Starting project selection...")  # Debugging line
    while True:
        main_menu()  # Display the main menu
        choice = input("Select a project by number: ")

        # Execute corresponding project based on user's choice
        if choice == '1':
            run_simple_calculator()
        elif choice == '2':
            run_quiz_game()
        elif choice == '3':
            run_tic_tac_toe()
        elif choice == '4':
            run_madilb()
        elif choice == '5':
            run_pig_latin()
        elif choice == '6':
            run_list_of_classes()
        elif choice == '0':
            print("Thank you for viewing my projects!")
            break  # Exit the loop and the program
        else:
            print("Invalid choice, please try again.")  # Invalid input handling

# Run the project selection function to start the program
project_selection()



