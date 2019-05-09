import pickle
import os

class GameSet:
    def __init__(self, home_score = 0, out_score = 0):
        self.home = home_score
        self.out = out_score

class Game():
    total_games = 0
    def __init__(self, home_player, out_player):
        self.home_player = home_player
        self.out_player = out_player
        self.result = []
        self.is_played = False
        Game.total_games += 1
        self.identifier = Game.total_games
        self.home = 0
        self.out = 0
    def set_result(self , result):
        if self.is_played == True:
            return 'Result is already set.'
        # todo: add check that result is a valid result for a ping-pong game
        self.result = result
        self.is_played = True
        winner, loser = self.get_winner()
        winner.wins += 1
        loser.losses += 1
        if winner.rank < loser.rank:
            loser.rank, winner.rank = winner.rank, loser.rank
    def get_sets(self):
        self.home = 0
        self.out = 0
        for game_set in self.result:
            if game_set.home > game_set.out:
                self.home += 1
            elif game_set.home < game_set.out:
                self.out += 1
        return self.home , self.out
    def get_winner(self):
        home, out = self.get_sets()
        if home > out:
            return self.home_player, self.out_player
        elif out > home:
            return self.out_player, self.home_player

class Games:
    f = 'games.pickle'
    def __init__(self):
        # exists = os.path.isfile(Games.f)
        # if exists:
        #     pickle_in = open(Games.f,'rb')
        #     self.list = pickle.load(pickle_in)
        #     pickle_in.close()
        # else:
            self.list = []
    def add_game(self, home_player, out_player):
        game = Game(home_player,out_player)
        self.list.append(game)
        # pickle_out = open('games.pickle','wb')
        # pickle.dump(self.list,pickle_out)
        # pickle_out.close()
        return game
    def get_by_id(self,identifier):
        for game in self.list:
            if game.identifier == identifier:
                return game
    def get_games(self):
        games_list = []
        for game in self.list:
            home, out = game.get_sets()
            games_list.append ({ 
                'identifier' : game.identifier,
                'home_player' : game.home_player.name, 
                'out_player' : game.out_player.name, 
                'home_sets' : home, 
                'out_sets' : out
            })
        return games_list
        
class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.wins = 0
        self.losses = 0
        
class Players:
    def __init__(self):
        self.list = []
        self.sets = set()
    def add_player(self, name):
        if name in self.sets:
            return 'Player already exists.'
        player = Player(name,len(self.list)+1)
        self.sets.add(player.name)
        self.list.append(player)
        return player
    def get_by_name(self, name):
        for player in self.list:
            if player.name == name:
                return player
    def list_by_rank(self):
        player_list = []
        sorted_dict = sorted(self.list, key = lambda e: e.rank)
        for player_instance in sorted_dict:
            player_list.append(player_instance.name)
        return player_list