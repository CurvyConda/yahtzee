from roll import roll_the_dice
import resources.score_card

def main():
    while not resources.score_card.grand_total_score == 100:
        f = open("resources/game_text.txt", "r")
        file_contents = f.read()
        print(file_contents)

        allowed_Characters = ["N", "S", "C", "Q"]

        option = input(">>> ").upper()

        if not option in allowed_Characters:
            raise ValueError("Selected input is not an option")
        elif option == "N":
            roll_the_dice(5)
        elif option == "S":
            print("Show Score")
        elif option == "C": 
             resources.score_card.display_score_card()
        elif option == "Q":
            print("Thank you for playing")
            exit()


if __name__ == "__main__":
    main()
