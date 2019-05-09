from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

from base import Base

eng = create_engine("sqlite:///ping_pong.db")
# conn = eng.connect()s
Session = sessionmaker(bind=eng)

Base = declarative_base()
