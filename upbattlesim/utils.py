from matplotlib import pyplot as plt
import pandas as pd

def display_character(char):
    print(f"\nName: {char['name']}")
    print(f"Level: {char['level']} | XP: {char['xp']}")
    print(f"Health: {char['health']}")
    print(f"Strength: {char['strength']}")
    print(f"Defense: {char['defense']}")
    print(f"Speed: {char['speed']}\n")

def plot_character_stats(char):
    labels = ['Health', 'Strength', 'Defense', 'Speed']
    stats = [char['health'], char['strength'], char['defense'], char['speed']]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, stats, color='skyblue')
    plt.title(f"{char['name']}'s Stats")
    plt.xlabel('Attributes')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.show()

def display_stat_analysis(df):
    print("\n--- Character Stats Analysis ---")
    print("Mean:")
    print(df[['health', 'strength', 'defense', 'speed']].mean().round(2))

    print("\nMedian:")
    print(df[['health', 'strength', 'defense', 'speed']].median())

    print("\nMax:")
    print(df[['health', 'strength', 'defense', 'speed']].max())

    print("\nMin:")
    print(df[['health', 'strength', 'defense', 'speed']].min())

