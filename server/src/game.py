from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from marshmallow import Schema, fields
from src.base import Base
from src.player import PlayerSchema

class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    home_player_id = Column(Integer, ForeignKey('player.id'))
    home_player = relationship('Player', foreign_keys = [home_player_id], uselist=False ) #backref = "games")
    out_player_id = Column(Integer, ForeignKey('player.id'))
    out_player = relationship('Player', foreign_keys = [out_player_id], uselist=False )# backref = "games")
    home_sets = Column(Integer)
    out_sets = Column(Integer)
    date = Column(Date)
    def __init__(self, home_player, out_player, home_sets = 0 ,out_sets = 0):
        self.home_player = home_player
        self.out_player = out_player
        self.home_sets = home_sets
        self.out_sets = out_sets
        self.date = datetime.now()

class GameSchema(Schema):
    id = fields.Int()
    home_player = fields.Nested(PlayerSchema)
    out_player= fields.Nested(PlayerSchema)
    home_sets = fields.Int()
    out_sets = fields.Int()
    date = fields.DateTime()