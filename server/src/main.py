from flask import Flask, jsonify, request
from src.base import Session, engine, Base
from src.game import Game, GameSchema
from src.player import Player, PlayerSchema
from marshmallow import ValidationError
from sqlalchemy.sql.expression import func
from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)
CORS(app)


# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/players')
def get_players():
    # fetching from the database
    session = Session()
    player_objects = session.query(Player).order_by(Player.rank)

    # transforming into JSON-serializable objects
    schema = PlayerSchema(many=True)
    players = schema.dump(player_objects)

    # serializing as JSON
    session.close()
    return jsonify(players.data)


@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    session = Session()
    if not id:
        return jsonify({'message': 'Missing input data'}), 400
    player = session.query(Player).get(id)
    session.delete(player)
    session.commit()
    return jsonify({
        'message': 'Player is deleted.',
    })

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
    if player:
        return jsonify({'message': 'Player name already exists'}), 400
    elif player is None:
        # Create a new player
        rank = session.query(func.count(Player.id)).as_scalar()+ 1
        player = Player(name, rank = rank)
        session.add(player)
    session.add(player)
    session.commit()
    result = PlayerSchema().dump(session.query(Player).get(player.id))
    return jsonify({
        'message': 'Created new player.',
        'data': result.data,
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
    return jsonify(games.data)


@app.route('/games', methods=['POST'])
def add_game():
    session = Session()
    json_data = request.get_json()
    data = ''
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = GameSchema().load(json_data)[0]
    except ValidationError as err:
        return jsonify(err.messages), 422
    home_player_name, out_player_name = data['home_player'], data['out_player']
    home_player = session.query(Player).filter_by(name=home_player_name).first()
    out_player = session.query(Player).filter_by(name=out_player_name).first()
    if not home_player or not out_player:
        return jsonify({'message': 'Player does not exist'}), 400
    if 'home_sets' and 'out_sets' in data.keys():
        game = Game(home_player, out_player, home_sets =  data.home_sets, out_sets = data.out_sets ) 
    else:
        game = Game(home_player,out_player) 
    session.add(game)
    session.add(game.home_player)
    session.add(game.out_player)
    session.commit()
    result = GameSchema().dump(session.query(Game).get(game.id))
    return jsonify({
        'message': 'Created new game.',
        'data': result.data,
    })

@app.route('/games/<int:id>', methods=['DELETE'])
def delete_game(id):
    session = Session()
    if not id:
        return jsonify({'message': 'Missing input data'}), 400
    game = session.query(Game).get(id)
    session.delete(game)
    session.commit()
    return jsonify({
        'message': 'Game is deleted.',
    })


@app.route('/games', methods=['PUT'])
def change_game():
    session = Session()
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = GameSchema().load(json_data)[0]
    except ValidationError as err:
        return jsonify(err.messages), 422
    if not 'id' or not 'home_sets' or not 'out_sets' in data.keys():
        return jsonify({'message': 'Missing input data'}), 400
    id, home_sets, out_sets = data['id'], data['home_sets'], data['out_sets']
    game = session.query(Game).get(id)
    game.set_result(home_sets, out_sets) 
    session.add(game)
    session.commit()
    result = GameSchema().dump(session.query(Game).get(game.id))
    return jsonify({
        'message': 'Game result is set.',
        'data': result.data,
    })