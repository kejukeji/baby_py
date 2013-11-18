# coding: UTF-8

from baby.models.baby_model import Baby
from baby.models.hospital_model import Doctor, Province, Hospital, Department, Position
from baby.util.others import set_session_user
from baby.models.database import db


def check_login(login_name, login_pass):
    """
       login_name: 登陆名
       login_pass: 登陆密码
    """
    baby = Baby.query.filter(Baby.login_name == login_name, Baby.baby_pass == login_pass).first()
    doctor = Doctor.query.filter(Doctor.doctor_name == login_name, Doctor.doctor_pass == login_pass).first()
    if baby != None or doctor != None:
        if baby != None:
            set_session_user(baby.login_name, baby.id)
            return baby
        if doctor != None:
            set_session_user(doctor.doctor_name, doctor.id)
            return doctor


def register_doctor(login_name, login_pass, real_name, area, hospital, belong_class, profile, email, tel):
    doctor = Doctor(doctor_name=login_name, doctor_pass=login_pass, real_name=real_name, province=area,
                    belong_hospital=hospital, belong_department=belong_class, position=profile, email=email,
                    tel=tel)
    try:
        db.add(doctor)
        db.commit()
        return 0
    except:
        return 1


def is_null(model):
    '''判断一个model是否为空'''
    if model:
        return True
    else:
        return False


def by_count(model, count):
    if count > 1:
        result_model = model.query.filter().all()
        return model
    else:
        result_model = model.query.filter().first()
        if result_model:
            return result_model


def get_province():
    '''得到注册所需要的省'''
    province_count = Province.query.filter().count()
    if province_count > 1:
        province = Province.query.filter().all()
    else:
        province = Province.query.filter().first()
    return province, province_count


def get_hospital():
    '''得到注册所需要的医院'''
    hospital_count = Hospital.query.filter().count()
    if hospital_count > 1:
        hospital = Hospital.query.filter().all()
    else:
        hospital = Hospital.query.filter().first()
    return hospital, hospital_count


def get_department():
    '''得到注册所需要的部门'''
    department_count = Department.query.filter().count()
    if department_count > 1:
        department = Department.query.filter().all()
    else:
        department = Department.query.filter().first()
    return department, department_count


def get_position():
    '''得到注册所需要的职位'''
    position_count = Position.query.filter().count()
    if position_count > 1:
        position = Position.query.filter().all()
    else:
        position = Position.query.filter().first()
    return position, position_count
