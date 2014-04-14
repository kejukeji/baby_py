# coding: UTF-8

from flask import render_template, request, redirect
from baby.util.others import get_session_user
from baby.services.more_service import check_login, get_department, get_hospital\
    , get_position, get_province
from baby.services.more_service import get_tracking
from baby.services.feature_service import get_court, get_brand, get_formula
from baby.services.formula import get_brand_out, get_court, get_brand_in
from baby.util.others import set_session_user



def to_login():
    """
       to login
    """
    return render_template('user_feature/login.html')


def to_mummy_login():
    """
    to mummy
    """
    return render_template('user_feature/mummy_login.html')



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
    user_id = request.args.get('user_id')
    type = request.args.get('type', 'doctor')
    set_session_user('user_id', user_id, '', '')
    set_session_user('type', type, '','')
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
    court, court_count = get_court()
    brand_in, brand_in_count = get_brand_in()
    brand_out, brand_out_count = get_brand_out()
    return render_template('doctor/formula_milk.html',
                           court=court,
                           court_count=court_count,
                           brand_in=brand_in,
                           brand_in_count=brand_in_count,
                           brand_out=brand_out,
                           brand_out_count=brand_out_count)

def to_formula_out():
    court, court_count = get_court()
    brand_in, brand_in_count = get_brand_out()
    return render_template('doctor/formula_milk_out.html',
                           court=court,
                           court_count=court_count,
                           brand_in=brand_in,
                           brand_in_count=brand_in_count)


def to_additional_follow_up(baby_id):
    login_type = request.args.get('type', 'doctor')
    court, court_count = get_court()
    brand, brand_count = get_brand()
    formula, formula_count = get_formula()
    return render_template('doctor/add_visit_record.html',
                           courts=court,
                           brands=brand,
                           formulas=formula,
                           court_count=court_count,
                           brand_count=brand_count,
                           formula_count=formula_count,
                           baby_id=baby_id,
                           login_type=login_type)