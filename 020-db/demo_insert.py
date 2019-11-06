from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model import Country, Property, Base

engine = create_engine('sqlite:///sqlalchemy_oecd.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


new_country = Country(name = 'Nambia')
session.add(new_country)
session.commit()