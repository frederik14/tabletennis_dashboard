from flask import Flask, jsonify, request
from .base import Session, engine, Base
from .game import Game, GameSchema
from .player import Player, PlayerSchema

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
def add_player():
    # mount exam object
    player_schema = PlayerSchema(only=('title', 'description'))\
        .load(request.get_json())

    player = Player(**player_schema.data)

    # persist exam
    session = Session()
    session.add(player)
    session.commit()

    # return created exam
    new_player = PlayerSchema().dump(player).data
    session.close()
    return jsonify(new_player), 201