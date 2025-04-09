# madilb.py

def run_madilb():
    """Generates a random story based on user input (Madilb)."""
    print("Project: Madilb")
    print("This project lets you create your own Madilb story.")
    print("What I learned: What a Madilb was haha.")
    print("Programming process: Easy!")
    
    # Collect user inputs for different parts of the story
    noun_1 = input("noun: ")
    noun_2 = input("noun: ")
    verb_1 = input("a past tense verb: ")
    name_1 = input("name: ")
    noun_3 = input("noun: ")
    adjective_1 = input("adjective: ")
    verb_2 = input("a past tense verb: ")
    place_1 = input("place: ")
    
    # Generate and display the story based on the user inputs
    print(f"""The {noun_1} fell from the {noun_2} and {verb_1} {name_1}'s {noun_3}.
{name_1} was {adjective_1} at the {noun_2}, so {name_1} {verb_2} all the {noun_1} down.
{name_1} then took all the {noun_1} to {place_1} to make {noun_1} pie.
{name_1} and {name_1}'s family enjoyed a nice meal.""")
