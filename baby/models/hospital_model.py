# coding:UTF-8

from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, DATETIME
from baby.models.database import Base
from baby.util.ex_time import todayfstr

PROVINCE = 'province'
DOCTOR_TABLE = 'doctor'
HOSPITAL = 'hospital'
DEPARTMENT = 'department'
POSITION = 'position'


class Province(Base):
    '''省'''
    __tablename__ = PROVINCE
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, server_default=None)


class Hospital(Base):
     """
         医院
     """
     __tablename__ = HOSPITAL
     id = Column(Integer, primary_key=True)
     name = Column(String(255), nullable=True)
     belong_province = Column(Integer,ForeignKey(Province.id, ondelete='cascade', onupdate='cascade'), nullable=False)


class Department(Base):
     """
         部门
     """
     __tablename__ = DEPARTMENT
     id = Column(Integer, primary_key=True)
     name = Column(String(255), nullable=True)


class Position(Base):
     """
         职位
     """
     __tablename__ = POSITION
     id = Column(Integer, primary_key=True)
     name = Column(String(255), nullable=True)
     belong_department = Column(Integer, ForeignKey(Department.id, ondelete='cascade', onupdate='cascade'), nullable=False)


class Doctor(Base):
    """
        医生
        id		Integer	    主键列
        doctor_name			用户名
        doctor_pass			登录密码
        real_name			真实姓名
        province_id			城市(市)
        belong_hospital	医院
        belong_dept		医院科室
        position			职位
        email			    邮箱
        tel			        手机号码
        rel_path			相对路径
        pic_name			图片名
        system_message_time 系统消息时间
        login_type			登录类型(doctor,baby)
    """
    __tablename__ = DOCTOR_TABLE
    id = Column(Integer, Sequence('doctor_id', 10001, 1), primary_key=True)
    # Column('id', Integer, Sequence('doctor_id', 100001, 1), primary_key=True)
    doctor_name = Column(String(20), nullable=False, server_default=None)
    doctor_pass = Column(String(18), nullable=False, server_default=None)
    real_name = Column(String(20), nullable=False, server_default=None)
    province_id = Column(Integer,ForeignKey(Province.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    belong_hospital_id = Column(Integer,ForeignKey(Hospital.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    belong_department = Column(Integer,ForeignKey(Department.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    position = Column(Integer,ForeignKey(Position.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    email = Column(String(50), nullable=False, server_default=None)
    tel = Column(String(11), nullable=True)
    rel_path = Column(String(255), nullable=True)
    picture_name = Column(String(255), nullable=True)
    system_message_time = Column(DATETIME, nullable=False, server_default=todayfstr())
    login_type = Column(String(10), nullable=False)

    def __init__(self, **kwargs):
        self.doctor_name = kwargs.pop('doctor_name')
        self.doctor_pass = kwargs.pop('doctor_pass')
        self.real_name = kwargs.pop('real_name')
        self.province_id = kwargs.pop('province')
        self.belong_hospital_id = kwargs.pop('belong_hospital')
        self.belong_department = kwargs.pop('belong_department')
        self.position = kwargs.pop('position')
        self.email = kwargs.pop('email')
        self.tel = kwargs.pop('tel')
        self.rel_path = kwargs.pop('rel_path', '/static')
        self.picture_name = kwargs.pop('picture_name', '/2013.jpg')
        self.system_message_time = kwargs.pop('system_message_time', todayfstr())
        self.login_type = kwargs.pop('login_type', 'doctor')

    def update(self, **kwargs):
        self.doctor_name = kwargs.pop('doctor_name')
        self.doctor_pass = kwargs.pop('doctor_pass')
        self.real_name = kwargs.pop('real_name')
        self.province_id = kwargs.pop('province_id')
        self.belong_hospital = kwargs.pop('belong_hospital')
        self.belong_department = kwargs.pop('belong_department')
        self.position = kwargs.pop('position')
        self.email = kwargs.pop('email')
        self.tel = kwargs.pop('tel')
        self.rel_path = kwargs.pop('rel_path')
        self.system_message_time = kwargs.pop('system_message_time', todayfstr())
        self.picture_name = kwargs.pop('picture_name')
