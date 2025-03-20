import csv
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

CHARACTER_FILE = "characters.csv"
fake = Faker()

def create_character():
    """Generate a character with random attributes and a backstory."""
    name = fake.first_name()
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    defense = random.randint(5, 15)
    speed = random.randint(5, 15)
    backstory = fake.sentence()
    return [name, health, strength, defense, speed, 0, 1, backstory]

def save_characters(characters):
    """Save characters to a CSV file."""
    with open(CHARACTER_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(characters)

def load_characters():
    """Load characters from a CSV file into a DataFrame."""
    try:
        return pd.read_csv(CHARACTER_FILE, names=["Name", "Health", "Strength", "Defense", "Speed", "Experience", "Level", "Backstory"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Health", "Strength", "Defense", "Speed", "Experience", "Level", "Backstory"])

def display_characters(df):
    """Print character stats."""
    print(df)

def battle(char1, char2):
    """Simulate a battle between two characters."""
    while char1[1] > 0 and char2[1] > 0:
        if char1[4] >= char2[4]:
            char2[1] -= max(1, char1[2] - char2[3])
            if char2[1] <= 0:
                return char1
            char1[1] -= max(1, char2[2] - char1[3])
        else:
            char1[1] -= max(1, char2[2] - char1[3])
            if char1[1] <= 0:
                return char2
            char2[1] -= max(1, char1[2] - char2[3])
    return char1 if char1[1] > 0 else char2

def visualize_character(df, name):
    """Generate a radar chart for a character's stats."""
    char = df[df["Name"] == name].iloc[0]
    stats = char[["Health", "Strength", "Defense", "Speed"]].values
    labels = ["Health", "Strength", "Defense", "Speed"]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats = np.concatenate((stats,[stats[0]]))
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw={"projection": "polar"})
    ax.fill(angles, stats, color='b', alpha=0.25)
    ax.plot(angles, stats, color='b', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title(f"Stats for {name}")
    plt.show()

def analyze_stats(df):
    """Perform basic statistical analysis on character attributes."""
    stats = df[["Health", "Strength", "Defense", "Speed"]]
    print("Statistical Summary:")
    print(stats.describe())

def main_menu():
    characters = load_characters()
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Battle")
        print("4. Visualize Character")
        print("5. Analyze Stats")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            new_char = create_character()
            characters.loc[len(characters)] = new_char
            save_characters(characters.values.tolist())
            print(f"Character {new_char[0]} created with backstory: {new_char[7]}")
        elif choice == "2":
            display_characters(characters)
        elif choice == "3":
            if len(characters) < 2:
                print("Not enough characters for battle.")
                continue
            print(characters[["Name"]])
            char1_name = input("Enter first character's name: ")
            char2_name = input("Enter second character's name: ")
            char1 = characters[characters["Name"] == char1_name].values.tolist()[0]
            char2 = characters[characters["Name"] == char2_name].values.tolist()[0]
            winner = battle(char1, char2)
            print(f"{winner[0]} wins the battle!")
        elif choice == "4":
            name = input("Enter character's name to visualize: ")
            visualize_character(characters, name)
        elif choice == "5":
            analyze_stats(characters)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
