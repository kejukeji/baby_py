# coding: UTF-8

from sqlalchemy import Column, Integer, DATETIME
from .database import Base


RECENTLY_MODIFIED = 'recently_modified'

class RecentlyModified(Base):
    '''最近修改'''
    __tablename__ = RECENTLY_MODIFIED
    id = Column(Integer, primary_key=True)
    update_time = Column(DATETIME, nullable=True)
