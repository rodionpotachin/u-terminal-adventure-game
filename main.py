# Importing external modules
import time
import random

# Defining global variables
random_item = random.choice(["Old hyper accelerator", "Old fuel pump",
                             "HyperTurbine MKII", "Oxidizer"])
Q_HomeLoc = ("...............................................\n"
             "What you would like to do? (Please,""use numbers only):\n"
             "1. Go to North: Strange big ruins\n"
             "2. Go to West: Misty forest\n"
             "3. Go to East: Creepy dusty field\n"
             "4. Try to repair your starship\n"
             "5. Try to take off (could be dangerous without repair)\n"
             "...............................................\n")
Q_StrBigRuins = ("...............................................\n"
                 "What you would like to do? (Please, use numbers only):\n"
                 "1. Take " + random_item + " only and return to your ship\n"
                 "2. Take ancient sword only and return"
                 " to your ship\n"
                 "3. Take the both items, " + random_item + " and"
                 " ancient sword and return to your ship\n"
                 "4. Return to your ship\n"
                 "...............................................\n")
Q_MiForest = ("...............................................\n"
              "What you would like to do? (Please, use numbers only):\n"
              "1. Take some crystals and return to your ship\n"
              "2. Return to your ship\n"
              "...............................................\n")
Q_CrDuField = ("...............................................\n"
               "What you would like to do? (Please, use numbers only):\n"
               "1. Take required components from the control panel\n"
               "2. Go to the dead body and try to get the dreadful mask\n"
               "3. Return to your ship\n"
               "...............................................\n")


def print_pause(words):
    print(words)
    time.sleep(1)


def text_intro():
    print_pause("..................................................\n"
                "The evil Empire was destroyed. The new republic actively"
                " explore the far star systems\n"
                "..................................................\n")
    print_pause("You are the regular republic trader. You're heading your"
                " way to one of the far star system")
    print_pause("All systems of your spacecraft are works normally."
                " You're snoozing in your pilot cabin calmly...")
    print_pause("But suddenly the spacecraft alarm system goes mad."
                " You start up from sleep and try to figure out that happens")
    print_pause("Suddenly something blow up inside the ship."
                " Black smoke starting to spread at the cabin")
    print_pause("You grab the control stick and quickly land at the nearest"
                " small planet")
    print_pause("..................................................\n")
    print_pause("The landing was hard. You realized that your starship"
                " hyperdrive was broken and you will need to have"
                " some replacement details")
    print_pause("You land on the top of some mountain. You looked around, on"
                " the north direction you can see strange big ruins")
    print_pause("on the west you can see misty forest, on the east you can"
                " see some creepy dusty field")
    print_pause("You realize that the only way to fix you ship and left this"
                " planet is to try to find some details for the ship repair")


def text_intro_StrangeBigRuins():
    print_pause("You slowly approach the ruins. It's look like it was"
                " an ancient temple")
    print_pause("You enter the main building which still keep quite well and"
                " starting to seek through the empty dusty rooms")
    print_pause("Luckily in one of the room you find the " + random_item +
                " which can be used for your ship repair")
    print_pause("Also, you spotted some interesting thing on the pedestal in"
                "the middle of the room."
                " It looks like ancient sword.")
    print_pause("You realize that you can sell it for a huge amount of money."
                " But you have a bad feeling about this...")


def text_intro_MistyForest():
    print_pause("You enter the misty forest. The gigantic trees"
                " obscured the sky above you. Darkness fell.")
    print_pause("Suddenly you spotted some red glowing among the trees."
                " You are heading to this place ")
    print_pause("You find out that glowing comes from a cave which was"
                " filled by the red crystals")
    print_pause("You heard somewhere that such crystals were used for the"
                " sword construction")
    print_pause("You realized that it could be used to power your"
                " spaceship hyperdrive")


def text_intro_CreepyDustyField():
    print_pause("You enter the creepy dusty field. You walk through"
                " it for almost two hours")
    print_pause("Suddenly you spotted the some kind of black stone"
                " building on the horizon")
    print_pause("When you come closer to it, you find out that it"
                " is an ancient tomb")
    print_pause("You feel shivers running up and down the spine ..."
                " But you enter the tomb bravery")
    print_pause("Inside the tomb, you found the gigantic dusty room."
                " In the right corner you spotted the control panel")
    print_pause("You realize that components from that panel can"
                " be used to fix your starship")
    print_pause("You also spotted with horror the dead body in the"
                " dreadful mask lying on the rock in the middle of the room")


def text_deadBody():
    print_pause("You are slowly going closer to the dead body."
                " The silver mask with empty eye sockets looks"
                " even more dreadful now.")
    print_pause("You are very slowly reach out to mask ...")
    print_pause("But suddenly the dead body cold hand grab your neck."
                " You feel that you can't make a breath")
    print_pause("The dead head in the mask slowly raised and peered"
                " into your eyes ...")
    print_pause("Ugh ... Sorry, but it's look like the game is over."
                " It wasn't a good idea to try to take collect that mask")


def text_repairSuccess():
    print_pause("You started the repairing process...")
    print_pause("Success! You managed to use all components"
                " and fix your starship")
    print_pause("Now, you need to hurry up!")
    print_pause("The darkness are coming. You would not"
                " want to stay here anymore")


def text_repairDeadBody():
    print_pause("You started the repairing process...")
    print_pause("But... Suddenly you feel that something goes wrong."
                " You slowly turn around")
    print_pause("The very dreadful dead man in the silver mask staying"
                " in front of you. You paralyzed with fear")
    print_pause("The dead man pointed to the ancient sword"
                " in your pocket")
    print_pause("The sword suddenly jump into a dead man hand..."
                " The red flash of light...")
    print_pause("Ugh ... Sorry, but it looks like the game is over."
                " It wasn't a good idea to take this sword though")


