import csv  
import random  
import pandas as pd  
from faker import Faker  
  
CHARACTER_FILE = "characters.csv"  
fake = Faker()  
  
# List of backstory templates  
backstories = [  
    f"{fake.first_name()} was born in {fake.city()}, where they trained tirelessly. "  
    f"After a life-altering event involving a fierce dragon, they vowed to become stronger.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they were constantly ridiculed. "  
    f"After a life-altering event involving a mysterious prophecy, they decided they've had enough.",  
      
    f"{fake.first_name()} was born in {fake.city()}. "  
    f"After a mysterious prophecy foretold by a sage, they decided to find out what the prophecy was really about.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they trained tirelessly. "  
    f"After the death of their parents, they vowed to seek revenge.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they were often bullied for their slender frame, "  
    f"but they turned that ridicule into determination.",  
      
    f"{fake.first_name()} was born in {fake.city()}, off the Great Mountains, where their family was torn apart by a tragic war. "  
    f"As a young kid, they watched their village be ravaged, leaving them orphaned and filled with rage. "  
    f"Fueled by the desire for revenge, they trained under a retired war hero, learning the art of combat and strategy.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they were raised by a tribe of mystical druids. "  
    f"Gifted with the ability to communicate with nature, they discovered their powers at a young age.",  
      
    f"{fake.first_name()} was born in {fake.city()}, and was trained as an assassin in the shadowy alleys of Nightfall, "  
    f"where cunning and stealth were key to survival. Orphaned at a young age, they were taken in by a secretive guild that taught them the arts of stealth and deception.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they saw the worst of humanity. "  
    f"After losing their friends to a ruthless warlord, they trained as a soldier, determined to avenge them.",  
      
    f"{fake.first_name()} was born in {fake.city()}, where they learned to fight to survive. "  
    f"Their father was a blacksmith who forged weapons for the citys guards, and after witnessing their father's unjust execution by corrupt officials, they vowed to change the system."  
]  
  
used_backstories = []  # Keep track of used backstories  
  
def create_character():    
    """Generate a character with detailed attributes and a backstory."""    
    name = fake.first_name()    
    health = random.randint(50, 100)    
    strength = random.randint(10, 20)    
    defense = random.randint(5, 15)    
    speed = random.randint(5, 15)    
      
    # Filter available backstories  
    available_backstories = [b for b in backstories if b not in used_backstories]  
      
    if available_backstories:  # Check if there are any available backstories  
        backstory = random.choice(available_backstories)  
        used_backstories.append(backstory)  # Add the selected backstory to used ones  
    else:  
        backstory = "All backstories have been used."  # Handle when all backstories are used  
  
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
