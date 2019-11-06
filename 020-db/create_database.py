from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


engine = create_engine('sqlite:///sqlalchemy_energy.db')
 
Base.metadata.create_all(engine)
