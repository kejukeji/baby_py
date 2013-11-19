# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.more_service import check_login, get_position, get_province, get_department, get_hospital
from baby.util.others import success_dic, fail_dic
from baby.util.baby_doctor_commonality import format_baby, doctor_pickler, register_data_department\
    , register_data_hospital, register_data_position, register_data_province
from baby.models.baby_model import Baby


class DoLogin(restful.Resource):
    """
       参数：
          1.login_name
          2.login_pass
          3.remember (1.代表记住）
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('login_name', type=str, required=True, help=u'login_name 必须')
        parser.add_argument('login_pass', type=str, required=True, help=u'login_pass 必须')
        parser.add_argument('remember', type=str, required=True, help=u'remember 必须')

        args = parser.parse_args()

        return_success = success_dic().dic
        return_fail = fail_dic().dic

        login_name = args.get('login_name')
        login_pass = args.get('login_pass')
        remember = args.get('remember')
        result = check_login(login_name, login_pass)
        if result:
            if type(result) is Baby:
                return_success['baby_list'] = []
                format_baby(result, return_success)
            else:
                return_success['doctor_list'] = []
                doctor_pickler(result, return_success)
            return_success['remember'] = remember
            return return_success
        else:
            return return_fail


class DoRegister(restful.Resource):
    """
       注册:
    """


class RegisterData(restful.Resource):
    """
       注册下拉列表数据
    """
    @staticmethod
    def get():
        province, province_count = get_province()
        hospital, hospital_count = get_hospital()
        department, department_count = get_department()
        position, position_count = get_position()

        return_success = success_dic().dic
        return_fail = fail_dic().dic

        if province and hospital and department and position:
            register_data_province(province, return_success)
            register_data_position(position, return_success)
            register_data_hospital(hospital, return_success)
            register_data_department(department, return_success)
            return return_success
        else:
            return return_fail
