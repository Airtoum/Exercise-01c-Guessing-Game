#!/usr/bin/env python3
import sys
import random
import time
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def lose(n):
    print("Sorry, better luck next time.")
    print("The number was " + str(n))

def game():
    win = False
    ORBOFACCOUNTING = False
    number = random.randint(1, 10)
    print(number)
    print("You are on a quest to find the secret number. Your travels have determined it is somewhere in the range from 1 to 10.")
    while (True):
        guess = input("Guess a room to enter from 1 to 10: ")
        if not is_int(guess) or int(guess) > 10 or int(guess) < 1:
            print("Your foolishness has awakened the Ghost of Trapdoors!")
            print(random.choice(["A trapdoor opens above your head and a giant spikeball crushes you!","A trapdoor opens beneath you and you fall into a pit of venomous weasels!","A trapdoor opens beside you, and a gray shadeless humanoid figure climbs out. He magically transforms all of your limbs into prosthetics and steals them all, including your head."]))
            lose(number)
            return
        else:
            guess = int(guess)
            if guess == 1:
                print("You enter the 1 Room.")
                print("Before you is a hallway of black spiky traps! Immediately in front of you is a convoy of watermelon-sized spikeballs rolling to your left through square holes in the walls. At the end of the room, you spot the 1 resting upon a pedestal.")
                validactions = ["1","2","3"]
                action = None
                while (not action in validactions):
                    action = input("What will you do?\n 1) Carefully run past them!\n 2) Jump over them!\n 3) Quantum tunnel to the end of Room 1\n")
                rng = random.randint(1,100)
                success = False
                if action == "1":
                    if rng < 5:
                        print("Your sense of timing fails you horribly! You get poked by the spikeball, and, 1 hospital trip later, end up back outside the 10 rooms.")
                    else:
                        print("You successfully run past the spikeballs!")
                        success = True
                elif action == "2":
                    print("You jump over the spikeballs!")
                    success = True
                elif action == "3":
                    if rng == 100:
                        print("Every particle in your body collectively, by complete chance, all go \"Eh, we are over there now.\" By some miracle of chance, you are now at the other side of the room. Congratulations!")
                        success = True
                    else:
                        print("Nothing happens. You leave the room out of embarrassment.")
                if success:
                    print("It appears all of the rest of the obstacles in the room were fake.")
                    print("You pick up the 1. It glistens in your hand.")
                    if guess == number:
                        win = True
                    else:
                        print("However, it is not the secret number. You turn back.")
            if guess == 2:
                print("You enter the 2 room.")
                print("This room seems peaceful. Before you is a wooden 2 on a pedestal, and an ORB OF ACCOUNTING.")
                print("You take them both.")
                ORBOFACCOUNTING = True
                if guess == number:
                    win = True
                else:
                    print("The 2 is not the secret number. You turn back.")
            if guess == 3:
                print("You enter the 3 room.")
                validactions = ["1","2","3"]
                action = None
                while (not action in validactions):
                    action = input("Before you is a lit-up dance floor from the 70's. The 3 is nowhere to be found. What do you do?\n 1) Search the room\n 2) Dismantle the dance floor\n 3) Boogie\n")
                if action == "1":
                    print("You search the room, but find nothing. The dance pad doesn't even seem to have a power source. You give up and leave.")
                if action == "2":
                    print("You try to dismantle the dance floor but it is against the very laws of physics to destroy such a thing. You are kicked out of the room by the sheer fabric of the universe itself for trying.")
                if action == "3":
                    print("You boogie!")
                    time.sleep(2)
                    print("Yeah!")
                    time.sleep(2)
                    print("Your dance moves are rewarded with the 3. The three also looks like a dance floor.")
                    if guess == number:
                        win = True
                    else:
                        print("The funkiness eminiting from the 3 is cool, but it is not the secret number. You turn back.")
            if guess == 4:
                print("You enter the 4 room. It is a pitch black void. In the distance, you can see the 4, sitting on a pedestal with a spotlight shining on it.")
                time.sleep(4)
                print("You begin walking towards it.")
                time.sleep(2)
                print("It will take you about 60 seconds to get there.")
                time.sleep(3)
                print("Yes, I am implying that you must wait 60 seconds before you can do something again.")
                time.sleep(11)
                print("You are one third of the way there.")
                time.sleep(20)
                print("You are getting closer to the 4.")
                time.sleep(15)
                print("You are very close!")
                time.sleep(1)
                print("WHOA! You almost stepped into a bear trap. Luckily, you were able to avoid it.")
                time.sleep(4)
                print("You arrive at the 4. It is made of a smooth white material and is about as heavy as a brick.")
                if guess == number:
                    win = True
                else:
                    print("Unfortunately, it is not the secret number. You turn around to walk back, but it appears the space has become distorted. The door you came from is only an arm's reach away.")
            if guess == 5:
                print("You step into the 5 room and begin plummeting down a vertical shaft.")
                print("Once you reach the bottom, you splat into the ground.")
                if guess == number:
                    win = True
                    print("However, something strange happens. Rather than you splatting into the ground, the ground splats into you. You float around, since there no longer is a ground. Then you see it. The 5, sitting on it's pedestal! \"I have saved you from certain death!\" says the 5. \"I would not like anyone getting hurt in the presence of the Secret Number.\" Your eyes light up. It's the secret number! You snatch the 5 before they can say anything else.")
                else:
                    lose(number)
                    return
            if guess == 6:
                print("You enter the 6 room.")
                validactions = ["1","2","3"]
                action = None
                while (not action in validactions):
                    action = input("Inside is a creature sitting on the ground. The creature speaks to you, \"Guess what number between 1 and 3 I'm thinking of.\"\n 1) 3\n 2) 1\n 3) 2\n")
                rng = random.randint(1,3)
                action = (int(action) - 2) % 3 + 1
                print("You guess " + str(action) + ".")
                if (action == rng):
                    print("\"Hey! You guessed it! Here's a 6.\"\nThe 6 is kind of gross.")
                    if guess == number:
                        win = True
                        print("However...")
                    else:
                        print("The 6 is not the secret number. You take the 6 with you, then get it out of your hand as soon as possible once you leave the room.")
                else:
                    print("\"NOPE! THE CORRECT ANSWER WAS " + str(rng) + "!! GET OUT OF HERE\"")
            if guess == 7:
                print("You enter room 7.")
                print("Inside the room is a collection of army generals and lieutenants. In the middle of the room is a war table.\nA man walks up to you and says, \"What should we do, Chancellor? If we get this wrong, millions of people could die.\"")
                validactions = ["1","2","3"]
                action = None
                while (not action in validactions):
                    action = input("Be very careful. This choice is incredibly important.\n 1) Send a group of archers\n 2) Surrender\n 3) Dig a hole\n")
                print("Someone on the other side of the room says \"Oh, the problem seems to have resolved itself. There is no need to do anything.\"")
                print("In the middle of the table is a piece that is larger than the rest and shaped like a 7. You take it.")
                if guess == number:
                    win = True
                else:
                    print("The 7 is not the secret number. You place it back on the table and leave.")
            if guess == 8:
                print("You enter room 8.")
                print("It is drab. The air smells of accounting. There is a desk with a computer on it.")
                if ORBOFACCOUNTING:
                    print("You take out the ORB OF ACCOUNTING before you pass out. Suddenly, everything in this room makes complete sense to you. You feel as if you have some sort of omnicience confined only within this room. You step up to a computer, reach into the screen, and pull out the essence of pure financial records shaped into an 8.")
                    if guess == number:
                        win = True
                    else:
                        print("The 8 is very interesting, but it is not the secret number. You put it back in the computer and turn back.")
                else:
                    print("You lose consciousness. You awaken back in the hallway of 10 rooms.")
            if guess == 9:
                print("You enter the 9 room.")
                print("...Or you would, if it wasn't just a closet. On the shelves is a 9, amongst cleaning products, towels, mops, and brooms. You take the 9.")
                if guess == number:
                    win = True
                else:
                    print("The 9 is not the secret number. You close the door to the 9 closet.")
            if guess == 10:
                print("You enter the 10 room.")
                print("In the back of the room is the 10, sitting on a pedestal. Between you and the 10 is a button, also on a pedestal. There is a sign next to it saying, \"Press this button to die instantly.\" Maybe it's a trick.")
                validactions = ["1","2"]
                action = None
                while (not action in validactions):
                    action = input("What do you do?\n 1) Press the button\n 2) Get the 10\n")
                if action == "1":
                    print("You press the button, and instantly die.")
                    lose(number)
                    return
                elif action == "2":
                    print("You get the 10. It looks like it was chiseled from stone 800 years ago.")
                    if guess == number:
                        win = True
                    else:
                        print("The 10 is not the secret number. You set it back down since it's very heavy.")
        if win:
            print("The number begins glowing in your hand! You've found it! You found the secret number!")
            print("Great job! You got it!")
            return
        

game()

# I promise my game engine will use classes and nodes