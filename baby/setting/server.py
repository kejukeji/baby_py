# coding: utf-8

from baby.setting.secret import EX_DB_PASSWORD, EX_DB_USER, EX_SECRET_KEY_SERVER, EX_DB_NAME

# flask模块需要的配置参数
# ===============================================================
DEBUG = False  # 是否启动调试功能
SECRET_KEY = EX_SECRET_KEY_SERVER  # session相关的密匙

# models模块需要的配置参数
# ===============================================================
SQLALCHEMY_DATABASE_URI = 'mysql://' + EX_DB_USER + ':' + EX_DB_PASSWORD + '@127.0.0.1:3306/' \
                          + EX_DB_NAME + '?charset=utf8'  # 连接的数据库
SQLALCHEMY_ECHO = False  # 是否显示SQL语句


# ===============================================================
# 用户头像
HEAD_PICTURE_UPLOAD_FOLDER = '/static/img/system/head_picture'  # 运行目录的相对目录，URL获取图片的路径
HEAD_PICTURE_BASE_PATH = '/var/www/baby_py/baby'
HEAD_PICTURE_ALLOWED_EXTENSION = ('png', 'jpg', 'jpeg', 'gif')  # 允许的拓展名