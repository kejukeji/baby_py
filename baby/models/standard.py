# coding: UTF-8

from sqlalchemy import Column,Integer, String, Float
from .database import Base

WEIGHT_STANDARD = 'weight_boy_standard_week'
WEIGHT_GRIS_STANDARD = 'weight_girl_standard_week'
HEIGHT_BOY_STANDARD = 'height_boy_standard_week'
HEIGHT_GIRL_STANDARD = 'height_girl_standard_week'
HEAD_SURROUND_BOY_STANDARD = 'head_surround_boy_standard_week'
HEAD_SURROUND_GIRL_STANDARD = 'head_surround_girl_standard_week'
WEIGHT_STANDARD_MONTH = 'weight_boy_standard_month'
WEIGHT_GRIS_STANDARD_MONTH = 'weight_girl_standard_month'
HEIGHT_BOY_STANDARD_MONTH = 'height_boy_standard_month'
HEIGHT_GIRL_STANDARD_MONTH = 'height_girl_standard_month'
HEAD_SURROUND_BOY_STANDARD_MONTH = 'head_surround_boy_standard_month'
HEAD_SURROUND_GIRL_STANDARD_MONTH = 'head_surround_girl_standard_month'


class WeightBoyStandardWeek(Base):
    """
       体重标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = WEIGHT_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class WeightGirlStandardWeek(Base):
    """
       体重标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = WEIGHT_GRIS_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeightBoyStandardWeek(Base):
    """
       身高标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEIGHT_BOY_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeightGirlStandardWeek(Base):
    """
       身高标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEIGHT_GIRL_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeadSurroundBoyStandardWeek(Base):
    """
       身高标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEAD_SURROUND_BOY_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')

class HeadSurroundGirlStandardWeek(Base):
    """
       身高标准
          age 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEAD_SURROUND_GIRL_STANDARD
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.week = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class WeightBoyStandardYear(Base):
    """
       体重标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = WEIGHT_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class WeightGirlStandardYear(Base):
    """
       体重标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = WEIGHT_GRIS_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeightBoyStandardYear(Base):
    """
       身高标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEIGHT_BOY_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeightGirlStandardYear(Base):
    """
       身高标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEIGHT_GIRL_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')


class HeadSurroundBoyStandardYear(Base):
    """
       身高标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEAD_SURROUND_BOY_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')

class HeadSurroundGirlStandardYear(Base):
    """
       身高标准
          month 年龄
          L
          M
          S
          P01
          P1
          P3
          P5
          P10
          P15
          P25
          P50
          P75
          P85
          P90
          P95
          P97
          P99
          P999
    """
    __tablename__ = HEAD_SURROUND_GIRL_STANDARD_MONTH
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False, server_default=None)
    L = Column(Float, nullable=False, server_default=None)
    M = Column(Float, nullable=False, server_default=None)
    S = Column(Float, nullable=False, server_default=None)
    P01 = Column(Float, nullable=False, server_default=None)
    P1 = Column(Float, nullable=False, server_default=None)
    P3 = Column(Float, nullable=False, server_default=None)
    P5 = Column(Float, nullable=False, server_default=None)
    P10 = Column(Float, nullable=False, server_default=None)
    P15 = Column(Float, nullable=False, server_default=None)
    P25 = Column(Float, nullable=False, server_default=None)
    P50 = Column(Float, nullable=False, server_default=None)
    P75 = Column(Float, nullable=False, server_default=None)
    P85 = Column(Float, nullable=False, server_default=None)
    P90 = Column(Float, nullable=False, server_default=None)
    P95 = Column(Float, nullable=False, server_default=None)
    P97 = Column(Float, nullable=False, server_default=None)
    P99 = Column(Float, nullable=False, server_default=None)
    P999 = Column(Float, nullable=False, server_default=None)

    def __init__(self, **kwargs):
        self.month = kwargs.pop('age', 0)
        self.L = kwargs.pop('L')
        self.M = kwargs.pop('M')
        self.S = kwargs.pop('S')
        self.P01 = kwargs.pop('P01')
        self.P1 = kwargs.pop('P1')
        self.P3 = kwargs.pop('P3')
        self.P5 = kwargs.pop('P5')
        self.P10 = kwargs.pop('P10')
        self.P15 = kwargs.pop('P15')
        self.P25 = kwargs.pop('P25')
        self.P50 = kwargs.pop('P50')
        self.P75 = kwargs.pop('P75')
        self.P85 = kwargs.pop('P85')
        self.P90 = kwargs.pop('P90')
        self.P95 = kwargs.pop('P95')
        self.P97 = kwargs.pop('P97')
        self.P99 = kwargs.pop('P99')
        self.P999 = kwargs.pop('P999')