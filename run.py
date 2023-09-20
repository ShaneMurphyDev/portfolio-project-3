# Name Input
name = input('Please enter your name > ')
print(f'Hello {name}. Welcome to my game. I hope you enjoy your time here.')

# Main Menu
while True:
start = input('Start the game, or learn how to play first? Start/Learn > ')
if start == 'Start':
    print(f'Okay, {name}. Let us begin.')
    break
elif start == 'Learn':
    print("")
    print("The objective of this game is to surive and escape the tundra")
    print("You will be prompted to make decisions along the way")
    print("Type your answers and hit enter make a choice")
    print("Survive untill the end to win the game")
    print("Make the wrong choice and perish")
    print("Good luck.")
    print("")
else:
    print("Invalid choice. Please enter 'Start' or 'Learn'.")