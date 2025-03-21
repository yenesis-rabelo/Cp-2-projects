import matplotlib.pyplot as plt
import numpy as np

def visualize_character(df, name):
    """Generate a radar chart for a character's stats."""
    try:
        char = df[df["Name"] == name].iloc[0]
    except IndexError:
        print("Character not found.")
        return
    
    stats = char[["Health", "Strength", "Defense", "Speed"]].values
    labels = ["Health", "Strength", "Defense", "Speed"]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats = np.concatenate((stats, [stats[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw={"projection": "polar"})
    ax.fill(angles, stats, color='b', alpha=0.25)
    ax.plot(angles, stats, color='b', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title(f"Stats for {name}")
    plt.show()
