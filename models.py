#!/usr/bin/env python
#coding:utf-8
"""
模型
"""
import os

from sqlalchemy import Column,create_engine,String,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_baseDir = os.path.dirname(__file__)
_Base = declarative_base()
_engine = create_engine('sqlite:///'+os.path.join(_baseDir,'platform.db'))
_DBsession = sessionmaker(bind=_engine)
session = _DBsession()

class Platform():
    __tablename__='platform'

    id = Column(String(48),primary_key=True)
    name = Column(String(48))
    companyName = Column(String(48))
    QQ = Column(String(48))
    phoneCustomer = Column(String(48))
    address = Column(String(128))
    noteSpecial = Column(Text)

    @staticmethod
    def init_db():
        _Base.metadata.create_all(_engine)

    @staticmethod
    def drop_db():
         _Base.metadata.drop_all(_engine)
if __name__ == '__main__':
    pass
    Platform.drop_db()
    Platform.init_db()