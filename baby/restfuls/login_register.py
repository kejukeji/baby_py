# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.more_service import *
from baby.util.others import success_dic, fail_dic
from baby.util.baby_doctor_commonality import register_data_department, register_data_hospital, register_data_position,\
    register_data_province
from baby.services.doctor_service import register_doctor


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
        is_true = check_is_type(result, remember, return_success)
        if is_true:
            return return_success
        else:
            return return_fail


class DoRegisterDoctor(restful.Resource):
    """
       注册:
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('login_name', type=str, required=True, help=u'login_name 必须')
        parser.add_argument('login_pass', type=str, required=True, help=u'login_pass 必须')
        parser.add_argument('real_name', type=str, required=True, help=u'real_name 必须')
        parser.add_argument('province_id', type=str, required=True, help=u'province_id 必须')
        parser.add_argument('belong_hospital', type=str, required=True, help=u'belong_hospital 必须')
        parser.add_argument('belong_department', type=str, required=True, help=u'belong_department 必须')
        parser.add_argument('position', type=str, required=True, help=u'position 必须')
        parser.add_argument('email', type=str, required=True, help=u'email 必须')
        parser.add_argument('tel', type=str, required=True, help=u'tel 必须')

        args = parser.parse_args()

        success = success_dic().dic
        fail = fail_dic().dic

        login_name = args.get('login_name')
        login_pass = args.get('login_pass')
        real_name = args.get('real_name')
        province_id = args.get('province_id')
        belong_hospital = args.get('belong_hospital')
        belong_department = args.get('belong_department')
        position = args.get('position')
        email = args.get('email')
        tel = args.get('tel')
        is_true = register_doctor(login_name, login_pass, real_name, province_id, belong_hospital, belong_department,
                                  position, email, tel)
        if is_true:
            success['doctor_id'] = 1
            success.pop('code')
            success['is_code'] = 200
            return success
        else:
            fail.pop('code')
            fail['is_code'] = 500
            return fail


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


class AlterPassword(restful.Resource):
    """
       修改密码
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True, help=u'user_id 必须')
        parser.add_argument('old_password', type=str, required=True, help=u'old_password 必须')
        parser.add_argument('new_password', type=str, required=True, help=u'new_password 必须')

        args = parser.parse_args()

        old_password = args['old_password']
        new_password = args['new_password']
        user_id = args['user_id']

        return_success = success_dic().dic
        return_fail = fail_dic().dic

        is_true = by_id_alter_password(user_id, old_password, new_password)
        if is_true:
            return_success.pop('code')
            return_success['is_code'] = 200
            return return_success
        else:
            return_fail.pop('code')
            return_fail['is_code'] = 500
            return return_fail
