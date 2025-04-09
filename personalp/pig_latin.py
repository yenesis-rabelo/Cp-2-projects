# pig_latin.py

def run_pig_latin():
    """Converts a word entered by the user to Pig Latin."""
    print("Project: Pig Latin Assignment")
    print("This project converts words into Pig Latin.")
    print("What I learned: What in the world Pig Latin was and how to do it.")
    print("Programming process: Simple!")
    
    def pig_latin(word):
        """Converts a given word to Pig Latin.""" 
        vowels = "aeiouAEIOU"
        
        # If the word starts with a vowel, append "way" to it
        if word[0] in vowels:
            return word + "way"
        
        # If the word starts with a consonant, move the first consonant(s) to the end and add "ay"
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
        
        # If the word has no vowels, return the word with "ay"
        return word + "ay"
    
    word = input("Enter a word to convert to Pig Latin: ")
    print(f"Pig Latin: {pig_latin(word)}")
