# coding: UTF-8

from ..models.hospital_model import Doctor, Province, Hospital, Department, Position
from ..models.feature_model import SystemMessage
from baby import db
from baby.util.ex_file import *
from baby.setting.xq import *
from werkzeug import secure_filename
from baby.util.others import flatten
import os


def doctor_info(doctor_id):
    """
        获得医生个人资料
            doctor_id: 医生的id
    """
    doctor = Doctor.query.filter(Doctor.id == doctor_id).first()
    if doctor:
        province = Province.query.filter(Province.id == doctor.province_id).first()
        if province:
            doctor.province = province.name
        hospital = Hospital.query.filter(Hospital.id == doctor.belong_hospital_id).first()
        if hospital:
            doctor.hospital = hospital.name
        department = Department.query.filter(Department.id == doctor.belong_department).first()
        if department:
            doctor.department = department.name
        position = Position.query.filter(Position.id == doctor.position).first()
        if position:
            doctor.positions = position.name
    return doctor



def doctor_pickler(doctor, resp_suc):
    doctor_pic = flatten(doctor)
    doctor_pic.pop('belong_hospital_id')
    doctor_pic.pop('belong_department')
    doctor_pic.pop('province_id')
    doctor_pic.pop('position')
    if doctor.rel_path and doctor.picture_name:
        doctor_pic['picture_path'] = doctor.rel_path + '/' + doctor.picture_name
    resp_suc['doctor_list'].append(doctor_pic)


def update_doctor(doctor_id, real_name, province_id, belong_hospital_id, belong_department, position, email, tel, upload_image, success):
    """
    修改医生个人资料
    """
    doctor = doctor_info(doctor_id)
    if doctor:
        if real_name:
            doctor.real_name = real_name
        if province_id:
            doctor.province_id = province_id
        if belong_hospital_id:
            doctor.belong_hospital_id = belong_hospital_id
        if belong_department:
            doctor.belong_department = belong_department
        if position:
            doctor.position = position
        if email:
            doctor.email = email
        if tel:
            doctor.tel = tel
        if upload_image:
            if not allowed_file_extension(upload_image.stream.filename, HEAD_PICTURE_ALLOWED_EXTENSION):
                return False
            old_picture = str(doctor.rel_path) + '/' + str(doctor.picture_name)
            base_path = HEAD_PICTURE_BASE_PATH
            doctor.rel_path = HEAD_PICTURE_UPLOAD_FOLDER
            doctor.picture_name = time_file_name(secure_filename(upload_image.stream.filename), sign=doctor_id)
            upload_image.save(os.path.join(base_path + doctor.rel_path+'/', doctor.picture_name))
            try:
                os.remove(old_picture)
            except:
                pass
        db.commit()
        doctor_pickler(doctor, success)
        return True
    else:
        return False


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

