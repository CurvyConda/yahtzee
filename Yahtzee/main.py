import roll
from prettytable import PrettyTable
from rich import print


player_card = PrettyTable()
player_card.title = 'YAHTZEE Player Card'
player_card.field_names = ['Upper Section', 'Points']
player_card.align = 'l'
player_card.add_row(['Aces', []])
player_card.add_row(['Twos', []])
player_card.add_row(['Threes', []])
player_card.add_row(['Fours', []])
player_card.add_row(['Fives', []])
player_card.add_row(['Sixes', []])
player_card.add_row(['Total Upper', []])
player_card.add_row(['Bonus*', []])



if __name__ == "__main__":
    print(player_card)
