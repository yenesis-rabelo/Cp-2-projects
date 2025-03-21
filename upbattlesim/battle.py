def battle(char1, char2):
    """Simulate a battle between two characters."""
    print(f"\n{char1[0]} vs {char2[0]} - Battle Start!")
    
    while char1[1] > 0 and char2[1] > 0:
        if char1[4] >= char2[4]:
            char2[1] -= max(1, char1[2] - char2[3])
            if char2[1] <= 0:
                print(f"{char1[0]} wins!")
                return char1
            char1[1] -= max(1, char2[2] - char1[3])
        else:
            char1[1] -= max(1, char2[2] - char1[3])
            if char1[1] <= 0:
                print(f"{char2[0]} wins!")
                return char2
            char2[1] -= max(1, char1[2] - char2[3])

    return char1 if char1[1] > 0 else char2
