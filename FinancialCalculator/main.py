#Yenesis Rabelo Financial Calculator 

def time_to_save(goal_amount, deposit, period_type="monthly"):
    if period_type == "monthly":
        return goal_amount / deposit
    elif period_type == "weekly":
        return goal_amount / (deposit * 4)
    else:
        return "Invalid period type. Choose 'weekly' or 'monthly'."


def compound_interest(principal, rate, time, compounds_per_year=1):
    A = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    return A


def budget_allocator(income, categories_percentages):
    budget = {}
    for category, percentage in categories_percentages.items():
        budget[category] = income * (percentage / 100)
    return budget


def sale_price(original_price, discount):
    return original_price - (original_price * discount / 100)


def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)


#example usage:
if __name__ == "__main__":
    #time to save example
    print("Time to save for goal:", time_to_save(5000, 200, "monthly"), "months")
    
    #compound interest example
    print("Compound Interest:", compound_interest(1000, 0.05, 5))  #$1000 at 5% for 5 years
    
    #budget allocator example
    categories = {'savings': 30, 'entertainment': 20, 'food': 50}
    print("Budget Allocator:", budget_allocator(3000, categories))
    
    #sale price example
    print("Sale price:", sale_price(100, 20))  #20% discount on $100
    
    #tip calculator example
    print("Tip:", calculate_tip(150, 15))  #15% tip on $150