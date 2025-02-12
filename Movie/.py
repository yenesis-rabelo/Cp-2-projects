# Movie data stored as a list of dictionaries for easy searching
movies = [
    {"title": "Hugo", "director": "Martin Scorsese", "genre": "Adventure/Drama", "rating": "PG", "length": 126, "actors": ["Asa Butterfield", "Chloë Grace Moretz"]},
    {"title": "Divergent", "director": "Neil Burger", "genre": "Sci-Fi/Action", "rating": "PG-13", "length": 139, "actors": ["Shailene Woodley", "Theo James"]},
    {"title": "The Intouchables", "director": "Olivier Nakache, Éric Toledano", "genre": "Biography/Comedy", "rating": "R", "length": 112, "actors": ["François Cluzet", "Omar Sy"]},
    {"title": "The Spectacular Now", "director": "James Ponsoldt", "genre": "Drama/Romance", "rating": "R", "length": 95, "actors": ["Miles Teller", "Shailene Woodley"]},
    {"title": "Fantastic Beasts and Where to Find Them", "director": "David Yates", "genre": "Fantasy/Adventure", "rating": "PG-13", "length": 133, "actors": ["Eddie Redmayne", "Katherine Waterston"]},
    {"title": "The Edge of Seventeen", "director": "Kelly Fremon Craig", "genre": "Comedy/Drama", "rating": "R", "length": 104, "actors": ["Hailee Steinfeld", "Woody Harrelson"]},
    {"title": "Kubo and the Two Strings", "director": "Travis Knight", "genre": "Animation/Adventure", "rating": "PG", "length": 101, "actors": ["Charlize Theron", "Art Parkinson"]},
    {"title": "Hunt for the Wilderpeople", "director": "Taika Waititi", "genre": "Adventure/Comedy", "rating": "PG-13", "length": 101, "actors": ["Sam Neill", "Julian Dennison"]},
    {"title": "Midnight in Paris", "director": "Woody Allen", "genre": "Romance/Fantasy", "rating": "PG-13", "length": 94, "actors": ["Owen Wilson", "Rachel McAdams"]},
    {"title": "Persepolis", "director": "Marjane Satrapi, Vincent Paronnaud", "genre": "Animation/Biography", "rating": "PG-13", "length": 96, "actors": ["Chiara Mastroianni", "Catherine Deneuve"]},
    {"title": "Me and Earl and the Dying Girl", "director": "Alfonso Gomez-Rejon", "genre": "Comedy/Drama", "rating": "PG-13", "length": 105, "actors": ["Thomas Mann", "Olivia Cooke"]},
    {"title": "Paddington", "director": "Paul King", "genre": "Comedy/Family", "rating": "PG", "length": 95, "actors": ["Hugh Bonneville", "Sally Hawkins"]},
    {"title": "The Book Thief", "director": "Brian Percival", "genre": "Drama/War", "rating": "PG-13", "length": 131, "actors": ["Sophie Nélisse", "Geoffrey Rush"]},
    {"title": "Before Sunrise", "director": "Richard Linklater", "genre": "Romance/Drama", "rating": "R", "length": 101, "actors": ["Ethan Hawke", "Julie Delpy"]},
    {"title": "The Giver", "director": "Phillip Noyce", "genre": "Sci-Fi/Drama", "rating": "PG-13", "length": 97, "actors": ["Brenton Thwaites", "Jeff Bridges"]},
    {"title": "Akeelah and the Bee", "director": "Doug Atchison", "genre": "Drama", "rating": "PG", "length": 112, "actors": ["Keke Palmer", "Laurence Fishburne"]},
    {"title": "The Outsiders", "director": "Francis Ford Coppola", "genre": "Drama/Crime", "rating": "PG-13", "length": 91, "actors": ["C. Thomas Howell", "Matt Dillon"]},
    {"title": "The Diving Bell and the Butterfly", "director": "Julian Schnabel", "genre": "Biography/Drama", "rating": "PG-13", "length": 112, "actors": ["Mathieu Amalric", "Emmanuelle Seigner"]},
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "genre": "Animation/Adventure", "rating": "PG", "length": 125, "actors": ["Daveigh Chase", "Suzanne Pleshette"]},
    {"title": "Eighth Grade", "director": "Bo Burnham", "genre": "Comedy/Drama", "rating": "R", "length": 93, "actors": ["Elsie Fisher", "Josh Hamilton"]},
    {"title": "To Kill a Mockingbird", "director": "Robert Mulligan", "genre": "Drama", "rating": "Not Rated", "length": 129, "actors": ["Gregory Peck", "Mary Badham"]},
    {"title": "Snowpiercer", "director": "Bong Joon-ho", "genre": "Sci-Fi/Action", "rating": "R", "length": 126, "actors": ["Chris Evans", "Tilda Swinton"]},
    {"title": "The Way Way Back", "director": "Nat Faxon, Jim Rash", "genre": "Comedy/Drama", "rating": "PG-13", "length": 103, "actors": ["Liam James", "Sam Rockwell"]},
    {"title": "Boyhood", "director": "Richard Linklater", "genre": "Drama", "rating": "R", "length": 165, "actors": ["Ellar Coltrane", "Patricia Arquette"]},
    {"title": "The Curious Case of Benjamin Button", "director": "David Fincher", "genre": "Drama/Fantasy", "rating": "PG-13", "length": 166, "actors": ["Brad Pitt", "Cate Blanchett"]},
    {"title": "Selma", "director": "Ava DuVernay", "genre": "Biography/Drama", "rating": "PG-13", "length": 128, "actors": ["David Oyelowo", "Carmen Ejogo"]},
    {"title": "The Princess and the Frog", "director": "Ron Clements, John Musker", "genre": "Animation/Family", "rating": "G", "length": 97, "actors": ["Anika Noni Rose", "Keith David"]},
    {"title": "The Kite Runner", "director": "Marc Forster", "genre": "Drama", "rating": "PG-13", "length": 128, "actors": ["Khalid Abdalla", "Zekeria Ebrahim"]},
    {"title": "The Secret Life of Walter Mitty", "director": "Ben Stiller", "genre": "Adventure/Comedy", "rating": "PG", "length": 114, "actors": ["Ben Stiller", "Kristen Wiig"]},
    {"title": "Moonrise Kingdom", "director": "Wes Anderson", "genre": "Comedy/Drama", "rating": "PG-13", "length": 94, "actors": ["Jared Gilman", "Kara Hayward"]},
    {"title": "The Farewell", "director": "Lulu Wang", "genre": "Comedy/Drama", "rating": "PG", "length": 100, "actors": ["Awkwafina", "Tzi Ma"]},
    {"title": "The Hundred-Foot Journey", "director": "Lasse Hallström", "genre": "Comedy/Drama", "rating": "PG", "length": 122, "actors": ["Helen Mirren", "Om Puri"]},
    {"title": "The Sisterhood of the Traveling Pants", "director": "Ken Kwapis", "genre": "Comedy/Drama", "rating": "PG", "length": 119, "actors": ["Amber Tamblyn", "Alexis Bledel"]},
    {"title": "Big Fish", "director": "Tim Burton", "genre": "Adventure/Drama", "rating": "PG-13", "length": 125, "actors": ["Ewan McGregor", "Albert Finney"]},
    {"title": "The Truman Show", "director": "Peter Weir", "genre": "Drama/Sci-Fi", "rating": "PG", "length": 103, "actors": ["Jim Carrey", "Laura Linney"]},
    {"title": "Bend It Like Beckham", "director": "Gurinder Chadha", "genre": "Comedy/Drama", "rating": "PG-13", "length": 112, "actors": ["Parminder Nagra", "Keira Knightley"]},
    {"title": "Life Is Beautiful", "director": "Roberto Benigni", "genre": "Comedy/Drama", "rating": "PG-13", "length": 116, "actors": ["Roberto Benigni", "Nicoletta Braschi"]}
]

