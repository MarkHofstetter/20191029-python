from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model import Country, Property, Base

import argparse

parser = argparse.ArgumentParser()



engine = create_engine('sqlite:///sqlalchemy_oecd.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
new_country = Country(name = 'Nambia')
session.add(new_country)
session.commit()
'''

read_country = session.query(Country).filter_by(name='Nambia').first()

new_property = Property(name='bla', value=42, country=read_country)
session.add(new_property)
session.commit()


print(read_country.name)

