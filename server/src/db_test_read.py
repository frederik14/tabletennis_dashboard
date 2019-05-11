from base import Session
from game import Game
from player import Player

session = Session()

# 3 - extract all movies
players = session.query(Player).all()

# 4 - print movies' details
print('\n### All players:')
for player in players:
    print(f'{player.name} has rank {player.rank}')
print('')

# 3 - extract all movies
games = session.query(Game).all()

# 4 - print games' details
print('\n### All games:')
for game in games:
    print(f'{game.home_player.name} - {game.out_player.name} ({game.home_sets},{game.out_sets})')
print('')