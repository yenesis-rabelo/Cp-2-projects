import csv
import random

CHARACTER_FILE = "characters.csv"

class Character:
    def __init__(self, name, health, strength, defense, speed, experience=0, level=1):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.experience = experience
        self.level = level
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def attack(self, opponent):
        damage = max(1, self.strength - opponent.defense)
        opponent.take_damage(damage)
        return damage
    
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 10:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.health += 5
        self.strength += 2
        self.defense += 2
        self.speed += 1
        print(f"{self.name} leveled up! Now at level {self.level}.")
    
    def to_list(self):
        return [self.name, self.health, self.strength, self.defense, self.speed, self.experience, self.level]
    
    @staticmethod
    def from_list(data):
        return Character(data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]))

def save_characters(characters):
    with open(CHARACTER_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for char in characters:
            writer.writerow(char.to_list())

def load_characters():
    characters = []
    try:
        with open(CHARACTER_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                characters.append(Character.from_list(row))
    except FileNotFoundError:
        pass
    return characters

def display_characters(characters):
    for char in characters:
        print(f"{char.name}: Level {char.level}, HP: {char.health}, STR: {char.strength}, DEF: {char.defense}, SPD: {char.speed}, EXP: {char.experience}")

def create_character():
    name = input("Enter character name: ")
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    defense = random.randint(5, 15)
    speed = random.randint(5, 15)
    return Character(name, health, strength, defense, speed)

def battle_system():
    characters = load_characters()
    if len(characters) < 2:
        print("Not enough characters to battle. Create more characters first.")
        return
    
    print("Select two characters for battle:")
    display_characters(characters)
    
    char1_name = input("Enter first character's name: ")
    char2_name = input("Enter second character's name: ")
    
    char1 = next((char for char in characters if char.name == char1_name), None)
    char2 = next((char for char in characters if char.name == char2_name), None)
    
    if not char1 or not char2 or char1 == char2:
        print("Invalid characters selected.")
        return
    
    print(f"Battle begins: {char1.name} vs {char2.name}!")
    while char1.health > 0 and char2.health > 0:
        if char1.speed >= char2.speed:
            damage = char1.attack(char2)
            print(f"{char1.name} attacks {char2.name} for {damage} damage!")
            if char2.health == 0:
                break
            
            damage = char2.attack(char1)
            print(f"{char2.name} attacks {char1.name} for {damage} damage!")
        else:
            damage = char2.attack(char1)
            print(f"{char2.name} attacks {char1.name} for {damage} damage!")
            if char1.health == 0:
                break
            
            damage = char1.attack(char2)
            print(f"{char1.name} attacks {char2.name} for {damage} damage!")
    
    winner = char1 if char1.health > 0 else char2
    print(f"{winner.name} wins the battle!")
    winner.gain_experience(10)
    save_characters(characters)

def main_menu():
    characters = load_characters()
    while True:
        print("\nBattle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Battle")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            new_char = create_character()
            characters.append(new_char)
            save_characters(characters)
            print(f"Character {new_char.name} created!")
        elif choice == "2":
            display_characters(characters)
        elif choice == "3":
            battle_system()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
