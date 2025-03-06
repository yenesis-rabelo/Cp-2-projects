# Function to display the menu
def display_menu():
    """Display the menu options to the user."""
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Display all books (Simple View)")
    print("3. Display all books (Detailed View)")
    print("4. Search for a book by title")
    print("5. Update a book's details")
    print("6. Remove a book")
    print("7. Exit")

# Function to add a new book to the library
def add_book(library):
    """Add a new book to the library catalog."""
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    rating = input("Enter the rating (out of 5): ")
    
    # Create a dictionary for the book and add it to the library list
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "rating": rating
    }
    library.append(book)
    print(f'Book "{title}" added successfully!')

# Function to display all books in the library (simple view)
def display_books_simple(library):
    """Display all books in the library (simple view: title and author)."""
    if not library:
        print("The library is empty.")
    else:
        print("\nBooks in the library (Simple View):")
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}")

# Function to display all books in the library (detailed view)
def display_books_detailed(library):
    """Display all books in the library (detailed view: all information)."""
    if not library:
        print("The library is empty.")
    else:
        print("\nBooks in the library (Detailed View):")
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Rating: {book['rating']}")

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

# Function to update a book's details
def update_book(library):
    """Update a book's details in the library."""
    title = input("Enter the title of the book to update: ")
    book_to_update = None
    
    # Search for the book in the library
    for book in library:
        if book["title"].lower() == title.lower():
            book_to_update = book
            break
    
    if book_to_update:
        print(f"Updating details for '{title}':")
        book_to_update["author"] = input(f"Enter new author (current: {book_to_update['author']}): ")
        book_to_update["year"] = input(f"Enter new year (current: {book_to_update['year']}): ")
        book_to_update["genre"] = input(f"Enter new genre (current: {book_to_update['genre']}): ")
        book_to_update["rating"] = input(f"Enter new rating (current: {book_to_update['rating']}): ")
        print(f"Book '{title}' has been updated.")
    else:
        print("Book not found. Cannot update.")

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
            display_books_simple(library)  # Display all books (simple view)
        elif choice == '3':
            display_books_detailed(library)  # Display all books (detailed view)
        elif choice == '4':
            search_book(library)  # Search for a book
        elif choice == '5':
            update_book(library)  # Update a book's details
        elif choice == '6':
            remove_book(library)  # Remove a book
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")

# Run the library management system
run_library_system()
