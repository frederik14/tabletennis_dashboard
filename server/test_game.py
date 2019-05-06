from ping_pong.game import Players, Games, GameSet

# app.run()
players = Players()
games = Games()

frederik = players.add_player('Frederik')
flore = players.add_player('Flore')

game = games.add_game(frederik,flore)

result = []
result.append(GameSet(11,3))
result.append(GameSet(9,11))
result.append(GameSet(11,4))
game.set_result(result)

winner, loser = game.get_winner()
print('winner: ', winner.name)

for player in players.list:
    print(player.name, 'has won', player.wins, 'time(s).')

player = players.get_by_name('Flore')
print(player.name, 'has won', player.wins, 'time(s).')

print(players.list_by_rank())