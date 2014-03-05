# coding: UTF-8


# flask模块需要的配置参数
# ===============================================================
DEBUG = True  # 是否启动调试功能
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT^&556gh/ghj~hj/kh'  # session相关的密匙

# models模块需要的配置参数
# ===============================================================
# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@42.121.108.142:3306/doctor_baby?charset=utf8'  # 连接的数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/doctor_baby?charset=utf8'  # 连接的数据库
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@118.26.238.87:3306/doctor_baby?charset=utf8'  # 连接的数据库
SQLALCHEMY_ECHO = True  # 是否显示SQL语句

# ===============================================================
# 用户头像
HEAD_PICTURE_UPLOAD_FOLDER = '/static/img/system/head_picture'  # 运行目录的相对目录，URL获取图片的路径
HEAD_PICTURE_BASE_PATH = '/Users/K/Documents/Code/baby_py/baby'
HEAD_PICTURE_ALLOWED_EXTENSION = ('png', 'jpg', 'jpeg', 'gif')  # 允许的拓展名
