import os
import time

def get_file_path():
    """Prompt the user for a file name and return the file path."""
    file_name = input("Enter the file name (with extension): ")
    if not os.path.isfile(file_name):
        print("Error: File does not exist.")
        return None
    return file_name

def count_words_in_file(file_path):
    """Count the number of words in the specified file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return len(content.split())

def update_file_with_wordcount(file_path, word_count):
    """Append the word count and timestamp to the file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"\n\n[Word Count: {word_count} | Last Updated: {timestamp}]")

def main():
    """Main function to execute the program steps."""
    file_path = get_file_path()
    if not file_path:
        return
    
    word_count = count_words_in_file(file_path)
    print(f"Word count: {word_count}")
    
    update_file_with_wordcount(file_path, word_count)
    print("File updated successfully with word count and timestamp.")

if __name__ == "__main__":
    main()