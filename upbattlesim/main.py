
from character import create_character, save_characters, load_characters, delete_character
from battle import battle
from visualization import visualize_character
from analysis import analyze_stats

def display_characters(df):
    """Print all character stats."""
    print(df)
def main_menu():
    characters = load_characters()
    
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Battle")
        print("4. Visualize Character")
        print("5. Analyze Stats")
        print("6. Delete Character")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            new_char = create_character()
            characters.loc[len(characters)] = new_char
            save_characters(characters.values.tolist())
            print(f"\nCharacter {new_char[0]} created!\nBackstory: {new_char[7]}\n")
        
        elif choice == "2":
            display_characters(characters)
        
        elif choice == "3":
            if len(characters) < 2:
                print("Not enough characters for battle.")
                continue
            print(characters[["Name"]])
            char1_name = input("Enter first character's name: ")
            char2_name = input("Enter second character's name: ")

            try:
                char1 = characters[characters["Name"] == char1_name].values.tolist()[0]
                char2 = characters[characters["Name"] == char2_name].values.tolist()[0]
            except IndexError:
                print("One or both characters not found.")
                continue

            winner = battle(char1, char2)
            print(f"\n{winner[0]} wins the battle!\n")
        
        elif choice == "4":
            name = input("Enter character's name to visualize: ")
            visualize_character(characters, name)
        
        elif choice == "5":
            analyze_stats(characters)
        
        elif choice == "6":
            name = input("Enter character's name to delete: ")
            characters = delete_character(characters, name)
            save_characters(characters.values.tolist())
        
        elif choice == "7":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()

