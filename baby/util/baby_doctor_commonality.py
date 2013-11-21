# coding: UTF-8

from .others import pickler, time_diff, flatten
from baby.models.baby_model import BabyPicture, Baby


def format_baby(baby, resp_suc):
    """
        格式化baby对象
    """
    baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == baby.id).first()
    baby_pic = flatten(baby)
    if baby.born_birthday:
        baby_birthday = baby.born_birthday
        baby_pic['time'] = time_diff(baby_birthday)
    if baby_picture:
        if baby_picture.rel_path and baby_picture.picture_name:
            baby_pic['picture_path'] = baby_picture.rel_path + '/' + baby_picture.picture_name
    resp_suc['baby_list'].append(baby_pic)


def pickler_baby_only(result, remember):
    if type(result) is Baby:
        baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == result.id).first()
        baby_pic = flatten(result)
        baby_pic['is_remember'] = int(remember)
        baby_pic.pop('id')
        baby_pic['user_id'] = result.id
        if result.born_birthday:
            baby_birthday = result.born_birthday
            baby_pic['time'] = time_diff(baby_birthday)
        if baby_picture:
            if baby_picture.rel_path and baby_picture.picture_name:
                baby_pic['picture_path'] = baby_picture.rel_path + '/' + baby_picture.picture_name
        return baby_pic
    elif type(result) is Doctor:
        pass


def doctor_pickler(doctor, resp_suc):
    doctor_pic = flatten(doctor)
    if doctor.rel_path and doctor.picture_name:
        doctor_pic['picture_path'] = doctor.rel_path + '/' + doctor.picture_name
    resp_suc['doctor_list'].append(doctor_pic)


def doctor_pickler_only(doctor, remember):
    doctor_pic = flatten(doctor)
    doctor_pic['is_remember'] = int(remember)
    doctor_pic.pop('id')
    doctor_pic['user_id'] = doctor.id
    if doctor.rel_path and doctor.picture_name:
        doctor_pic['picture_path'] = doctor.rel_path + '/' + doctor.picture_name
    return doctor_pic


def search_pickler(search_history, resp_suc):
    """
        转换json
    """
    search_pic = flatten(search_history)
    resp_suc['search_history_list'].append(search_pic)


def system_message_pickler(system_message, resp_suc):
    """
        转换json
    """
    search_pic = flatten(system_message)
    resp_suc['system_message_list'].append(search_pic)


def register_data_province(province, return_success):
    """
       下拉列表省份数据
    """
    return_success['province_list'] = []
    if type(province) is list:
        for p in province:
            province_pic = flatten(p)
            return_success['province_list'].append(province_pic)
    else:
        province_pic = flatten(province)
        return_success['province_list'].append(province_pic)


def register_data_hospital(hospital, return_success):
    """
       下拉列表医院数据
    """
    return_success['hospital_list'] = []
    if type(hospital) is list:
        for h in hospital:
            hospital_pic = flatten(h)
            return_success['hospital_list'].append(hospital_pic)
    else:
        hospital_pic = flatten(hospital)
        return_success['hospital_list'].append(hospital_pic)


def register_data_department(department, return_success):
    """
       下拉列表部门数据
    """
    return_success['department_list'] = []
    if type(department) is list:
        for d in department:
            department_pic = flatten(d)
            return_success['department_list'].append(department_pic)
    else:
        department_pic = flatten(department)
        return_success['department_list'].append(department_pic)


def register_data_position(position, return_success):
    """
       下拉列表职位数据
    """
    return_success['position_list'] = []
    if type(position) is list:
        for p in position:
            position_pic = flatten(p)
            return_success['position_list'].append(position_pic)
    else:
        position_pic = flatten(position)
        return_success['position_list'].append(position_pic)