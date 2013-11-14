# coding: UTF-8

from baby.models.baby_model import Baby
from baby.models.hospital_model import Doctor
from baby.util.others import set_session_user


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