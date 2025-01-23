# Function to display the menu
def display_menu():
    """Display the menu options to the user."""
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book by title")
    print("4. Remove a book")
    print("5. Exit")

# Function to add a new book to the library
def add_book(library):
    """Add a new book to the library catalog."""
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    # Create a dictionary for the book and add it to the library list
    book = {"title": title, "author": author}
    library.append(book)
    print(f'Book "{title}" added successfully!')

# Function to display all books in the library
def display_books(library):
    """Display all books in the library."""
    if not library:
        print("The library is empty.")
    else:
        print("\nBooks in the library:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}")

# Function to search for a book by title
def search_book(library):
    """Search for a book by title in the library."""
    title = input("Enter the title of the book to search for: ")
    found_books = [book for book in library if title.lower() in book["title"].lower()]
    
    if found_books:
        print("\nBooks found:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found with that title.")

# Function to remove a book from the library
def remove_book(library):
    """Remove a book from the library by its title."""
    title = input("Enter the title of the book to remove: ")
    book_to_remove = None
    
    # Search for the book in the library
    for book in library:
        if book["title"].lower() == title.lower():
            book_to_remove = book
            break
    
    if book_to_remove:
        library.remove(book_to_remove)
        print(f'Book "{title}" has been removed from the library.')
    else:
        print("Book not found. Cannot remove.")

# Function to run the program and handle user input
def run_library_system():
    """Run the library management system."""
    # List to store all books in the library
    library = []
    
    # Infinite loop to keep showing the menu until the user chooses to exit
    while True:
        # Display the menu options
        display_menu()
        
        # Get the user's choice
        choice = input("Enter the number of your choice: ")
        
        # Execute the corresponding action based on the user's choice
        if choice == '1':
            add_book(library)  # Add a new book
        elif choice == '2':
            display_books(library)  # Display all books
        elif choice == '3':
            search_book(library)  # Search for a book
        elif choice == '4':
            remove_book(library)  # Remove a book
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")

# Run the library management system
run_library_system()

