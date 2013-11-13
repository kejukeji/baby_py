# coding: UTF-8

from flask import render_template, request
from baby import app
from baby.models.baby_model import Baby
from baby.models.hospital_model import Doctor


@app.route('/login/', methods={'GET', 'POST'})
def login_control():
    """
       to login
    """
    return render_template('user_feature/login.html')


@app.route('/do/login', methods={'GET', 'POST'})
def do_login_control():
    """
       所属参数
          login_name:登陆名
          login_pass:密码
    """
    login_name = request.form.get('login_name', '')
    login_pass = request.form.get('login_pass', '')
    baby = Baby.query.filter()


@app.route('/update/password/', methods={'GET', 'POST'})
def update_password_control():
    """
       to update password
    """
    return render_template('user_feature/password.html')