def text_winGame():
    print_pause("You come to your pilot desk and turn on the"
                " engine ignition...")
    print_pause("Yeeeees! It's working!")
    print_pause("Your starship slowly kick off from the ground start to"
                " gather height")
    print_pause("At the last moment you saw the dark figure of a man"
                " in the mountains")
    print_pause("But the height was pretty big already so you can't say for"
                "sure that exactly you saw")
    print_pause("You set the course and jump to the space...")
    print_pause("Congrats! You won the game!")


def validation_input(answer, options):
    while True:
        response = input(answer).lower()
        for options_check in options:
            if options_check in response:
                return options_check
        print_pause("Sorry, I didn't get you. It's a dangerous planet,"
                    "so pick your answers carefully \n")


def outcome_options_main(items, starshipstatus):
    response_0 = validation_input(Q_HomeLoc, ["1", "2", "3", "4", "5"])
    if "1" in response_0:
        outcome_options_StrangeBigRuins(items, starshipstatus)
    elif "2" in response_0:
        outcome_options_MistyForest(items, starshipstatus)
    elif "3" in response_0:
        outcome_options_CreepyDustyField(items, starshipstatus)
    elif "4" in response_0:
        outcome_options_repair(items, starshipstatus)
    elif "5" in response_0:
        outcome_options_flight(starshipstatus, items)


def outcome_options_StrangeBigRuins(items, starshipstatus):
    text_intro_StrangeBigRuins()
    response_1 = validation_input(Q_StrBigRuins, ["1", "2", "3", "4"])
    if "1" in response_1:
        if random_item not in items:
            print_pause("Your taking the " + random_item +
                        " and heading you way back to your starship \n")
            items.append(random_item)
            outcome_options_main(items, starshipstatus)
        else:
            print_pause("You already collect this item."
                        " Please check your pockets\n")
            outcome_options_StrangeBigRuins(items, starshipstatus)
    elif "2" in response_1:
        if "ancient sword" not in items:
            print_pause("Your taking the ancient sword and"
                        " heading your way back to your starship \n")
            items.append("ancient sword")
            outcome_options_main(items, starshipstatus)
        else:
            print_pause("You already collect this item."
                        "Please check your pockets\n")
            outcome_options_StrangeBigRuins(items, starshipstatus)
    elif "3" in response_1:
        if "ancient sword" not in items and random_item not in items:
            print_pause("Your taking the ancient sword and " +
                        random_item + "and heading you way"
                        " back to your starship \n")
            items.append(random_item)
            items.append("ancient sword")
            outcome_options_main(items, starshipstatus)
        else:
            print_pause("You already collect those items."
                        "Please check your pockets\n")
            outcome_options_StrangeBigRuins(items, starshipstatus)
    elif "4" in response_1:
        print_pause("You heading your way back to your starship")
        outcome_options_main(items, starshipstatus)


def outcome_options_MistyForest(items, starshipstatus):
    text_intro_MistyForest()
    response_2 = validation_input(Q_MiForest, ["1", "2"])
    if "1" in response_2:
        if "crystals" not in items:
            print_pause("Your taking some crystals and heading you way"
                        " back to your starship \n")
            items.append("crystals")
            outcome_options_main(items, starshipstatus)
        else:
            print_pause("You already collect this item."
                        "Please check your pockets\n")
            outcome_options_MistyForest(items, starshipstatus)
    elif "2" in response_2:
        print_pause("You heading your way back to your starship")
        outcome_options_main(items, starshipstatus)


def outcome_options_CreepyDustyField(items, starshipstatus):
    text_intro_CreepyDustyField()
    response_3 = validation_input(Q_CrDuField, ["1", "2", "3"])
    if "1" in response_3:
        if "control panel components" not in items:
            print_pause("Your taking the control panel"
                        " components and heading you way"
                        " back to your starship \n")
            items.append("control panel components")
            outcome_options_main(items, starshipstatus)
        else:
            print_pause("You already collect this item."
                        "Please check your pockets\n")
            outcome_options_CreepyDustyField(items, starshipstatus)
    elif "2" in response_3:
        text_deadBody()
        play_again_check()
    elif "3" in response_3:
        print_pause("You heading your way back to your starship")
        outcome_options_main(items, starshipstatus)


def outcome_options_repair(items, starshipstatus):
    if (random_item in items and
            "crystals" in items and "control panel components" in items and
            "ancient sword" not in items):
        text_repairSuccess()
        starshipstatus = 1
        outcome_options_main(items, starshipstatus)
    elif "ancient sword" in items:
        text_repairDeadBody()
        play_again_check()
    else:
        print_pause("It looks like your dont"
                    " have all components for the repair")
        outcome_options_main(items, starshipstatus)


def outcome_options_flight(starshipstatus, items):
    if starshipstatus == 1:
        text_winGame()
        play_again_check()
    else:
        print_pause("You come to your pilot desk"
                    " and turn on the engine ignition... \n")
        print_pause("Nooooo! The engine doesn't show any presence of life. \n")
        outcome_options_main(items, starshipstatus)


def play_again_check():
    response_4 = validation_input("Would you like try"
                                  " again (yes/no)?\n", ["yes", "no"]).lower()
    if "yes" in response_4:
        play_game()
    else:
        print_pause("Thank you!")


def play_game():
    items = []
    starshipstatus = 0
    text_intro()
    outcome_options_main(items, starshipstatus)


# The program enter point:
play_game()
