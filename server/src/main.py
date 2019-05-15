from flask import Flask, jsonify, request
from .base import Session, engine, Base
from .game import Game, GameSchema
from .player import Player, PlayerSchema
from marshmallow import ValidationError
from sqlalchemy.sql.expression import func

# creating the Flask application
app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/players')
def get_players():
    # fetching from the database
    session = Session()
    player_objects = session.query(Player).all()

    # transforming into JSON-serializable objects
    schema = PlayerSchema(many=True)
    players = schema.dump(player_objects)

    # serializing as JSON
    session.close()
    return jsonify(players.data)


@app.route('/players', methods=['POST'])
# def add_player():
#     # mount exam object
#     player_schema = PlayerSchema().load(request.get_json())
#     player = Player(player_schema.data['name'],player_schema.data['rank'])

#     # persist exam
#     session = Session()
#     session.add(player)
#     session.commit()

#     # return created exam
#     new_player = PlayerSchema().dump(player).data
#     session.close()
#     return jsonify(new_player), 201

@app.route('/players', methods=['POST'])
def new_player():
    session = Session()
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = PlayerSchema().load(json_data)[0]
    except ValidationError as err:
        return jsonify(err.messages), 422
    name = data['name']
    player = session.query(Player).filter_by(name=name).first()
    rank = session.query(func.max(Player.rank)).scalar() + 1
    if player is None:
        # Create a new player
        player = Player(name,rank)
        session.add(player)
    session.add(player)
    session.commit()
    result = PlayerSchema().dump(session.query(Player).get(player.id))
    return jsonify({
        'message': 'Created new player.',
        'player': result,
    })

@app.route('/games')
def get_games():
    # fetching from the database
    session = Session()
    games_objects = session.query(Game).all()

    # transforming into JSON-serializable objects
    schema = GameSchema(many=True)
    games = schema.dump(games_objects)

    # serializing as JSON
    session.close()
    return jsonify(games)


@app.route('/games', methods=['POST'])
def add_game():
    # mount exam object
    game_schema = GameSchema().load(request.get_json())
    game = Game(game_schema.data['home_player'],game_schema.data['out_player'], home_sets = game_schema.data['home_sets'], out_sets = game_schema.data['out_sets'])

    # persist exam
    session = Session()
    session.add(game)
    session.commit()

    # return created exam
    new_game = GameSchema().dump(game).data
    session.close()
    return jsonify(new_game), 201

@app.route('/games', methods=['PUT'])
def change_game():
    # mount exam object
    game_schema = GameSchema().load(request.get_json())

    session = Session()
    game = session.query(game_schema['id'])
    game.home_sets = game_schema.data['home_sets']
    game.out_sets = game_schema.data['out_sets']

    # persist exam
    session.add(game)
    session.commit()

    # return created exam
    new_game = GameSchema().dump(game).data
    session.close()
    return jsonify(new_game), 201