def print_movies():
    """Function to print the list of all movies."""
    for movie in movies:
        print(f"Title: {movie['title']}, Director: {movie['director']}, Genre: {movie['genre']}, Length: {movie['length']} minutes")

def filter_movies(filters):
    """Function to filter movies based on given filters."""
    filtered_movies = movies
    for key, value in filters.items():
        filtered_movies = [movie for movie in filtered_movies if value.lower() in str(movie[key]).lower()]
    return filtered_movies

def get_recommendations():
    """Function to get movie recommendations based on user input."""
    print("Welcome to the Movie Recommendation Program!\n")
    
    print("Select filters for your recommendations. You can choose two or more filters:")
    print("1. Genre")
    print("2. Director")
    print("3. Length (minutes)")
    print("4. Actors")
    
    filters = {}
    filter_choices = [1, 2, 3, 4]
    
    while len(filters) < 2:
        choice = int(input("Enter the number of the filter you want to use (e.g., 1 for Genre): "))
        if choice not in filter_choices:
            print("Invalid choice. Please select a valid filter number.")
            continue
        if choice == 1:
            genre = input("Enter the genre you're interested in: ")
            filters["genre"] = genre
        elif choice == 2:
            director = input("Enter the director you're interested in: ")
            filters["director"] = director
        elif choice == 3:
            length = int(input("Enter the maximum length of movie (in minutes): "))
            filters["length"] = length
        elif choice == 4:
            actor = input("Enter the actor's name: ")
            filters["actors"] = actor
    
    print("\nFetching recommendations based on your filters...\n")
    recommended_movies = filter_movies(filters)
    if recommended_movies:
        for movie in recommended_movies:
            print(f"Title: {movie['title']}, Director: {movie['director']}, Genre: {movie['genre']}, Length: {movie['length']} minutes")
    else:
        print("No movies found that match your filters.")

# Option to print the entire movie list or get recommendations
while True:
    print("\n1. Print all movies")
    print("2. Get movie recommendations")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print_movies()
    elif choice == 2:
        get_recommendations()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
