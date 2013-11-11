# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from ..util.others import success_dic, fail_dic
from ..services.baby_service import get_baby_info, get_parenting_guide
from ..util.baby_doctor_commonality import format_baby, system_message_pickler


class BabyInfo(restful.Resource):
    """
        婴儿个人资料
    """
    @staticmethod
    def get():
        """
            参数:
                baby_id：婴儿登录id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('baby_id', type=str, required=True, help=u'婴儿baby_id必须。')

        args = parser.parse_args()

        baby_id = args['baby_id']
        resp_suc = success_dic().dic
        resp_fail = fail_dic().dic

        resp_suc['baby_list'] = []
        baby = get_baby_info(baby_id)
        if baby:
            format_baby(baby, resp_suc)
            return resp_suc
        else:
            return resp_fail


class ParentingGuide(restful.Resource):
    """
        育儿指南
    """
    @staticmethod
    def get():
        """
            参数:
                baby_id: 婴儿登录id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('baby_id', type=str, required=True, help=u'婴儿登录baby_id必须。')

        args = parser.parse_args()

        baby_id = args['baby_id']
        resp_suc = success_dic().dic
        resp_fail = fail_dic().dic
        resp_suc['system_message_list'] = []
        parenting_guide = get_parenting_guide(baby_id)
        if parenting_guide:
            if type(parenting_guide) is list:
                for parenting in parenting_guide:
                    system_message_pickler(parenting, resp_suc)
            else:
                system_message_pickler(parenting_guide, resp_suc)
            return resp_suc
        else:
            return resp_fail

