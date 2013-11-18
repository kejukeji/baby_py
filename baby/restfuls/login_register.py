# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.more_service import check_login
from baby.util.others import success_dic, fail_dic


class DoLogin(restful.Resource):
    """
       参数：
          1.login_name
          2.login_pass
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('login_name', type=str, required=True, help=u'login_name 必须')
        parser.add_argument('login_pass', type=str, required=True, help=u'login_pass 必须')

        args = parser.parse_args()

        return_success = success_dic().dic
        return_fail = fail_dic().dic

        return_success['user_list'] = []

        login_name = args.get['login_name', '']
        login_pass = args.get['login_pass', '']
        result = check_login(login_name, login_pass)
        if result:
            return return_success
        else:
            return return_fail
