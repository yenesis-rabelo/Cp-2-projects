import csv  
import random  
import pandas as pd  
from faker import Faker  
  
CHARACTER_FILE = "characters.csv"  
fake = Faker()  
  
backstories = [  
    f"{fake.first_name()} was born in {fake.city()}, where they trained tirelessly. "  
    f"After a life-altering event involving a fierce dragon, they vowed to become stronger.",  
]  
  
used_backstories = []  
  
def create_character():    
    name = fake.first_name()    
    health = random.randint(50, 100)    
    strength = random.randint(10, 20)    
    defense = random.randint(5, 15)    
    speed = random.randint(5, 15)    
    
    available_backstories = [b for b in backstories if b not in used_backstories]  
    backstory = random.choice(available_backstories) if available_backstories else "No backstory available."  
    used_backstories.append(backstory)  
    
    return [name, health, strength, defense, speed, 0, 1, backstory]    
  
def save_characters(df):  
    df.to_csv(CHARACTER_FILE, index=False)  
  
def load_characters():  
    try:  
        return pd.read_csv(CHARACTER_FILE)  
    except FileNotFoundError:  
        return pd.DataFrame(columns=["Name", "Health", "Strength", "Defense", "Speed", "Experience", "Level", "Backstory"])  
  
def delete_character(df, name):  
    df = df[df["Name"] != name]  
    print(f"Character {name} has been deleted.")  
    return df  