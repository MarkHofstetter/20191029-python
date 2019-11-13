from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import Country, Property, Base

engine = create_engine('sqlite:///sqlalchemy_oecd.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



def get_data(self, filter = None):
    countries = session.query(Country)
    if filter:
        countries = countries.filter(Country.name.contains(filter))
    self.count = countries.count()
    print('Count:', self.count)
    self.headers = ['Country Name', 'Country ID']
    self.rows = [(country.name, country.id) \
                    for country in countries.all()]
    # return (rows, count, headers)
