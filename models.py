from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:woaiwoziji123@localhost:3306/peek?charset=utf8')
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)

def addInstances(instance):
