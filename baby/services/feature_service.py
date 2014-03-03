# coding: UTF-8

from baby.models.feature_model import TypeOfMilk, Court, Brand
from baby.services.base_service import get_model
from baby.services.more_service import *
from baby.models.recently_modified import *
from baby.util.others import flatten
from baby import db



def insert_formula(court_id, brand_id, type, energy, protein, carbon_compound, axunge):
    """

    """
    type_of_milk = TypeOfMilk(court_id=court_id, bran_id=brand_id, type=type, energy=energy, protein=protein,
                            carbon_compound=carbon_compound, axunge=axunge)
    db.add(type_of_milk)
    try:
        db.commit()
    except:
        return False
    return True


def get_court():
    """
    获取院内/外
    """
    court, court_count = get_model(Court)
    return court, court_count


def get_brand():
    """
    获取品牌
    """
    brand, brand_count = get_model(Brand)
    return brand, brand_count


def get_formula():
    """
    获取奶粉
    """
    formula, formula_count = get_model(TypeOfMilk)
    return formula, formula_count


def is_list(obj):
    if type(obj) is list:
        return True
    else:
        return False


def format_province_hospital(success):
    '''格式化省市下面的所述医院以及所述部门'''
    province, province_count = get_province()
    hospital, hospital_count = get_hospital()
    department, department_count = get_department()
    position, position_count = get_position()

    success['total'] = []

    if is_list(province) and is_list(hospital) and is_list(department) and is_list(position):
        total_list = []
        for p in province:
            p_pic = flatten(p)
            p_pic['sub_hospital'] = []
            for h in hospital:
                if h.belong_province == p.id:
                    hospital_pic = flatten(h)
                    p_pic['sub_hospital'].append(hospital_pic)
                    hospital_pic['sub_department'] = []
                    for d in department:
                        if d.belong_hospital == h.id:
                            department_pic = flatten(d)
                            hospital_pic['sub_department'].append(department_pic)
                            department_pic['sub_position'] = []
                            for po in position:
                                if po.belong_department == d.id:
                                    position_pic = flatten(po)
                                    department_pic['sub_position'].append(position_pic)
            success['total'].append(p_pic)


def get_recent_modified():
    '''获取最近更新时间'''
    recent = RecentlyModified.query.filter().first()
    if recent:
        recent_pic = flatten(recent)
        return recent_pic
    return 'None'