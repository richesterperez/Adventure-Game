# You can use this workspace to write and submit your adventure game project.
import time
import random


def time_message(message, num):
    print(message)
    time.sleep(num)


# This function can be use to repeat action if there was a mistype.
def valid_input(prompt, opt1, opt2):
    while True:
        response = input(prompt).lower()
        if response in opt1:
            break
        elif response in opt2:
            break
        else:
            time_message("I don't understand. Try again.\n", 2)
    return response


def intro():
    time_message("'Welcome to the Fantasy World'", 2)
    time_message("You have been reincarnated as a hero to save this world.", 2)
    time_message("Make haste to save this world hero!!\n", 2)
    time_message("You will have a guide to helped you defeat "
                 "the monster in this world.\n", 3)
    time_message("Guide: Hero, we must come defeat the monster "
                 "lurking in this world.", 3)
    time_message("But first, you must find a weapon that could "
                 "defeat the monster.\n", 2)
    time_message("The Guide explain to you that you may encounter "
                 "a random monster and what weapon "
                 "you must use to defeat the monsters:\n"
                 "1) Goblin - can be defeated with the goblin "
                 "slayer sword or excalibur.\n"
                 "2) Troll - can be defeated with the troll slayer "
                 "sword or excalibur.\n"
                 "3) Witch - can be defeated by witch slayer or excalibur.\n"
                 "4) Dragon - can only be defeated by excalibur.", 3)


def first_path(items):
    weapon = ['goblin slayer', 'witch slayer', 'troll slayer']
    doubt = valid_input("Do you wish to enter? 'Yes' or 'No'\n",
                        'yes', 'no')

    if 'yes' in doubt:
        items.append(random.choice(weapon))
        time_message("\nYou decided to enter the cave.", 2)
        time_message("You found a treasure and inside is a weapon.\n", 2)
        time_message(f"You now have {items} in your inventory.", 2)
        if 'troll slayer' in items and 'witch slayer' in items:
            if 'goblin slayer' in items:
                time_message("You have found all the items in cave.", 2)
                time_message("The God in the cave reward you a "
                             "legendary weapon.", 3)
                time_message("You obtain the excalibur!!", 2)
                items.append("excalibur")
                time_message(f"You now have {items} in your inventory.", 2)
        continue1(items)
    elif 'no' in doubt:
        time_message("The guide and the hero went back to the 3 paths.", 2)
        travel(items)


# Asking the user to continue travelling the first path.
def continue1(items):
    question = valid_input("Do you still wish to continue "
                           "exploring the cave? 'Yes' or 'No'\n",
                           "yes", "no")

    if 'yes' in question:
        time_message("\nYou continued to explore the cave.", 2)
        first_path(items)
    elif 'no' in question:
        time_message("You went back to the three paths:", 2)
        travel(items)


def second_path(items):
    enemy = ['dragon', 'troll', 'goblin', 'witch']

    time_message("The guide and the brave hero travel on the second path", 2)
    time_message("As they walk to a narrow path, an earthquake approach!!", 2)
    time_message(" *rumble* *rumble*", 2)
    time_message(f"\nThese are your equipment: {items}\n", 2)

    doubt2 = valid_input("Are you ready to defeat the world boss?"
                         " 'Yes or No'\n", "yes", "no")

    if 'yes' in doubt2:
        boss = random.choice(enemy)
        time_message(f"\nYou encountered a {boss}!!", 2)
        # Troll
        if boss == 'troll':
            if 'troll slayer' in items or 'excalibur' in items:
                time_message("You are well equipped and defeated "
                             "the boss!", 2)
                time_message("Congratulations on defeating the "
                             "world boss!!", 2)
                play_again()
            else:
                time_message("You do not have the right weapon!", 2)
                time_message("The boss beat you, You lose!", 2)
                play_again()
        # Goblin
        elif boss == 'goblin':
            if 'goblin slayer' in items or 'excalibur' in items:
                time_message("You are well equipped and defeated "
                             "the boss!", 2)
                time_message("Congratulations on defeating the "
                             "world boss!!", 2)
                play_again()
            else:
                time_message("You do not have the right weapon!", 2)
                time_message("The boss beat you, You lose!", 2)
                play_again()
        # Witch
        elif boss == 'witch':
            if 'witch slayer' in items or 'excalibur' in items:
                time_message("You are well equipped and defeated "
                             "the boss!", 2)
                time_message("Congratulations on defeating the "
                             "world boss!!", 2)
                play_again()
            else:
                time_message("You do not have the right weapon!", 2)
                time_message("The boss beat you, You lose!", 2)
                play_again()
        # Dragon
        elif boss == 'dragon':
            if 'excalibur' in items:
                time_message("You are well equipped and defeated "
                             "the boss!", 2)
                time_message("Congratulations on defeating the "
                             "world boss!!", 2)
                play_again()
            else:
                time_message("You do not have the right weapon!", 2)
                time_message("The boss beat you, You lose!", 2)
                play_again()
    elif 'no' in doubt2:
        time_message("The hero and the guide pull back for now.", 2)
        time_message("You will now return to the three paths:", 2)
        travel(items)


def third_path(items):
    dimension = ['excalibur', 'blackhole', 'pit of lava']

    time_message("You travel with your guide, as you approach,"
                 " you see a portal.", 2)

    response = valid_input("Do you wish to touch the portal? "
                           "'Yes' or 'No'\n", "yes", "no")

    if 'yes' in response:
        destination = random.choice(dimension)
        if destination == 'excalibur':
            items.append('excalibur')
            time_message("You touched the portal and dazzled by "
                         "its brightness.", 2)
            time_message("You get closed to the light and see a "
                         "sword burried in the rock.", 2)
            time_message("You picked up the sword.", 2)
            time_message("Its the legendary sword!", 2)
            time_message("You obtain the excalibur.", 2)
            time_message("You will now return to the three paths:\n", 2)
            travel(items)
        elif destination == 'blackhole':
            time_message("You touched the portal and cannot see anything.", 2)
            time_message("It is peached black!!", 2)
            time_message("Oh no! You are swallowed by the blackhole.", 2)
            time_message("You lose.", 2)
            play_again()
        elif destination == 'pit of lava':
            time_message("You touched the portal and see a bright"
                         " red light.", 2)
            time_message("As you get close, you feel a burning"
                         " sensation in your skin.", 2)
            time_message("Oh no! it's a pit of lava!", 2)
            time_message("You are succumbed by the lava.", 2)
            time_message("You lose.", 2)
            play_again()

    elif 'no' in response:
        time_message("You will now return to the three paths:\n", 2)
        travel(items)


def travel(items):
    time_message("\nYou travel with your guide and encounter "
                 "3 different paths:\n"
                 "1) Travel to a cave where you can find weapons.\n"
                 "2) Travel to the world boss.\n"
                 "3) Travel to a dimension where there is a risk "
                 "of losing the game or obtaining the legendary "
                 "excalibur weapon.", 2)
    path = input("Where do you wish to go?\n")

    if path == "1":
        time_message("You chose the first path and explore the cave:\n", 2)
        first_path(items)
    elif path == '2':
        time_message("You chose the second path.\n", 2)
        second_path(items)
    elif path == '3':
        time_message("You chose the third path.\n", 2)
        third_path(items)
    else:
        time_message("I dont understand.", 2)
        travel(items)


def play_again():

    Again = valid_input("Do you wish to play again? 'Yes' or 'No'\n",
                        "yes", "no")

    if 'yes' in Again:
        play_game()
    elif 'no' in Again:
        time_message("Thank you for playing.", 2)


def play_game():
    items = []
    intro()
    travel(items)


play_game()
