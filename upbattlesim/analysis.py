import pandas as pd
from file import characters

def analyze_characters():
    if not characters:
        print("No characters to analyze.")
        return

    df = pd.DataFrame.from_dict(characters, orient='index')

    print("\n--- Character Stats Analysis ---")
    print("Mean Stats:")
    print(df[['health', 'strength', 'defense', 'speed']].mean().round(2))

    print("\nMedian Stats:")
    print(df[['health', 'strength', 'defense', 'speed']].median())

    print("\nMax Stats:")
    print(df[['health', 'strength', 'defense', 'speed']].max())

    print("\nMin Stats:")
    print(df[['health', 'strength', 'defense', 'speed']].min())

