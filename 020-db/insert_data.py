import load_data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model import Country, Property, Base

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--database',
  action="store", dest="database",
  help="sqlite database file")

parser.add_argument('-o', '--oecdfile',
  action="store", dest="oecdfile",
  help="oecd file to be parsed")


options = parser.parse_args()

engine = create_engine('sqlite:///'+options.database)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

oecd_data = load_data.load_oecd()    

for country_name, row in oecd_data.iterrows():
    new_country = Country(name = country_name)
    session.add(new_country)
    session.commit()
    for k, v in row.items():
        print(k, v)
        new_property = Property(name=k, value=v, country=new_country)
        session.add(new_property)
    session.commit()
    
'''
sqlite> select c.name, p.name, value from country c join property p on c.id = country_id
   ...> where p.name = 'Life satisfaction' order by value desc limit 10;
Denmark|Life satisfaction|7.5
Iceland|Life satisfaction|7.5
Switzerland|Life satisfaction|7.5
Finland|Life satisfaction|7.4
Israel|Life satisfaction|7.4
Norway|Life satisfaction|7.4
Australia|Life satisfaction|7.3
Canada|Life satisfaction|7.3
Netherlands|Life satisfaction|7.3
New Zealand|Life satisfaction|7.3
'''    