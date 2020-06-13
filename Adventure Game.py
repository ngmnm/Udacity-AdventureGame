import random
import time


def print_sleep(massage):
    print(massage)
    time.sleep(2)


def fight_or_run():
    print_sleep("would you like to (1) fight or (2) tun away?\n")
    decision = random.randint(1, 2)
    print_sleep("you have chosen " + decision.__str__())
    if decision == 1:
        return 1
    elif decision == 2:
        return 2
    else:
        fight_or_run()


def field():
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")


def play_again():

    print_sleep("GAME OVER\n")
    newGame = input("Would you like to play again? (y/n)\n")
    if newGame == 'y':
        new_game()
    elif newGame == 'n':
        print("Thanks for playing ! See you next time.")
        exit(0)
    else:
        play_again()


def intro():
    print_sleep("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a wicked fairie is somewhere"
                " around here, and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty (but not "
                "very effective) dagger.")


def house(item):
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens "
                "and out steps a gorgon.")
    print_sleep("Eep! This is the fragon's house!")
    print_sleep("The dragons attacks you !")

    if 'sword' not in item:
        defeat = ["You have been defeated!", "The gorgon killed you "]
        print_sleep("You feel a bit under-oreoared fir this,"
                    " what with only having a tiny dagger.")
        if fight_or_run() == 1:
            print_sleep("you do your best...")
            print_sleep("but your dagger is no match for the gorgon")
            print_sleep(random.choice(defeat))
            play_again()
        else:
            print_sleep("You run back into the field. Luckly, "
                        "you don't seem to have been followed.\n")
            field()
            game(item)
    else:
        if fight_or_run() == 1:
            print_sleep("As the dragon moves to attack,"
                        " you unsheath your new sword.")
            print_sleep("The Sword of Ogototh shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_sleep("But the gorgon takes one look at your"
                        " shiny new toy and runs away!")
            print_sleep("You have rid the town of the gorgon."
                        " You are victorious!")
            play_again()
        else:
            print_sleep("You run back into the field. Luckly,"
                        " you don't seem to have been followed.\n")
            field()
            game(item)


def cave(item):
    print_sleep("you peer cautiously into the cave.")
    if 'sword' in item:
        print_sleep("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    else:
        print_sleep("#It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old daffer "
                    "and take the sword with you .")
        item.append("sword")

    print_sleep("you walk back out to the field\n")
    field()


def game(item):

    user_choice = input("(please enter 1 or 2.)\n")
    if user_choice == '1':
        house(item)
        game(item)
    elif user_choice == '2':
        cave(item)
        game(item)
    else:
        game(item)


def new_game():
    item = []
    intro()
    game(item)


new_game()
