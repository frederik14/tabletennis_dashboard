from datetime import date
from game import Game
from player import Player
from base import Session, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create movies
# home_player = Player('Frederik',1)
# out_player = Player('Flore',2)

players = session.query(Player).all()

game1 = Game(players[0],players[1],home_sets=2,out_sets=1)

# 9 - persists data
session.add(game1)

# 10 - commit and close session
session.commit()
session.close()