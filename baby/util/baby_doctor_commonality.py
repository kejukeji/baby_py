# coding: UTF-8

from .others import pickler, time_diff


def format_baby(baby, resp_suc):
    """
        格式化baby对象
    """
    baby_pic = pickler.flatten(baby)
    baby_pic['picture_path'] = baby.rel_path + baby.picture_name
    baby_birthday = baby.born_birthday
    baby_pic['time'] = time_diff(baby_birthday)
    resp_suc['baby_list'].append(baby_pic)


def doctor_pickler(doctor, resp_suc):
    doctor_pic = pickler.flatten(doctor)
    doctor_pic['picture_path'] = doctor.rel_path + doctor.picture_name
    resp_suc['doctor_list'].append(doctor_pic)


def search_pickler(search_history, resp_suc):
    """
        转换json
    """
    search_pic = pickler.flatten(search_history)
    resp_suc['search_history_list'].append(search_pic)


def system_message_pickler(system_message, resp_suc):
    """
        转换json
    """
    search_pic = pickler.flatten(system_message)
    resp_suc['system_message_list'].append(search_pic)