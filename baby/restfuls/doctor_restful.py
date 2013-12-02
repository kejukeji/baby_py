# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse

from baby.util.others import success_dic, fail_dic
from ..util.baby_doctor_commonality import format_baby, search_pickler, system_message_pickler

from ..services.baby_service import baby_collect_list, baby_list, search_by_keyword_time
from ..services.doctor_service import doctor_info, get_meeting_message, update_doctor, doctor_pickler
from ..services.search_history_service import search_history_list, delete_all_search
from ..services.academic_abstract_service import get_academic_abstract
from ..services.collect_service import insert_or_cancel_collects
import werkzeug


class BabyList(restful.Resource):
    """
        婴儿列表
    """
    @staticmethod
    def get():
        """
            所需参数：
                page: 分页，传入当前页码
                type：1列表，0收藏
        """
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=str, required=True, help=u'分页page，传入当前页')
        parser.add_argument('doctor_id', type=str, required=True, help=u'doctor_id 必须')

        args = parser.parse_args()
        page = args['page']
        doctor_id = args['doctor_id']

        resp_suc = success_dic().dic
        fail = fail_dic().dic
        resp_suc['baby_list'] = []
        baby = baby_list(page, int(doctor_id))
        if baby:
            if type(baby) is list:
                for bb in baby:
                    format_baby(bb, resp_suc)
            else:
                format_baby(baby, resp_suc)
            return resp_suc
        else:
            return fail


class BabyCollect(restful.Resource):
    """
        婴儿收藏列表
    """
    @staticmethod
    def get():
        """
            所需参数：
                doctor_id：登录医生id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('doctor_id', type=str, required=True, help=u'登录医生doctor_id')
        parser.add_argument('page', type=str, required=True, help=u'分页，传入当前page页码')

        args = parser.parse_args()
        doctor_id = args['doctor_id']
        page = args['page']
        resp_suc = success_dic().dic
        fail = fail_dic().dic
        resp_suc['baby_list'] = []
        baby_collect = baby_collect_list(page, doctor_id)
        if baby_collect:
            if type(baby_collect) is list:
                for baby_c in baby_collect:
                    format_baby(baby_c, resp_suc)
            else:
                format_baby(baby_collect, resp_suc)
            return resp_suc
        else:
            return fail


class DoctorInfo(restful.Resource):
    """
        医生我的个人资料
    """
    @staticmethod
    def post():
        """
            参数：
                doctor_id: 医生登录id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('doctor_id', type=str, required=True, help=u'医生登录doctor_id必须。')
        parser.add_argument('type', type=str, required=False)
        parser.add_argument('real_name', type=str, required=False)
        parser.add_argument('province', type=str, required=False)
        parser.add_argument('belong_hospital', type=str, required=False)
        parser.add_argument('belong_department', type=str, required=False)
        parser.add_argument('position', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('tel', type=str, required=False)
        parser.add_argument('upload_image', type=werkzeug.datastructures.FileStorage, location='files')

        args = parser.parse_args()

        success = success_dic().dic
        fail = fail_dic().dic
        success['doctor_list'] = []

        doctor_id = args['doctor_id']
        type_way = args['type']
        if type_way:
            real_name = args['real_name']
            province_id = args['province']
            belong_hospital = args['belong_hospital']
            belong_department = args['belong_department']
            position = args['position']
            email = args['email']
            tel = args['tel']
            upload_image = args['upload_image']
            is_ture = update_doctor(doctor_id, real_name, province_id, belong_hospital, belong_department, position,
                                    email, tel, upload_image, success)
            if is_ture:
                return success
            else:
                return fail
        else:
            doctor = doctor_info(doctor_id)
            if doctor:
                doctor_pickler(doctor, success)
                return success
            else:
                return fail


class Search(restful.Resource):
    """
        医生搜索婴儿
    """
    @staticmethod
    def get():
        """
            参数
                keyword：关键字搜索
                birthday_time：出生日期搜索
        """
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required=True, help=u'keyword关键字必须。')
        parser.add_argument('birthday_time', type=str, required=False)

        args = parser.parse_args()

        success = success_dic().dic
        fail = fail_dic().dic
        success['baby_list'] = []

        keyword = args['keyword']
        birthday_time = args['birthday_time']
        baby = search_by_keyword_time(keyword, birthday_time)
        if baby:
            format_baby(baby, success)
            return success
        else:
            return fail


class Search_View(restful.Resource):
    """
        搜索界面需要的历史记录
    """
    @staticmethod
    def get():
        """

        """
        success = success_dic().dic
        fail = fail_dic().dic
        success['search_history_list'] = []

        search_history = search_history_list()
        if search_history:
            if type(search_history) is list:
                for search in search_history:
                    search_pickler(search, success)
            else:
                search_pickler(search_history, success)
            return success
        else:
            return fail


class DeleteSearchHistoryAll(restful.Resource):
    """
        清楚历史记录
    """
    @staticmethod
    def get():
        """

        """
        success = success_dic().dic
        fail = fail_dic().dic
        result = delete_all_search()
        if result == 0:
            return success
        else:
            return fail


class MeetingNotice(restful.Resource):
    """
        会议通知以及育儿指南
    """
    @staticmethod
    def get():
        """
            参数:
                id: 登录id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help=u'登录的id')

        args = parser.parse_args()

        id = args['id']
        success = success_dic().dic
        fail = fail_dic().dic
        success['system_message_list'] = []

        system_message = get_meeting_message(id)
        if system_message:
            if type(system_message) is list:
                for system in system_message:
                    system_message_pickler(system, success)
            else:
                system_message_pickler(system_message, success)
            return success
        else:
            return fail


class AcademicAbstract(restful.Resource):
    """
       学术文摘
    """
    @staticmethod
    def get():
        """
        page: 分页
        """
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=str, required=True, help=u'page 必须')

        args = parser.parse_args()

        page = args['page']

        success = success_dic().dic
        fail = fail_dic().dic
        # 调用service中方法获取model数据
        # 根据返回的boolean值来判断是否有数据
        is_true = get_academic_abstract(page, success)

        if is_true:
            return success
        else:
            return fail


class DoctorCollect(restful.Resource):
    """
    收藏baby
    """
    @staticmethod
    def get():
        """
        argument:
        1.type: 收藏类型，baby  or  abstract
        2.baby_id: 收藏baby id
        3.abstract_id: 收藏abstract id
        4.doctor_id: 医生id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, required=True, help=u'type 必须')
        parser.add_argument('doctor_id', type=str, required=True, help=u'doctor_id 必须')
        parser.add_argument('baby_id', type=str)
        parser.add_argument('abstract_id', type=str)

        args = parser.parse_args()

        collect_type = args['type']
        doctor_id = args['doctor_id']
        baby_id = args['baby_id']
        abstract_id = args['abstract_id']

        success = success_dic().dic
        fail = fail_dic().dic

        if baby_id:
            is_true = insert_or_cancel_collects(doctor_id, baby_id, collect_type)
            if is_true:
                return success
            else:
                return fail
        if abstract_id:
            is_true = insert_or_cancel_collects(doctor_id, abstract_id, collect_type)
            if is_true:
                return success
            else:
                return fail
