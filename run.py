import sys
import time


# d = delay, creates time delay for text
d = 1.2


# Name Input
print("")
print("#====================#")
print("#                    #")
print("#      SNOWFALL      #")
print("#                    #")
print("#====================#")
print("")
time.sleep(d)
name = input('Please enter your name > ')
print(f'Hello {name}. Welcome to my game. I hope you enjoy your time here.')
print("")


#  Intro
def intro():
    print("")
    print("Your vision is...blurry")
    time.sleep(d)
    print("Ears ringing..")
    time.sleep(d)
    print("Everything feels heavy and tired")
    time.sleep(d)
    print("As your vision clears you can make out some silhouettes")
    time.sleep(d)
    print("An orange flickering light to your right")
    time.sleep(d)
    print("A chill runs through your body")
    time.sleep(d)
    print("There is a mechanical wreck 30 meters away")
    time.sleep(d)
    print("Its a small aircraft, its on fire")
    time.sleep(d)
    print('"Right...the storm..."')
    time.sleep(d)
    print("You look down at yourself and see a badge")
    time.sleep(d)
    print('"Forest Ranger"')
    time.sleep(d)
    print("You start to recall the crash")
    time.sleep(d)
    print("A blur or lights flashing and alarms ringing")
    time.sleep(d)
    print("You were on your way to an isolated research center")
    time.sleep(d)
    print("You did your best to land safely but the tree line..")
    time.sleep(d)
    print("made that impossible")
    time.sleep(d)
    print("You pick yourself up from the ground")
    time.sleep(d)
    print("I need to get to the research station..12 miles east")
    time.sleep(d)
    print("Before you lies 3 paths")
    time.sleep(d)
    print("Continue further up the mountain, shortest but most direct route")
    print("")
    print("Enter the cave just ahead, could be good shelter")
    print("")
    print("Follow the iced over river")
    print("")
    time.sleep(d)
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


# Retry funtion
def retry():
    retry = input('Its over. Would you like to try again? Yes/No /n')
    if retry == 'Yes':
        intro()
    elif start == 'No':
        print("=== GAME OVER ===")


# First Pathway
def path1():
    print("")
    print("Though not steep by any means, walking uphill is difficult")
    time.sleep(d)
    print("You get a good view of the surrounding area")
    time.sleep(d)
    print('"Its even colder up here...I cant stay here.."')
    time.sleep(d)
    print("You see the dim lights of the reseach station on the horizon")
    time.sleep(d)
    print("Before you lies 2 possible paths")
    time.sleep(d)
    print("Keep going up, follow the mountain back down on the other side")
    time.sleep(d)
    print("Follow a ledge that straddles around the mountain")
    print("")
    time.sleep(d)
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
    time.sleep(d)
    print("Minutes turn to hours")
    time.sleep(d)
    print("your legs start to feel like stone")
    time.sleep(d)
    print("The peak is not in sight")
    time.sleep(d)
    print('"so...tired..."')
    time.sleep(d)
    print("Your vision begins to fade")
    time.sleep(d)
    print("This is how you died")
    time.sleep(d)
    print("Frozen, near the peak of this mountain")
    print("")
    time.sleep(d)
    retry()


def path1_2():
    print("")
    print("You choose to follow the narrow ledge around the mountain")
    time.sleep(d)
    print("Thankfully, you manage to keep your balance")
    time.sleep(d)
    print("after crossing to the other side")
    time.sleep(d)
    print("youre brought to a decline youre able to slide down")
    time.sleep(d)
    print("it brings you to an open clearing in the forest")
    print("")
    time.sleep(d)
    path_clearing()


# 2nd Pathway
def path2():
    print("")
    print("You enter the cave, the temperature is slightly warmer")
    time.sleep(d)
    print("As you follow the cave the path narrows")
    time.sleep(d)
    print("Before you lies two paths")
    time.sleep(d)
    print("To the left there is a path that narrows")
    time.sleep(d)
    print("You think you could just about squeeze through")
    time.sleep(d)
    print("To the right the path curves around a corner")
    print("")
    time.sleep(d)
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
    time.sleep(d)
    print("You get anxious as it closes in around you")
    time.sleep(d)
    print("After a few minutes you come to a dead end")
    time.sleep(d)
    print("Theres a small hole in the wall")
    time.sleep(d)
    print("After climbing through the cave opens up again")
    time.sleep(d)
    print("You follow the cold breeze")
    time.sleep(d)
    print("It leads you back outside")
    time.sleep(d)
    print("Youre on the other side of the mountain")
    time.sleep(d)
    print("an open clearing lies ahead")
    print("")
    time.sleep(d)
    path_clearing()


