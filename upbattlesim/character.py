import csv
import random
import pandas as pd
from faker import Faker

CHARACTER_FILE = "characters.csv"
fake = Faker()

def create_character():
    """Generate a character with detailed attributes and a backstory."""
    name = fake.first_name()
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    defense = random.randint(5, 15)
    speed = random.randint(5, 15)
    
    backstory = (
        f"{name} was born in {fake.city()}, where they trained tirelessly. "
        f"After a life-altering event involving {fake.word()}, they vowed to become stronger. "
        f"Known for their {fake.word()} spirit, they are feared by many."
    )

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

def delete_character(df, name):
    """Delete a character by name."""
    df = df[df["Name"] != name]
    print(f"Character {name} has been deleted.")
    return df