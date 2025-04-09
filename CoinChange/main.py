from coin_utils import load_coin_denominations
from solver import coin_change
from display import show_available_countries, show_coin_result

def main():
    countries = load_coin_denominations()
    

    if not countries:
        print("No country data loaded. Exiting.")
        return

    while True:
        show_available_countries(countries)

        country = input("Enter the country (or 'exit' to quit): ").strip().lower()
        if country == "exit":
            print("Goodbye!")
            break

        if country not in countries:
            print("Invalid country. Please choose from the list.")
            continue

        while True:
            try:
                target = float(input("Enter the target amount (or -1 to choose another country): ").strip())
                if target == -1:
                    break

                result = coin_change(target, countries[country])
                show_coin_result(result)
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

                countries = load_coin_denominations()



if __name__ == "__main__":
    main()
