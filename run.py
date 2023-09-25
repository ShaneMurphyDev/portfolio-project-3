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
    while True:
        firstPath = input("Please choose Mountain/Cave/River > ")
        if firstPath == 'Mountain':
            path1()
            break
        elif firstPath == 'Cave':
            print("cave")
            path2()
        elif firstPath == 'River':
            print("river")
            path3()
        else:
            print("")
            print("Invalid choice. Enter 'Mountain' 'Cave' or 'River'.")
            print("")


def retry():
    retry = input("You have died. Would you like to try again? Yes/No")
    if retry == 'Yes':
        intro()
    elif start == 'No':
        print("=== GAME OVER ===")


def path1():
    print("")
    print("Though not steep by any means, walking uphill is difficult")
    print("You get a good view of the surrounding area")
    print('"Its even colder up here...I cant stay here.."')
    print("You see the dim lights of the reseach station on the horizon")
    print("Before you lies 2 possible paths")
    print("Keep going up, follow the mountain back down on the other side")
    print("Follow a ledge that straddles around the mountain")
    while True:
        firstPath = input("Please choose Upward/Ledge > ")
        if firstPath == 'Upward':
            path1_1()
            break
        elif firstPath == 'Ledge':
            path1_2()
        else:
            print("")
            print("Invalid choice. Please enter 'Left' or 'Right'")
            print("")


def path1_1():
    print("")
    print("You choose to go further up the mountain")
    print("Minutes turn to hours")
    print("your legs start to feel like stone")
    print("The peak is not in sight")
    print('"so...tired..."')
    print("Your vision begins to fade")
    print("This is how you died")
    print("Frozen, near the peak of this mountain")
    retry()


def path1_2():
    print("")
    print("You choose to follow the narrow ledge around the mountain")
    print("Thankfully, you manage to keep your balance")
    print("after crossing to the other side")
    print("youre brought to a decline youre able to slide down")
    print("it brings you to an open clearing in the forest")
    path_clearing()


def path2():
    print("")
    print("You enter the cave, the temperature is slightly warmer")
    print("As you follow the cave the path narrows")
    print("Before you lies two paths")
    print("To the left there is a path that narrows")
    print("You think you could just about squeeze through")
    print("To the right the path curves around a corner")
    while True:
        secondPath = input("Please choose Left/Right > ")
        if secondPath == 'Left':
            path2_1()
            break
        elif secondPath == 'Right':
            path2_2()
        else:
            print("")
            print("Invalid choice. Please enter 'Left' or 'Right'")
            print("")


def path2_1():
    print("")
    print("You choose to follow the narrow cave path")
    print("You get anxious as it closes in around you")
    print("After a few minutes you come to a dead end")
    print("Theres a small hole in the wall")
    print("After climbing through the cave opens up again")
    print("You follow the cold breeze")
    print("It leads you back outside")
    print("Youre on the other side of the mountain")
    print("an open clearing lies ahead")
    path_clearing()


def path2_2():
    print("")
    print("You choose to follow the right path")
    print("After a few minutes of walking")
    print("You come to an open cavern")
    print("Foliage litters the floor and...")
    print("bones!! as you begin to turn around")
    print("a large creature emerges, a grizzly bear")
    print("before you can even start running you feel claws in your back")
    print("The bear tears you apart and eats you")
    retry()


def path3():
    print("")
    print("You choose to follow the river")
    print("It takes you in the general direction you need to go")
    print("The further you go, the wider the river is getting")
    print("Before you lies two paths")
    print("Continue following the widening river")
    print("Cross now, over the ice")
    while True:
        thirdPath = input("Please choose Follow/Cross > ")
        if thirdPath == 'Follow':
            path3_1()
            break
        elif thirdPath == 'Cross':
            path3_2()
        else:
            print("")
            print("Invalid choice. Please enter 'Follow' or 'Cross'")
            print("")


def path3_1():
    print("")
    print("You follow the winding river")
    print("After what seems like an hour it starts to narrow again")
    print("You find and old wooden bridge that seems safe to cross")
    print("After crossing you find an open clearing")
    path_clearing()


def path3_2():
    print("")
    print("You choose to cross the river")
    print("As you slowly make your way across the ice")
    print("You feel it crack, and the sound sends a shiver up your spine")
    print("Suddenly it gives out and youre plunged into the dark water!")
    print("The freezing cold enters every part of your body")
    print("Unable to pull yourself back out")
    print("This is where you die")
    print("Drowned in the depths")
    retry()


def path_clearing():
    print("")
    print('"im exhausted...need..to keep going.."')
    print("as you arrive in the clearing you take a few minutes to rest")
    print("your body temperature has been steadily dropping")
    print("hunger and thirst are setting in")
    print("you observe the nearby area")
    print("before you lies 3 paths")
    print("A forest, with a snow topped canopy")
    print("A rocky field, filled stones from small to huge")
    print("A swampy marsh, looking empty and barren")
    while True:
        clearingPath = input("Please choose Forest/Field/Marsh > ")
        if clearingPath == 'Forest':
            clearingPath_1()
            break
        elif clearingPath == 'Field':
            clearingPath_2()            
        elif clearingPath == 'Marsh':
            clearingPath_3()
        else:
            print("")
            print("Invalid choice. Please enter 'Forest' 'Field' or 'Marsh'")
            print("")


def clearingPath_1():
    print("")
    print("You choose to enter the forest")
    print("The deeper you go, the darker it gets")
    print("light fades to black")
    print("you lose all notion of direction")
    print("a chorus of growling fills the air")
    print("you are set upon by a wolf pack")
    print("In a flurry of teeth and claw you are ripped to shreds")
    print("This is how you died")
    print("Eaten, alone, in the depths of the forest")
    retry()


def clearingPath_2():
    print("")
    print("You choose to cross the stoney field")
    print("The terrain is rough, often needing to climb over rocks")
    print("as you make your way through it begins to settle")
    print("it starts to settle and return to a flat field with a hill")
    print("you reach the top of the hill and look around")
    print("there are two points of interest ahead")
    print("a log cabin, no lights, snow covered roof")
    print("a vehicle, car maybe, also covered in snow")
    print("you know you only have to energy to travel to one")        


def clearingPath_3():
    print("")
    print("You choose to enter the marsh")
    print("Open air")
    print("walking feels easier")
    print("the dirt beneath your feet is soft")
    print("you realize, too late, you are in the middle of a mud lake")
    print("your feet are stuck, and going deeper")
    print("as the mud gets to your torso you know its over")
    print("This is how you died")
    print("Sunken, drowned in a lake of mud")
    retry()


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
