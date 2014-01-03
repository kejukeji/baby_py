# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.more_service import *
from baby.util.others import success_dic, fail_dic, get_session
from baby.util.baby_doctor_commonality import register_data_department, register_data_hospital, register_data_position,\
    register_data_province
from baby.services.doctor_service import register_doctor
from baby.services.baby_service import create_baby


class DoLogin(restful.Resource):
    """
       参数：
          1.login_name
          2.login_pass
          3.remember (1.代表记住）
          4.type
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('login_name', type=str, required=True, help=u'login_name 必须')
        parser.add_argument('login_pass', type=str, required=True, help=u'login_pass 必须')
        parser.add_argument('remember', type=str, required=True, help=u'remember 必须')
        parser.add_argument('login_type', type=str, required=True, help=u'login_type 必须')

        args = parser.parse_args()

        return_success = success_dic().dic
        return_fail = fail_dic().dic

        login_name = args.get('login_name')
        login_pass = args.get('login_pass')
        remember = args.get('remember')
        login_type = args.get('login_type')
        result = check_login(login_name, login_pass, login_type)
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
        if is_true != 0:
            success['doctor_id'] = is_true
            success['msg'] = '注册成功'
            return success
        else:
            fail['msg'] = '注册失败'
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


class ForgetPassword(restful.Resource):
    """
       修改密码
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        # parser.add_argument('user_id', type=str, required=True, help=u'user_id 必须')
        parser.add_argument('old_password', type=str, required=True, help=u'old_password 必须')
        parser.add_argument('new_password', type=str, required=True, help=u'new_password 必须')

        args = parser.parse_args()

        old_password = args['old_password']
        new_password = args['new_password']
        # user_id = args['user_id']

        return_success = success_dic().dic
        return_fail = fail_dic().dic
        user_id = get_session('user_id')
        if user_id is None:
            return_fail.pop('message')
            return_fail['msg'] = '请先登录!'
            return_fail.pop('code')
            return_fail['code'] = 404
            return return_fail

        is_true = by_id_alter_password(user_id, old_password, new_password)
        if is_true:
            return_success['message'] = '修改密码成功'
            return return_success
        else:
            return_success['message'] = '旧密码不正确'
            return return_success


class CreateBabyAccount(restful.Resource):
    """
    创建婴儿账户
    """
    @staticmethod
    def post():
        """
        参数：
        baby_name	    婴儿名
        login_name      婴儿登陆
        gender		    性别
        due_date	    预产期
        born_birthday	出生日期
        born_weight		出生体重
        born_height		出生身高
        born_head		出生头围
        childbirth_style	分娩方式
        complication_id	合并症(可以多选，实用逗号隔开)
        restore_day		恢复出生体重天数
        apgar_score		Apgar评分
        """
        parser = reqparse.RequestParser()
        parser.add_argument('patriarch_tel', type=str, required=True, help=u'patriarch_tel 必须')
        parser.add_argument('baby_name', type=str, required=True, help=u'baby_name 必须')
        # parser.add_argument('login_name', type=str, required=True, help=u'login_name 必须')
        parser.add_argument('baby_pass', type=str, required=True, help=u'baby_pass 必须')
        parser.add_argument('gender', type=str, required=True, help=u'gender 必须')
        parser.add_argument('due_date', type=str, required=True, help=u'due_date 必须')
        parser.add_argument('born_birthday', type=str, required=True, help=u'born_birthday 必须')
        parser.add_argument('born_weight', type=str, required=True, help=u'born_weight 必须')
        parser.add_argument('born_height', type=str, required=True, help=u'born_height 必须')
        parser.add_argument('born_head', type=str, required=True, help=u'born_head 必须')
        parser.add_argument('childbirth_style', type=str, required=True, help=u'childbirth_style 必须')
        parser.add_argument('complication_id', type=str, required=True, help=u'complication_id 必须')
        parser.add_argument('growth_standard', type=str, required=False)
        # parser.add_argument('restore_day', type=str, required=True, help=u'restore_day 必须')
        # parser.add_argument('apgar_score', type=str, required=True, help=u'apgar_score 必须')

        args = parser.parse_args()

        success = success_dic().dic
        fail = fail_dic().dic

        patriarch_tel = args['patriarch_tel']
        baby_name = args['baby_name']
        baby_pass = args['baby_pass']
        # login_name = args['login_name']
        gender = args['gender']
        due_date = args['due_date']
        born_birthday = args['born_birthday']
        born_weight = args['born_weight']
        born_height = args['born_height']
        born_head = args['born_head']
        childbirth_style = args['childbirth_style']
        complication_id = args['complication_id']
        growth_standard = args['growth_standard']
        # restore_day = args['restore_day']
        # apgar_score = args['apgar_score']
        is_ture = create_baby(patriarch_tel, baby_name, baby_pass, gender, due_date, born_birthday, born_weight, born_height, born_head,
                              childbirth_style, complication_id, growth_standard)
        if is_ture != 0:
            success['baby_id'] = is_ture
            success['msg'] = '创建账户成功'
            return success
        elif is_ture == 1:
            fail['message'] = '账户已经存在'
        else:
            fail['message'] = '创建账户失败!系统内部错误'
            return fail
