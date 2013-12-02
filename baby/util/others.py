# coding: utf-8

from wtforms import BooleanField
from flask import session
import jsonpickle
import datetime

pickler = jsonpickle.pickler.Pickler(unpicklable=False, max_depth=2)


def flatten(model):
    """去除pickler.flatten里面的一个字段"""
    json = pickler.flatten(model)
    json.pop('_sa_instance_state', None)
    return json


def form_to_dict(form):
    form_dict = {}

    for key in form._fields:  # 可以编写一个更好的函数，可惜我不会。。。
        if isinstance(form._fields[key].data, BooleanField) or isinstance(form._fields[key].data, int):
            form_dict[key] = form._fields[key].data
            continue

        if form._fields[key].data:
            form_dict[key] = form._fields[key].data

    return form_dict


def time_diff(dt):
    dt = datetime.datetime.strptime(str(dt), "%Y-%m-%d %H:%M:%S")
    today = datetime.datetime.today()
    s = int((today - dt).total_seconds())

    # day_diff > 365, use year
    if s / 3600 / 24 >= 365:
        return str(s / 3600 / 24 / 365) + " 年"
    elif s / 3600 / 24 >= 30:  # day_diff > 30, use month
        return str(s / 3600 / 24 / 30) + " 个月"
    elif s / 3600 >= 24:  # hour_diff > 24, use day
        return str(s / 3600 / 24) + " 天"
    elif s / 60 > 60:  # minite_diff > 60, use hour
        return str(s / 3600) + " 小时"
    elif s > 60:  # second_diff > 60, use minite
        return str(s / 60) + " 分钟"
    else:  # use "just now"
        return "刚刚"


def page_utils(count, page, per_page=6):
    min = 1
    max = count / per_page if count % per_page == 0 else count / per_page + 1
    page = page if ( page >= min and page <= max  ) else 1

    return page, per_page


def isNotNull(object):
    if object:
        if type(object) is list:
            return True
        else:
            return False
    else:
        return False


#取得一个正确的返回字典
class success_dic(object):
    def __init__(self):
        self.dic = {}
        self.dic['code'] = 200
        self.dic['message'] = 'success'
        #self.dic['test'] = 'test success'

    def set(self, k, v):
        self.dic[k] = v


#取得一个错误的返回字典
class fail_dic(object):
    def __init__(self):
        self.dic = {}
        self.dic['code'] = 500
        self.dic['message'] = 'error！'
        #self.dic['test'] = 'test fail'

    def set(self, k, v):
        self.dic[k] = v


def get_session_user():
    if session.has_key('user') and session['user']:
        #这里只能传递一个字符串，不然会报没有序列化的错
        return session['user']
    return None


def get_session(key):
    '''获取session中key的值'''
    if session.has_key(str(key)) and session[str(key)]:
        return session[str(key)]
    return None


def set_session_user(key_name, value_name, key_id, value_id):
    """
       登陆成功保存到session当中
    """
    session[str(key_name)] = value_name
    session[str(key_id)] = value_id