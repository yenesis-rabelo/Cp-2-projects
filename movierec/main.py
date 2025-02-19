import csv

def load_movies(file_path):
    """Load movies from a CSV file into a DataFrame."""
    return csv.reader(file_path)

def filter_movies(df, genre=None, director=None, min_length=None, max_length=None, actor=None):
    """Filter movies based on given criteria."""
    filtered_df = df
    
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if director:
        filtered_df = filtered_df[filtered_df['Director'].str.contains(director, case=False, na=False)]
    if min_length:
        filtered_df = filtered_df[filtered_df['Length (min)'] >= min_length]
    if max_length:
        filtered_df = filtered_df[filtered_df['Length (min)'] <= max_length]
    if actor:
        filtered_df = filtered_df[filtered_df['Notable Actors'].str.contains(actor, case=False, na=False)]
    
    return filtered_df

def print_movies(df):
    """Print the full list of movies."""
    print(df[['Title', 'Director', 'Genre', 'Length (min)', 'Notable Actors']].to_string(index=False))

def main():
    file_path = "/mnt/data/Movies list (1).csv"
    df = load_movies(file_path)
    
    print("Welcome to the Movie Recommendation System!")
    print("You can filter movies by Genre, Director, Length, and Actor.")
    
    genre = input("Enter a genre (or leave blank): ").strip()
    director = input("Enter a director's name (or leave blank): ").strip()
    min_length = input("Enter minimum movie length in minutes (or leave blank): ").strip()
    max_length = input("Enter maximum movie length in minutes (or leave blank): ").strip()
    actor = input("Enter an actor's name (or leave blank): ").strip()
    
    min_length = int(min_length) if min_length.isdigit() else None
    max_length = int(max_length) if max_length.isdigit() else None
    
    filtered_movies = filter_movies(df, genre, director, min_length, max_length, actor)
    
    if filtered_movies.empty:
        print("No movies found matching your criteria.")
    else:
        print("\nRecommended Movies:")
        print_movies(filtered_movies)
    
    print("\nFull movie list:")
    print_movies(df)

if __name__ == "__main__":
    main()
