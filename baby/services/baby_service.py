# coding: UTF-8

from ..models.baby_model import Baby, BabyPicture
from ..models import db
from ..models.feature_model import Collect, SearchHistory, SystemMessage
from ..util.seesion_query import *
from ..util.others import page_utils


def baby_list(page):
    """
        全部婴儿列表
    """
    baby_count = Baby.query.filter().count()
    page, per_page = page_utils(baby_count, page)
    if baby_count > 1:
        babys = Baby.query.filter()[per_page*(page-1):per_page*page]
        return babys
    else:
        baby = Baby.query.filter().first()
        return baby


def baby_collect_list(page, doctor_id):
    """
        得到医生收藏婴儿列表
            page: 分页，当前页
            doctor_id: 医生的id
    """
    result_count = session.query(Baby). \
        filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').count()
    page, per_page = page_utils(result_count, page)
    if result_count > 1:
        results = session.query(Baby).\
            filter(Collect.doctor_id == doctor_id, Collect.type == 'baby')[per_page*(page-1):per_page*page]
        return results
    else:
        result = session.query(Baby).\
            filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').first()
        return result


def search_by_keyword_time(keyword, time):
    """
        根据关键字或者时间来搜索
        关键字时间一起搜索
    """
    if keyword:
        baby = Baby.query.filter(Baby.baby_name.like('%' + keyword + '%')).first()
        search_history = SearchHistory(keyword=keyword)
        db.add(search_history)
        db.commit()
        return baby
    #if time:
    #    baby = Baby.quer.filter().first()
    #    return baby


def is_null(obj):
    '''判断是否为空'''
    if obj:
        if obj.rel_path and obj.picture_name:
            return True
    else:
        return False


def get_baby_info(baby_id):
    """
        得到婴儿信息
            baby_id：婴儿登录id
    """
    baby = Baby.query.filter(Baby.id == baby_id).first()
    baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == baby_id).first()
    bool = is_null(baby_picture)
    if bool:
        baby.picture_path = baby_picture.rel_path + '/' + baby_picture.picture_name
    return baby


def get_parenting_guide(baby_id):
    """
        得到育儿指南
            baby_id: 婴儿登录id
    """
    baby = Baby.query.filter(Baby.id == baby_id).first()
    if baby:
        system_message_count = SystemMessage.query.filter(SystemMessage.type == 'guide').count()
        if system_message_count > 1:
            system_messages = SystemMessage.query.filter(SystemMessage.type == 'guide')[:3]
            return system_messages
        else:
            system_message = SystemMessage.query.filter(SystemMessage.type == 'guide').first()
            return system_message