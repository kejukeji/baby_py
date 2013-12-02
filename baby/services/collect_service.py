# coding: UTF-8
from baby.models.feature_model import Collect
from baby import db


def check_is_collect(doctor_id, type_id, collect_type):
    '''检查是否已经收藏'''
    collect_result = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type_id == type_id, Collect.type == collect_type).first()
    if collect_result is not None:
        return collect_result
    else:
        return None


def insert_collects(doctor_id, type_id, collect_type):
    '''添加收藏'''
    result = check_is_collect(doctor_id, type_id, collect_type)
    if result:
        try:
            db.delete(result)
            db.commit()
        except:
            return False
        return True
    else:
        collect = Collect(doctor_id=doctor_id, type_id=type_id, type=collect_type)
        try:
            db.add(collect)
            db.commit()
        except:
            return False
        return True