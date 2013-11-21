# coding: UTF-8

from ..models.hospital_model import Doctor
from ..models.feature_model import SystemMessage
from baby import db


def doctor_info(doctor_id):
    """
        获得医生个人资料
            doctor_id: 医生的id
    """
    doctor = Doctor.query.filter(Doctor.id == doctor_id).first()
    return doctor


def get_meeting_message(id):
    """
        得到会议消息
            id: 根据id来判断是属于医生还是婴儿
    """
    doctor = Doctor.query.filter(Doctor.id == id).first()
    if doctor:
        system_message_count = SystemMessage.query.filter(SystemMessage.type == 'abstract').count()
        if system_message_count > 1:
            system_messages = SystemMessage.query.filter(SystemMessage.type == 'abstract').\
                order_by(SystemMessage.message_date.desc())[:3]
            return system_messages
        else:
            system_message = SystemMessage.query.filter(SystemMessage.type == 'abstract').first()
            return system_message

def register_doctor(login_name, login_pass, argument_real_name, argument_province, argument_belong_hospital,
                    argument_belong_department, argument_position, argument_email, argument_tel):
    """
       注册医师
    """
    doctor_result = Doctor.query.filter(Doctor.doctor_name == login_name).first()
    if doctor_result:
        return False
    else:
        doctor = Doctor(doctor_name=login_name, doctor_pass=login_pass, real_name=argument_real_name, province=argument_province,
                        belong_hospital=argument_belong_hospital, belong_department=argument_belong_department, position=argument_position,
                        email=argument_email, tel=argument_tel)
        try:
            db.add(doctor)
            db.commit()
        except:
            return False
        return True