def path2_2():
    print("")
    print("You choose to follow the right path")
    time.sleep(d)
    print("After a few minutes of walking")
    time.sleep(d)
    print("You come to an open cavern")
    time.sleep(d)
    print("Foliage litters the floor and...")
    time.sleep(d)
    print("bones!! as you begin to turn around")
    time.sleep(d)
    print("a large creature emerges, a grizzly bear")
    time.sleep(d)
    print("before you can even start running you feel claws in your back")
    time.sleep(d)
    print("The bear tears you apart and eats you")
    print("")
    time.sleep(d)
    retry()


# 3rd Pathway
def path3():
    print("")
    print("You choose to follow the river")
    time.sleep(d)
    print("It takes you in the general direction you need to go")
    time.sleep(d)
    print("The further you go, the wider the river is getting")
    time.sleep(d)
    print("Before you lies two paths")
    time.sleep(d)
    print("Continue following the widening river")
    time.sleep(d)
    print("Cross now, over the ice")
    print("")
    time.sleep(d)
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
    time.sleep(d)
    print("After what seems like an hour it starts to narrow again")
    time.sleep(d)
    print("You find and old wooden bridge that seems safe to cross")
    time.sleep(d)
    print("After crossing you find an open clearing")
    time.sleep(d)
    print("")
    path_clearing()


def path3_2():
    print("")
    print("You choose to cross the river")
    time.sleep(d)
    print("As you slowly make your way across the ice")
    time.sleep(d)
    print("You feel it crack, and the sound sends a shiver up your spine")
    time.sleep(d)
    print("Suddenly it gives out and youre plunged into the dark water!")
    time.sleep(d)
    print("The freezing cold enters every part of your body")
    time.sleep(d)
    print("Unable to pull yourself back out")
    time.sleep(d)
    print("This is where you die")
    time.sleep(d)
    print("Drowned in the depths")
    print("")
    time.sleep(d)
    retry()


# 4th Pathway
def path_clearing():
    print("")
    print('"im exhausted...need..to keep going.."')
    time.sleep(d)
    print("as you arrive in the clearing you take a few minutes to rest")
    time.sleep(d)
    print("your body temperature has been steadily dropping")
    time.sleep(d)
    print("hunger and thirst are setting in")
    time.sleep(d)
    print("you observe the nearby area")
    time.sleep(d)
    print("before you lies 3 paths")
    time.sleep(d)
    print("A forest, with a snow topped canopy")
    time.sleep(d)
    print("A rocky field, filled stones from small to huge")
    time.sleep(d)
    print("A swampy marsh, looking empty and barren")
    time.sleep(d)
    print("")
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
    time.sleep(d)
    print("The deeper you go, the darker it gets")
    time.sleep(d)
    print("light fades to black")
    time.sleep(d)
    print("you lose all notion of direction")
    time.sleep(d)
    print("a chorus of growling fills the air")
    time.sleep(d)
    print("you are set upon by a wolf pack")
    time.sleep(d)
    print("In a flurry of teeth and claw you are ripped to shreds")
    time.sleep(d)
    print("This is how you died")
    time.sleep(d)
    print("Eaten, alone, in the depths of the forest")
    print("")
    time.sleep(d)
    retry()


def clearingPath_3():
    print("")
    print("You choose to enter the marsh")
    time.sleep(d)
    print("Open air")
    time.sleep(d)
    print("walking feels easier")
    time.sleep(d)
    print("the dirt beneath your feet is soft")
    time.sleep(d)
    print("you realize, too late, you are in the middle of a mud lake")
    time.sleep(d)
    print("your feet are stuck, and going deeper")
    time.sleep(d)
    print("as the mud gets to your torso you know its over")
    time.sleep(d)
    print("This is how you died")
    time.sleep(d)
    print("Sunken, drowned in a lake of mud")
    print("")
    time.sleep(d)
    retry()


