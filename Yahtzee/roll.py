from random import randint as rnd
import resources.score_card


def roll_the_dice(number_of_dice):
    die = []
    for i in range(number_of_dice):
        die.append(rnd(1, 6))

    show_roll(die)

    reroll = input("\nWhich die do you want to reroll?")
    reroll = reroll.split()
    for index, ch in enumerate(reroll):
        reroll[index] = int(ch) - 1

    for index in reroll:
        die[index] = rnd(1, 6)

    show_roll(die)

    reroll = input("\nWhich die do you want to reroll?")
    reroll = reroll.split()
    for index, ch in enumerate(reroll):
        reroll[index] = int(ch) - 1

    for index in reroll:
        die[index] = rnd(1, 6)

    show_roll(die)
    allocate_score(die)
    resources.score_card.display_score_card()
    return die


def allocate_score(die):
    score_to_change = int(input("\nWhat would you like to score this as?"))
    if score_to_change == 2:
        resources.score_card.change_score(1, 3)
    print("\n", score_to_change)
    print("\n⚡️ ⚡️ ⚡️", die)


def show_roll(die):
    print("The die rolls are ", end="")
    for d in die:
        print(
            str(d) + " ",
            end="",
        )
