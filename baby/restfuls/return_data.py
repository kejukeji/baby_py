# coding: UTF-8

from flask.ext import restful
from baby.util.others import success_dic, fail_dic
from baby.services.complication import *
from baby.services.feature_service import *


class Complication(restful.Resource):
    """
    合并症
    """
    @staticmethod
    def get():
        success = success_dic().dic
        fail = fail_dic().dic

        is_true = get_complication(success)
        if is_true:
            return success
        else:
            fail['message'] = '没有数据'
            return fail


class RegisterData(restful.Resource):
    """
    注册数据
    """
    @staticmethod
    def get():
        success = success_dic().dic
        format_province_hospital(success)
        return success