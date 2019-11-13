from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import Country, Property, Base
import argparse

parser = argparse.ArgumentParser()
engine = create_engine('sqlite:///sqlalchemy_oecd.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

countries = session.query(Country).filter(Country.name.contains('au'))

print(countries.count()) # besser!

print(len(countries.all())) # expandiert evtl die Liste

for country in countries.all():
    print(country.name, country.id)

