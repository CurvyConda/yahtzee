from random import randint as rnd


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
    return die


def show_roll(die):
    print("The die rolls are ", end="")
    for d in die:
        print(
            str(d) + " ",
            end="",
        )
