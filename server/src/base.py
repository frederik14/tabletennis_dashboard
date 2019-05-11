from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

engine = create_engine("sqlite:///ping_pong.db", module = sqlite3.dbapi2)
# conn = eng.connect()s
Session = sessionmaker(bind=engine)

Base = declarative_base()