# 5th Pathway
def clearingPath_2():
    print("")
    print("You choose to cross the stoney field")
    time.sleep(d)
    print("The terrain is rough, often needing to climb over rocks")
    time.sleep(d)
    print("as you make your way through it begins to settle")
    time.sleep(d)
    print("it starts to settle and return to a flat field with a hill")
    time.sleep(d)
    print("you reach the top of the hill and look around")
    time.sleep(d)
    print("there are two points of interest ahead")
    time.sleep(d)
    print("a log cabin, no lights, snow covered roof")
    time.sleep(d)
    print("a vehicle, car maybe, also covered in snow")
    time.sleep(d)
    print("you know you only have to energy to travel to one")
    print("")
    time.sleep(d)
    while True:
        thirdPath = input("Please choose Cabin/Car > ")
        if thirdPath == 'Cabin':
            cabin()
            break
        elif thirdPath == 'Car':
            car()
        else:
            print("")
            print("Invalid choice. Please enter 'Cabin' or 'Car'")
            print("")


def car():
    print("")
    print("You choose to head towards the car")
    time.sleep(d)
    print("As you get closer you notice something is off")
    time.sleep(d)
    print("It isnt really a car after all")
    time.sleep(d)
    print("but the remains of one, scrap")
    time.sleep(d)
    print("you climb inside to look around for anything useful")
    time.sleep(d)
    print("but the wreck has nothing to offer but the bitter cold")
    time.sleep(d)
    print("This is how you died")
    time.sleep(d)
    print("Frozen inside scrap metal remains")
    print("")
    time.sleep(d)
    retry()


def cabin():
    print("")
    print("You choose to head towards the cabin")
    time.sleep(d)
    print("as you approach you notice the door is barred shut")
    time.sleep(d)
    print("but you manage to open a window and enter")
    time.sleep(d)
    print("everything is dustry")
    time.sleep(d)
    print("it's clear nobody has been here in a long time")
    time.sleep(d)
    print("Youre not far from the station now...")
    time.sleep(d)
    print("Stay the night, and continue tomorrow")
    time.sleep(d)
    print("Or catch your breath, and try to make it tonight")
    print("")
    time.sleep(d)
    while True:
        thirdPath = input("Please choose Stay/Leave > ")
        if thirdPath == 'Stay':
            stay()
            break
        elif thirdPath == 'Leave':
            leave()
        else:
            print("")
            print("Invalid choice. Please enter 'Stay' or 'Leave'")
            print("")


def leave():
    print("")
    print("you chose to leave")
    time.sleep(d)
    print("you know youre close, you feel it")
    time.sleep(d)
    print("the sun begins to set, as you start to feel anxious")
    time.sleep(d)
    print("the sense of familiarity begins to fade")
    time.sleep(d)
    print("you realise youre lost again")
    time.sleep(d)
    print("a sense of hopelessness creeps in as you wander")
    time.sleep(d)
    print("this is how you died")
    time.sleep(d)
    print("lost and alone")
    print("")
    time.sleep(d)
    retry()


def stay():
    print("")
    print("You choose to stay")
    time.sleep(d)
    print("there is a small old looking bed and a fireplace")
    time.sleep(d)
    print("after some looking around you manage to light a small fire")
    time.sleep(d)
    print("the cabin warms, taking the chill out of your bones")
    time.sleep(d)
    print("you fall asleep for what feel like forever")
    time.sleep(d)
    print("the fire has died and its cold again")
    time.sleep(d)
    print("you get up and get ready for the rest of the trip")
    time.sleep(d)
    print("back to the bitter cold")
    time.sleep(d)
    print("After a while, you spot the station on the horizon")
    time.sleep(d)
    print("Motivation surges")
    time.sleep(d)
    print("Youre going to make it")
    time.sleep(d)
    print("")
    print("")
    time.sleep(d)
    print(f"Congratulations, {name}! You have beat the game.")
    time.sleep(d)
    print("You made many wise decisions to get here")
    time.sleep(d)
    print("I hope you have enjoyed the journey")
    time.sleep(d)
    retry()


# Main Menu
while True:
    start = input('Start, or learn how to play first? Start/Learn > ')
    if start == 'Start':
        intro()
        break
    elif start == 'Learn':
        print("")
        print("The objective of this game is to surive and escape the tundra")
        time.sleep(d)
        print("You will be prompted to make decisions along the way")
        time.sleep(d)
        print("Type your answers and hit enter make a choice")
        time.sleep(d)
        print("Survive untill the end to win the game")
        time.sleep(d)
        print("Make the wrong choice and perish")
        time.sleep(d)
        print("Good luck.")
        time.sleep(d)
        print("")
    else:
        print("")
        print("Invalid choice. Please enter 'Start' or 'Learn'.")
        print("")
