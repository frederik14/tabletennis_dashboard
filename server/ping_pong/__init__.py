import markdown
import os
import shelve
import json
import logging
import pickle

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
from ping_pong.game import Players, Games, GameSet

# Create a Games instance
persistent_file = 'persistency.pickle'
exists = os.path.isfile(persistent_file)
if exists:
    pickle_in = open(persistent_file,'rb')
    games = pickle.load(pickle_in)
    pickle_in.close()
else:
    games = Games()

# Create a Players instance
players = Players()

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class PlayerList(Resource):
    def get(self):
        return {'message': 'Success', 'data': players.list_by_rank()}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True, trim = True)

        # Parse the arguments into an object
        args = parser.parse_args()
        
        if args.name in players.sets:
            return {'message': 'Player aready exists', 'data': args}, 200

        players.add_player(args.name)
        return {'message': 'Player added', 'data': args}, 201


class GamesList(Resource):
    def get(self):
        return {'message': 'Success', 'data': games.get_games()}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('home_player', required=True, trim=True)
        parser.add_argument('out_player', required=True, trim=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        home_player = players.get_by_name(args.home_player)
        out_player = players.get_by_name(args.out_player)
        game = games.add_game(home_player,out_player)
        pickle_out = open(persistent_file,'wb')
        pickle.dump(games,pickle_out)
        pickle_out.close()
        return {'message': 'Device registered', 'data': args, 'identifier': game.identifier}, 201

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('result', action = 'append')
        parser.add_argument('identifier', type=int)
        
        args = parser.parse_args()
        
        result = []
        set1 = GameSet(int(args.result[0]),int(args.result[1]))
        result.append(set1)
        set2 = GameSet(int(args.result[2]),int(args.result[3]))
        result.append(set2)
        if len(args.result) > 5:
            if int(args.result[4])+int(args.result[5]) != 0:
                set3 = GameSet(int(args.result[2]),int(args.result[3]))
                result.append(set3)
        game = games.get_by_id(args.identifier)
        game.set_result(result)
        pickle_out = open(persistent_file,'wb')
        pickle.dump(games,pickle_out)
        pickle_out.close()

        return {'message': 'Device registered', 'data': args}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('identifier', type=int)
        args = parser.parse_args()
        # If the key does not exist in the data store, return a 404 error.
        if not (args.identifier in games.list):
            return {'message': 'Game not found', 'data': {}}, 404

        del games.list[args.identifier]
        return '', 204


api.add_resource(PlayerList, '/players')
api.add_resource(GamesList, '/games')
# api.add_resource(Device, '/device/<string:identifier>')




