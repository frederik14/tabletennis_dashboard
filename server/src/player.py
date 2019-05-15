from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, sql
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from src.base import Base

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rank = Column(Integer, unique=True)
    def __init__(self, name, rank = sql.functions.max(rank)+1 ):
        self.name = name
        self.rank = rank

class PlayerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    rank = fields.Int()