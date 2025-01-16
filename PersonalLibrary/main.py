#define an empty list to store the books
library = []

#function to add a new book to the library
def add_book():

    #ask the user for book details
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    
    #create a dictionary representing the book
    new_book = {"title": title, "author": author}
    
    #add the new book to the library list
    library.append(new_book)
    print(f"'{title}' by {author} has been added to your library.")

#function to search for a book by title or author
def search_books():

    #ask the user for a search term (title or author)
    search_term = input("Enter the title or author to search for: ").lower()
    
    #initialize a list to store search results
    results = []
    
    #loop through all books in the library
    for book in library:

        #if the search term matches either the title or the author (which is case insensitive)
        if search_term in book["title"].lower() or search_term in book["author"].lower():

            results.append(book)  #add the matching book to results
    
    #check if any books were found
    if results:
        print("Found the following books:")
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found matching your search.")

#function to remove a book from the library by title
def remove_book():

    #ask the user for the title of the book to remove
    title = input("Enter the title of the book you want to remove: ")
    
    #loop through the books in the library
    for book in library:

        if book["title"].lower() == title.lower():  #match the title (which is case insensitive)

            library.remove(book)  #remove the book from the list

            print(f"'{title}' has been removed from your library.")
            return  #exit the function after removing the book
    
    #if no matching book is found
    print(f"'{title}' not found in your library.")

#function to display all books in the library
def display_books():

    #check if the library is empty
    if library:
        print("\nYour library contains the following books:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("Your library is empty.")

#function that runs the main program and displays the menu options
def run_program():
    while True:

        #display the menu of options
        print("\nLibrary Catalog Menu:")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Remove a book")
        print("4. Display all books")
        print("5. Exit")
        
        #get the user's choice
        choice = input("Please choose an option (1-5): ")
        
        #call the appropriate function based on user's choice
        if choice == '1':

            add_book()  #add a new book to the library
        elif choice == '2':

            search_books()  #search for books by title or author
        elif choice == '3':

            remove_book()  #remove a book from the library
        elif choice == '4':

            display_books()  #display all books in the library
        elif choice == '5':

            print("Exiting the program. Goodbye!")  #exit the program
            break  #break the loop to exit the program
        else:

            print("Invalid choice. Please select a valid option.")  #invalid choice handler

#run the program
