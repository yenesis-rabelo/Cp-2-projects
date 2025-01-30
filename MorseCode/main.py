#Yenesis Rabelo Morse Code Assignment 

# List of English characters (uppercase) and their corresponding Morse code symbols
english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']


# Function to translate English text to Morse code
def english_to_morse(english_text):
    # Convert input text to uppercase and split into individual characters
    english_text = english_text.upper()
    morse_text = []
    
    # Loop through each character in the English text
    for char in english_text:
        # Check if the character is in the alphabet
        if char in english_alphabet:
            # Find the index of the character and append corresponding Morse code symbol
            morse_text.append(morse_code[english_alphabet.index(char)])
        elif char == ' ':
            # Handle spaces by adding a space
            morse_text.append(' ')
        else:
            # Handle any non-alphabetic characters
            print(f"Error: '{char}' not valid in Morse code.")
            return None
    
    # Join the Morse code symbols with a space separator and return the result
    return ' '.join(morse_text)


# Function to translate Morse code to English text
def morse_to_english(morse_text):
    # Split the Morse code into individual symbols
    morse_symbols = morse_text.split(' ')
    english_text = []
    
    # Loop through each Morse symbol
    for symbol in morse_symbols:
        # Check if the symbol is valid
        if symbol in morse_code:
            # Find the index of the Morse code symbol and append corresponding English character
            english_text.append(english_alphabet[morse_code.index(symbol)])
        elif symbol == '':
            # Handle spaces between words
            english_text.append(' ')
        else:
            # Handle any invalid Morse code symbols
            print(f"Error: '{symbol}' not valid in Morse code.")
            return None
    
    # Join the English characters to form the text
    return ''.join(english_text)


# Main function to interact with the user
def main():
    while True:
        # Display options for the user
        print("Welcome to the English-Morse Code Translator!")
        print("1. Translate English to Morse Code")
        print("2. Translate Morse Code to English")
        print("3. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Get the text from the user and translate it to Morse code
            english_text = input("Enter text to translate to Morse Code: ")
            translated_morse = english_to_morse(english_text)
            if translated_morse:
                print(f"Morse Code: {translated_morse}")
        
        elif choice == '2':
            # Get the Morse code from the user and translate it to English
            morse_text = input("Enter Morse Code to translate to English: ")
            translated_english = morse_to_english(morse_text)
            if translated_english:
                print(f"English Text: {translated_english}")
        
        elif choice == '3':
            # Exit the program
            print("Exiting program...")
            break
        
        else:
            # Handle invalid choice
            print("Invalid choice. Please select 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()






