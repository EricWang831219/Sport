# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('oracle+cx_oracle://eric:spwilldie99@127.0.0.1:1521')
Session = sessionmaker(bind=engine)

Base = declarative_base()