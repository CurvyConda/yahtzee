from prettytable import PrettyTable

class Player:
  def __init__(self, name, player_card, score):
    self.name = name
    self.player_card = player_card
    self.score  = 0

  def player_card():
    player_card = PrettyTable()
    player_card.title = 'YAHTZEE Player Card'
    player_card.field_names = ['Upper Section', 'Points']
    player_card.add_row = ['Aces', int]
    return player_card
