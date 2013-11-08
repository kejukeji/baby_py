# coding: UTF-8

from sqlalchemy import Column, String, Integer, DATETIME, ForeignKey, Float
from database import Base
from hospital_model import Doctor
from .baby_model import Baby

SYSTEM_MESSAGE_TABLE = 'system_message'
TRACKING_TABLE = 'tracking'
ACADEMIC_ABSTRACT_TABLE = 'academic_abstract'
COLLECT_TABLE = 'collect'
TYPE_OF_MILK_TABLE = 'type_of_milk'
SEARCH_HISTORY = 'search_history'


class SystemMessage(Base):
    """
        系统消息
        id : 主键
        message_content : 消息内容
        message_date : 消息通知时间
        type : 属于那种消息（文摘[abstract]，育儿指南[guide]）
    """
    __tablename__ = SYSTEM_MESSAGE_TABLE
    id = Column(Integer, primary_key=True)
    message_content = Column(String(255), nullable=True)
    message_date = Column(DATETIME, nullable=True)
    type = Column(String(20), nullable=False)


class TypeOfMilk(Base):
    """
        配方奶种类
        id : 主键
        type : 类型
        name : 配方奶名称
    """
    __tablename__ = TYPE_OF_MILK_TABLE
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=True)
    name = Column(String(50), nullable=True)

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.name = kwargs.pop('name')


class Tracking(Base):
    """
        跟踪baby记录
        id :主键
        baby_id :外键，关联的baby表
        measure_date : 测量时期
        weight : baby体重
        height : baby身高
        head_wai : baby头围
        breast_milk_amount: 母乳喂养量
        formula_kind_milk : 配方奶种类
        formula_feed_measure : 配方奶喂养量
    """
    __tablename__ = TRACKING_TABLE
    id = Column(Integer, primary_key=True)
    baby_id = Column(Integer, ForeignKey(Baby.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    measure_date = Column(DATETIME, nullable=True)
    weight = Column(Float(2), nullable=True)
    height = Column(Float(2), nullable=True)
    head_wai = Column(Float(2), nullable=True)
    breast_milk_amount = Column(Float(2), nullable=True)
    type_of_milk_id = Column(Integer, ForeignKey(TypeOfMilk.id, ondelete='cascade', onupdate='cascade'),
                             nullable=False)
    formula_feed_measure = Column(Float(2), nullable=True)

    def __init__(self, **kwargs):
        self.baby_id = kwargs.pop('baby_id')
        self.measure_date = kwargs.pop('measure_date')
        self.weight = kwargs.pop('weight')
        self.height = kwargs.pop('height')
        self.head_wai = kwargs.pop('head_wai')
        self.breast_milk_amount = kwargs.pop('breast_milk_amount')
        self.type_of_milk_id = kwargs.pop('type_of_milk_id')
        self.formula_feed_measure = kwargs.pop('formula_feed_measure')


class AcademicAbstract(Base):
    """
        学术文摘
        id : 主键
        title : 标题
        content : 内容
    """
    __tablename__ = ACADEMIC_ABSTRACT_TABLE
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    content = Column(String(255), nullable=True)


class Collect(Base):
    """
        收藏
        id : 主键
        doctor_id :外键，医生表相关联
        type_id : 外键，收藏的婴儿或者文摘
        type : 收藏类型（baby，abstract）
    """
    __tablename__ = COLLECT_TABLE
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey(Doctor.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    type_id = Column(Integer, nullable=False)
    type = Column(String(10), nullable=True)


class SearchHistory(Base):
    """
        搜索历史记录
        id: 主键
        keyword: 搜索关键字
    """
    __tablename__ = SEARCH_HISTORY
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=True)

    def __init__(self, **kwargs):
        self.keyword = kwargs.pop('keyword')


