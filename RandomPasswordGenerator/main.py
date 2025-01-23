#Yenesis Rabelo Random Password Generator Assignment

import random
import string


# Function to generate a password based on user input
def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    # Create possible character sets based on user preferences
    char_set = ''
    
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_numbers:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation
    
    if len(char_set) == 0:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password by randomly selecting characters from the char_set
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password


# Function to run the program
def main():
    # Ask the user for their requirements
    print("Password Generator")


    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'


    # Generate four possible passwords
    passwords = [generate_password(length, use_upper, use_lower, use_numbers, use_special) for _ in range(4)]


    # Display the generated passwords
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, 1):
        print(f"{idx}. {password}")


if __name__ == "__main__":
    main()
