# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from ..util.others import success_dic, fail_dic
from ..services.baby_service import get_baby_info, get_parenting_guide, update_baby
from ..util.baby_doctor_commonality import system_message_pickler
import werkzeug


class BabyInfo(restful.Resource):
    """
        婴儿个人资料
    """
    @staticmethod
    def post():
        """
            参数:
                baby_id：婴儿登录id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('baby_id', type=str, required=True, help=u'婴儿baby_id必须。')
        parser.add_argument('type', type=str, required=False)
        parser.add_argument('patriarch_tel', type=str, required=False)
        parser.add_argument('baby_name', type=str, required=False)
        parser.add_argument('due_date', type=str, required=False)
        parser.add_argument('gender', type=str, required=False)
        parser.add_argument('born_weight', type=str, required=False)
        parser.add_argument('born_height', type=str, required=False)
        parser.add_argument('born_head', type=str, required=False)
        parser.add_argument('childbirth_style_id', type=str, required=False)
        parser.add_argument('complication_id', type=str, required=False)
        parser.add_argument('apagar_score', type=str, required=False)
        parser.add_argument('upload_image', type=werkzeug.datastructures.FileStorage, location='files')



        args = parser.parse_args()

        baby_id = args['baby_id']
        type_way = args['type']

        success = success_dic().dic
        fail = fail_dic().dic
        success['baby_list'] = []



        if type_way:
            patriarch_tel = args['patriarch_tel']
            baby_name = args['baby_name']
            due_date = args['due_date']
            born_weight = args['born_weight']
            born_height = args['born_height']
            born_head = args['born_head']
            childbirth_style_id = args['childbirth_style_id']
            complication_id = args['complication_id']
            apagar_score = args['apagar_score']
            upload_image = args['upload_image']
            gender = args['gender']
            is_ture = update_baby(baby_id, patriarch_tel, baby_name, due_date, gender, born_weight, born_height, born_head, childbirth_style_id,
                        complication_id, apagar_score, upload_image, success)
            if is_ture:
                return success
            else:
                return fail
        else:
            baby = get_baby_info(baby_id, success)
            if baby:
                return success
            else:
                return fail


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

