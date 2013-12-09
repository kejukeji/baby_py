# coding: UTF-8

from sqlalchemy import Column, String, Integer, DATETIME, Float, Sequence, ForeignKey
from baby.models.database import Base
from baby.util.ex_time import todayfstr


BABY_TABLE = 'baby'
BABY_PICTURE = 'baby_picture'
COMPLICATIONS = 'complication'
CHILDBIRTH_STYLES = 'childbirth_style'


class Complication(Base):
    """
    合并症
    id：主键
    name：合并症名
    parent_id: 所属那种
    """
    __tablename__ = COMPLICATIONS
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    parent_id = Column(Integer, nullable=False)


class ChildbirthStyle(Base):
    """
    分娩方式
    id: 主键
    name： 方式
    """
    __tablename__ = CHILDBIRTH_STYLES
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class Baby(Base):
    """
        婴儿
        id	:主键id
        baby_name	    婴儿名
        login_name      婴儿登陆
        gender		    性别
        due_date	    预产期
        born_birthday	出生日期
        born_weight		出生体重
        born_height		出生身高
        born_head		出生头围
        childbirth_style	分娩方式
        complication_id	合并症(可以多选，实用逗号隔开)
        restore_day		恢复出生体重天数
        apgar_score		Apgar评分
        growth_standard		生长参考标准
        system_message_time 系统信息时间
        login_type		登录类型(doctor,baby)
    """
    __tablename__ = BABY_TABLE
    id = Column(Integer, Sequence('baby_id', 10001, 1), primary_key=True)
    patriarch_tel = Column(String(11), nullable=False, server_default=None)
    baby_name = Column(String(20), nullable=True)
    baby_pass = Column(String(20), nullable=False, server_default=None)
    login_name = Column(String(20), nullable=False, server_default=None)
    gender = Column(String(2), nullable=False, server_default=None)
    due_date = Column(DATETIME, nullable=False, server_default=None)
    born_birthday = Column(DATETIME, nullable=False, server_default=None)
    born_weight = Column(Float(2), nullable=False, server_default=None)
    born_height = Column(Float(2), nullable=False, server_default=None)
    born_head = Column(Float(2), nullable=False, server_default=None)
    #childbirth_style_id = Column(Integer, ForeignKey(ChildbirthStyle.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    childbirth_style = Column(String(20), nullable=False)
    complication_id = Column(String(255), nullable=False, server_default=None)
    restore_day = Column(Integer, nullable=False, server_default=None)
    apgar_score = Column(Integer, nullable=False, server_default=None)
    growth_standard = Column(String(100), nullable=True)
    system_message_time = Column(DATETIME, nullable=False, server_default=None)
    login_type = Column(String(10), nullable=False)

    def __init__(self, **kwargs):
        self.patriarch_tel = kwargs.pop('patriarch_tel')
        self.baby_name = kwargs.pop('baby_name')
        self.baby_pass = kwargs.pop('baby_pass')
        self.gender = kwargs.pop('gender')
        self.due_date = kwargs.pop('due_date')
        self.born_birthday = kwargs.pop('born_birthday')
        self.born_weight = kwargs.pop('born_weight')
        self.born_height = kwargs.pop('born_height')
        self.born_head = kwargs.pop('born_head')
        #self.childbirth_style_id = kwargs.pop('childbirth_style')
        self.childbirth_style = kwargs.pop('childbirth_style')
        self.complication_id = kwargs.pop('complication')
        self.restore_day = kwargs.pop('restore_day', 0)
        self.apgar_score = kwargs.pop('apgar_score', 0)
        self.growth_standard = kwargs.pop('growth_standard', 0)
        self.system_message_time = kwargs.pop('system_message_time', todayfstr())
        self.login_name = kwargs.pop('login_name', '')
        self.login_type = kwargs.pop('login_type', 'baby')

    def update(self, **kwargs):
        self.patriarch_tel = kwargs.pop('patriarch_tel')
        self.baby_name = kwargs.pop('baby_name')
        self.baby_pass = kwargs.pop('baby_pass')
        self.gender = kwargs.pop('gender')
        self.due_date = kwargs.pop('due_date')
        self.born_birthday = kwargs.pop('born_birthday')
        self.born_weight = kwargs.pop('born_weight')
        self.born_height = kwargs.pop('born_height')
        self.born_head = kwargs.pop('born_head')
        self.childbirth_style = kwargs.pop('childbirth_style')
        self.complication = kwargs.pop('complication')
        self.restore_day = kwargs.pop('restore_day')
        self.apgar_score = kwargs.pop('apgar_score')
        self.growth_standard = kwargs.pop('growth_standard')


class BabyPicture(Base):
    """
       婴儿图片表
          id: 主键
          user_id: 关联baby
          base_path: 绝对路劲
          rel_path: 相对路劲
          picture_name: 图片名
    """
    __tablename__ = BABY_PICTURE
    id = Column(Integer, primary_key=True)
    baby_id = Column(Integer, ForeignKey(Baby.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    base_path = Column(String(250), nullable=True)
    rel_path = Column(String(250), nullable=True)
    picture_name = Column(String(250), nullable=True)

    def __init__(self, **kwargs):
        self.baby_id = kwargs.pop('baby_id')
        self.base_path = kwargs.pop('base_path')
        self.rel_path = kwargs.pop('rel_path')
        self.picture_name = kwargs.pop('picture_name')


