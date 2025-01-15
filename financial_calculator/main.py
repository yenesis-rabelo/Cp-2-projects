def calculate_savings_time(goal_amount, deposit, deposit_frequency):
    if deposit_frequency == 'weekly':
        time_to_save = goal_amount / deposit  # Weeks required
    elif deposit_frequency == 'monthly':
        time_to_save = goal_amount / deposit  # Months required
    return time_to_save

def calculate_compound_interest(principal, annual_rate, years, compounds_per_year):
    # Compound interest formula: A = P(1 + r/n)^(nt)
    rate_per_period = annual_rate / compounds_per_year
    periods = compounds_per_year * years
    amount = principal * (1 + rate_per_period) ** periods
    return amount

def allocate_budget(income, savings_percent, entertainment_percent, food_percent):
    savings = income * (savings_percent / 100)
    entertainment = income * (entertainment_percent / 100)
    food = income * (food_percent / 100)
    return savings, entertainment, food

def calculate_sale_price(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    return sale_price

def calculate_tip(meal_cost, tip_percent):
    tip_amount = meal_cost * (tip_percent / 100)
    return tip_amount

def main():
    while True:
        print("\nFinancial Calculations Menu:")
        print("1. How long will it take to save for a goal?")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == '1':
            goal_amount = float(input("Enter your savings goal amount: $"))
            deposit = float(input("Enter your weekly or monthly deposit amount: $"))
            deposit_frequency = input("Is your deposit weekly or monthly? ").lower()
            time_to_save = calculate_savings_time(goal_amount, deposit, deposit_frequency)
            print(f"It will take {time_to_save:.2f} {deposit_frequency} to reach your goal.")

        elif choice == '2':
            principal = float(input("Enter the principal amount: $"))
            annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
            years = int(input("Enter the number of years: "))
            compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))
            final_amount = calculate_compound_interest(principal, annual_rate / 100, years, compounds_per_year)
            print(f"The final amount after {years} years is: ${final_amount:.2f}")

        elif choice == '3':
            income = float(input("Enter your monthly income: $"))
            savings_percent = float(input("Enter the percentage for savings: "))
            entertainment_percent = float(input("Enter the percentage for entertainment: "))
            food_percent = float(input("Enter the percentage for food: "))
            savings, entertainment, food = allocate_budget(income, savings_percent, entertainment_percent, food_percent)
            print(f"Your budget allocation is as follows:")
            print(f"Savings: ${savings:.2f}")
            print(f"Entertainment: ${entertainment:.2f}")
            print(f"Food: ${food:.2f}")

        elif choice == '4':
            original_price = float(input("Enter the original price: $"))
            discount_percent = float(input("Enter the discount percentage: "))
            sale_price = calculate_sale_price(original_price, discount_percent)
            print(f"The sale price after the discount is: ${sale_price:.2f}")

        elif choice == '5':
            meal_cost = float(input("Enter the cost of your meal: $"))
            tip_percent = float(input("Enter the tip percentage: "))
            tip_amount = calculate_tip(meal_cost, tip_percent)
            print(f"The tip amount is: ${tip_amount:.2f}")

        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

