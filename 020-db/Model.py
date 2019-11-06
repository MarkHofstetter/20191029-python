from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Property(Base):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    value = Column(Float, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)

engine = create_engine('sqlite:///sqlalchemy_oecd.db')
 
Base.metadata.create_all(engine)
