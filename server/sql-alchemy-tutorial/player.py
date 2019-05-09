from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(Integer)
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank