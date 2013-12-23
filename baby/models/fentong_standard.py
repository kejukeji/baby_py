# coding: UTF-8

from sqlalchemy import Column,Integer, String, Float
from .database import Base
from .base_class import InitUpdate


FEN_TONG_WEIGHT_BOY = 'fen_tong_weight_boy'
FEN_TONG_HEIGHT_BOY = 'fen_tong_height_boy'
FEN_TONG_HEAD_BOY = 'fen_tong_head_boy'
FEN_TONG_WEIGHT_GIRL = 'fen_tong_weight_girl'
FEN_TONG_HEIGHT_GIRL = 'fen_tong_height_girl'
FEN_TONG_HEAD_GIRL = 'fen_tong_head_girl'


class FenTongWeightBoy(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_WEIGHT_BOY
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)


class FenTongHeightBoy(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_HEIGHT_BOY
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)


class FenTongHeadBoy(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_HEAD_BOY
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)


class FenTongWeightGirl(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_WEIGHT_GIRL
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)


class FenTongHeightGirl(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_HEIGHT_GIRL
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)


class FenTongHeadGirl(Base, InitUpdate):
    """
    week
    3degree
    10degree
    50degree
    90degree
    97degree
    """
    __tablename__ = FEN_TONG_HEAD_GIRL
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=True)
    degree_three = Column(Float, nullable=True)
    degree_ten = Column(Float, nullable=True)
    degree_fifty = Column(Float, nullable=True)
    degree_ninety = Column(Float, nullable=True)
    degree_ninety_seven = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.init_value(('week', 'degree_three', 'degree_ten', 'degree_fifty', 'degree_ninety', 'degree_ninety_seven'), kwargs)