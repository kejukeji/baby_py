# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.formula import *
from baby.util.others import success_dic, fail_dic


class AddVisitRecordData(restful.Resource):
    """
    新增随访记录
       奶粉数据
    """
    @staticmethod
    def get():
        success = success_dic().dic
        fail = fail_dic().dic

        court_list = is_list_court()
        brand_list = is_list_brand()
        kind_list = is_list_kind()

        success['court'] = court_list
        success['brand'] = brand_list
        success['kind'] = kind_list

        return success

