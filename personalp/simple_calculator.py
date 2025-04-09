def run_simple_calculator():
    """Runs the simple calculator that performs basic math operations."""
    print("Project: Simple Calculator")
    print("This project performs basic mathematical operations, including addition, subtraction, multiplication, division, exponentiation, floor division, and modulus.")
    print("What I learned: How to calculate using code.")
    print("Programming process: Fairly easy.")
    
    # User inputs two numbers for calculation
    number_1 = float(input("Type a number: "))
    number_2 = float(input("Type another number: "))
    
    # Performing and displaying the calculations
    print(f"{number_1} plus {number_2} equals {number_1 + number_2}")
    print(f"{number_1} minus {number_2} equals {number_1 - number_2}")
    print(f"{number_1} times {number_2} equals {number_1 * number_2}")
    print(f"{number_1} divided by {number_2} equals {number_1 / number_2}")
    print(f"{number_1} to the power of {number_2} equals {number_1 ** number_2}")
    print(f"{number_1} divided by {number_2} and rounded down equals {number_1 // number_2}")
    print(f"{number_1} mod {number_2} equals {number_1 % number_2}")
