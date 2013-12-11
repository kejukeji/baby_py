# coding: UTF-8

from baby.models.baby_model import *
from baby.util.others import flatten


def get_complication(success):
    """
    获取全部合并症数据
    """
    parent_list = []
    child_list = []
    parent_complication = Complication.query.filter(Complication.parent_id == 0).all() # 得到所有父级
    child_complication = Complication.query.filter(Complication.parent_id != 0).all() # 得到所有子级
    success['complication'] = []
    if parent_complication and type(parent_complication) is list:
        if child_complication and type(child_complication) is list:
            for parent in parent_complication:
                parent_pic = flatten(parent)
                parent_list.append(parent_pic)
                parent_pic['child'] = []
                for child in child_complication:
                    if child.parent_id == parent.id:
                        child_pic = flatten(child)
                        parent_pic['child'].append(child_pic)
        success['complication'].append(parent_list)
        return True
    else:
        return False