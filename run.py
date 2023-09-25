# Name Input
print("")
print("#====================#")
print("#                    #")
print("#      SNOWFALL      #")
print("#                    #")
print("#====================#")
print("")
name = input('Please enter your name > ')
print(f'Hello {name}. Welcome to my game. I hope you enjoy your time here.')


def intro():
    print("")
    print("")
    print("Your vision is...blurry")
    print("Ears ringing..")
    print("Everything feels heavy and tired")
    print("As your vision clears you can make out some silhouettes")
    print("An orange flickering light to your right")
    print("A chill runs through your body")
    print("There is a mechanical wreck 30 meters away")
    print("Its a small aircraft, its on fire")
    print('"Right...the storm..."')
    print("You look down at yourself and see a badge")
    print('"Forest Ranger"')
    print("You start to recall the crash")
    print("A blur or lights flashing and alarms ringing")
    print("You were on your way to an isolated research center")
    print("You did your best to land safely but the tree line..")
    print("made that impossible")
    print("You pick yourself up from the ground")
    print("I need to get to the research station..12 miles east")
    print("Before you lies 3 paths")
    print("Continue further up the mountain, shortest but most direct route")
    print("Enter the cave just ahead, could be good shelter")
    print("Follow the iced over river")
    print("")
    firstPath = input("Please choose Mountain/Cave/River > ")
    if firstPath == 'Mountain':
        print("mountain")
        path1()
    elif firstPath == 'Cave':
        print("cave")
        path2()
    elif firstPath == 'River':
        print("river")
        path3()


def path1():
    print("")


def path1_1():
    print("")


def path1_2():
    print("")


def path2():
    print("")


def path2_1():
    print("")


def path2_2():
    print("")


def path3():
    print("")


def path3_1():
    print("")


def path3_2():
    print("")


# Main Menu
while True:
    start = input('Start the game, or learn how to play first? Start/Learn > ')
    if start == 'Start':
        intro()
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
        print("")
        print("Invalid choice. Please enter 'Start' or 'Learn'.")
        print("")