from sqlalchemy import Column,Integer, String, Float
from .database import Base

NINE_WEIGHT_BOY = 'nine_weight_boy'
NINE_WEIGHT_GIRL = 'nine_weight_girl'
NINE_HEIGHT_BOY = 'nine_height_boy'
NINE_HEIGHT_GIRL = 'nine_height_girl'
NINE_HEAD_BOY = 'nine_head_boy'
NINE_HEAD_GIRL = 'nine_head_girl'


class NineWeightBoy(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_WEIGHT_BOY
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')


class NineWeightGirl(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_WEIGHT_GIRL
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')


class NineHeightBoy(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_HEIGHT_BOY
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')


class NineHeightGirl(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_HEIGHT_GIRL
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')


class NineHeadBoy(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_HEAD_BOY
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')


class NineHeadGirl(Base):
    """
    Nine standard data
    month
    negative3
    negative2
    negative1
    zero
    positive1
    positive2
    positive3
    """
    __tablename__ = NINE_HEAD_GIRL
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=True)
    negative3 = Column(Float, nullable=True)
    negative2 = Column(Float, nullable=True)
    negative1 = Column(Float, nullable=True)
    zero = Column(Float, nullable=True)
    positive1 = Column(Float, nullable=True)
    positive2 = Column(Float, nullable=True)
    positive3 = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('month')
        self.negative3 = kwargs.pop('negative3')
        self.negative2 = kwargs.pop('negative2')
        self.negative1 = kwargs.pop('negative1')
        self.zero = kwargs.pop('zero')
        self.positive1 = kwargs.pop('positive1')
        self.positive2 = kwargs.pop('positive2')
        self.positive3 = kwargs.pop('positive3')