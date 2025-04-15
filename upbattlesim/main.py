from characters import character_menu
from battle import battle_menu
from file import save_characters, load_characters, get_characters_dataframe
from utils import plot_character_stats, display_stat_analysis
from analysis import analyze_characters

def main():
    load_characters()
    while True:
        print("\n--- RPG Character Manager ---")
        print("1. Manage Characters")
        print("2. Battle")
        print("3. Save Characters")
        print("4. Exit")
        print("5. View Stats & Visualizations")
        print("6. Analyze Character Stats")  # Added for analysis
        option = input("Choose an option: ")
        if option == '1':
            character_menu()
        elif option == '2':
            battle_menu()
        elif option == '3':
            save_characters()
            print("Characters saved.")
        elif option == '4':
            save_characters()
            print("Goodbye!")
            break
        elif option == '5':
            df = get_characters_dataframe()
            if df.empty:
                print("No character data available.")
            else:
                print("Available characters:")
                print(df['name'].tolist())
                name = input("Enter character name to visualize: ")
                char = df[df['name'] == name].to_dict(orient='records')
                if char:
                    plot_character_stats(char[0])
                display_stat_analysis(df)
        elif option == '6':  # Triggering analysis
            analyze_characters()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
