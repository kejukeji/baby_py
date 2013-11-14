# coding: UTF-8

from flask import render_template, request
from baby import app
from baby.models.baby_model import Baby
from baby.models.hospital_model import Doctor
from baby.util.others import get_session_user
from baby.services.more_service import check_login


@app.route('/html/login.html/', methods={'GET', 'POST'})
def to_login():
    """
       to login
    """
    return render_template('user_feature/login.html')


@app.route('/do/login', methods={'GET', 'POST'})
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



@app.route('/html/password.html/', methods={'GET', 'POST'})
def to_update_password():
    """
       to update password
    """
    return render_template('user_feature/password.html')


@app.route('/update/password/', methods={'GET', 'POST'})
def update_password():
    """
       参数：
          1.旧密码
          2.新密码
    """
    user_name = get_session_user()
    return 'True'


@app.route('/html/register.html')
def to_register():
    '''到注册界面'''
    return render_template('user_feature/register.html')
