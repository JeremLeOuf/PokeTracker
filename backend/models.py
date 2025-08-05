from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"  # Table name in DB

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class PokemonSets(Base):
    __tablename__ = "pokemon_sets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    series = Column(String, nullable=False)
    printed_total = Column(Integer)
    total = Column(Integer)
    ptcgo_code = Column(String)
    release_date = Column(Date)
