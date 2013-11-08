# coding: UTF-8

from ..models.hospital_model import Doctor
from ..models.feature_model import SystemMessage


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
    doctor = Doctor.query.filter(Doctor.id == id, Doctor.login_type == 'doctor').first()
    if doctor:
        system_message_count = SystemMessage.query.filter(SystemMessage.type == 'abstract').count()
        if system_message_count > 1:
            system_messages = SystemMessage.query.filter(SystemMessage.type == 'abstract').\
                order_by(SystemMessage.message_date.desc())[:3]
            return system_messages
        else:
            system_message = SystemMessage.query.filter(SystemMessage.type == 'abstract').first()
            return system_message

