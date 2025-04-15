import random
from faker import Faker
from utils import display_character
from file import characters

faker = Faker()

def character_menu():
    def create_character():
        name = input("Enter character name: ")
        if name in characters:
            print("Character already exists.")
            return
        characters[name] = generate_random_character(name)
        print(f"Character '{name}' created!")

    def create_random_character():
        name = faker.first_name()
        characters[name] = generate_random_character(name)
        characters[name]['description'] = faker.sentence()
        print(f"Random character '{name}' created with backstory: {characters[name]['description']}")

    def view_characters():
        if not characters:
            print("No characters to display.")
            return
        for char in characters.values():
            display_character(char)

    while True:
        print("\nCharacter Menu:")
        print("1. Create Character")
        print("2. Create Random Character")
        print("3. View Characters")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            create_character()
        elif choice == '2':
            create_random_character()
        elif choice == '3':
            view_characters()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

def generate_random_character(name):
    return {
        'name': name,
        'health': random.randint(80, 120),
        'strength': random.randint(10, 20),
        'defense': random.randint(5, 15),
        'speed': random.randint(5, 15),
        'level': 1,
        'xp': 0
    }
