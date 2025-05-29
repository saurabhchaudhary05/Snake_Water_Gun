'''
1 for snake
-1 for water
0 for gun
'''

import random  # For computer's random choice

# List of possible choices
choices = ["s", "w", "g"]

# Mapping user input to values
youDict = {"s": 1, "w": -1, "g": 0}
revDict = {1: "snake", -1: "water", 0: "gun"}

# Initialize scores
your_score = 0
computer_score = 0
rounds = 0

while True:
    # Take user input
    youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    
    # Check if input is valid
    if youstr not in youDict:
        print("Invalid input. Try again")
        continue

    you = youDict[youstr]

    # Computer's random choice
    computer_choice = random.choice(choices)
    computer = youDict[computer_choice]

    print(f"Computer chose: {revDict[computer]}")

    # Determine the winner and update scores
    if computer == you:
        print("Draw")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("Computer won this round")
        computer_score += 1
    else:
        print("You won this round")
        your_score += 1

    rounds += 1  # Count the round

    # Ask if the user wants to continue
    c = input("Do you want to continue? (yes or no): ").lower()
    if c != 'yes':
        break

# Final results
print("\n--- Game Over ---")
print(f"Total Rounds Played: {rounds}")
print(f"Your Score: {your_score}")
print(f"Computer's Score: {computer_score}")

if your_score > computer_score:
    print("🎉 You won the game!")
elif computer_score > your_score:
    print("💻 Computer won the game!")
else:
    print("🤝 It's a draw!")
