def run_quiz_game():
    """Runs a quiz game that tests knowledge about the Solar System."""
    print("Project: Quiz Creation ProficiencyTest")
    print("This project tests your knowledge about the Solar System.")
    print("What I learned: How cool coding really was.")
    print("Programming process: Fairly easy.")
    
    score = 0  # Initialize the score
    
    # Define the first question with options and the correct answer
    question1 = {
        "question": "What is the largest planet in our solar system?",
        "options": {
            "A": "Earth",
            "B": "Jupiter",
            "C": "Saturn",
            "D": "Mars"
        },
        "correct_answer": "B"
    }
    
    # Define a second, easier question
    easier_question = {
        "question": "Which planet is closest to the Sun?",
        "options": {
            "A": "Mercury",
            "B": "Venus",
            "C": "Earth",
            "D": "Mars"
        },
        "correct_answer": "A"
    }
    
    def ask_question(question):
        """Asks the user a question and checks if the answer is correct."""
        print(question["question"])
        for option, answer in question["options"].items():
            print(f"{option}: {answer}")
        user_answer = input("Your answer (A, B, C, D): ").upper()
        return user_answer == question["correct_answer"]
    
    # Ask the first question
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
    
    print(f"Your final score is: {score}/5")
    if score == 5:
        print("Excellent! You know a lot about the Solar System!")
    elif score >= 3:
        print("Good job! You have a decent understanding of the Solar System.")
    else:
        print("Keep studying! You can do better next time!")

