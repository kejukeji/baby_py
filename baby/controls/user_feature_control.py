# coding: UTF-8

from flask import render_template, request
from baby.util.others import get_session_user
from baby.services.more_service import check_login, get_department, get_hospital\
    , get_position, get_province



def to_login():
    """
       to login
    """
    return render_template('user_feature/login.html')



def do_login():
    """
       所属参数
          login_name:登陆名
          login_pass:密码
    """
    login_name = request.form.get('login_name', '')
    login_pass = request.form.get('login_pass', '')
    result = check_login(login_name, login_pass)
    if result:
        return render_template('user_feature/index.html')
    else:
        return render_template('user_feature/login.html')




def to_update_password():
    """
       to update password
    """
    return render_template('user_feature/password.html')



def update_password():
    """
       参数：
          1.旧密码
          2.新密码
    """
    user_name = get_session_user()
    return 'True'



def to_register():
    '''到注册界面'''
    province, province_count = get_province()
    hospital, hospital_count = get_hospital()
    department, department_count = get_department()
    position, position_count = get_position()
    return render_template('user_feature/register.html',
                           province = province,
                           hospital = hospital,
                           department = department,
                           position = position,
                           province_count = province_count,
                           hospital_count = hospital_count,
                           department_count = department_count,
                           position_count = position_count)


def standard():
    #entering_who()
    return render_template('index.html')


def to_formula():
    return render_template('doctor/formula_milk.html')

def to_additional_follow_up():
    return render_template('doctor/add_visit_record.html')