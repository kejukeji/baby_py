# coding: UTF-8

from baby import app
from flask.ext import restful
from restfuls.doctor_restful import BabyList, BabyCollect, DoctorInfo, Search

# # 后台Admin
# admin = Admin(name=u'小宇')
# # 初始化app
# admin.init_app(app)
#
# # 上传图片路径
# file_path = os.path.join(os.path.dirname(__file__), 'static')
# admin.add_view(Yu_File(file_path, '/static/', name='文件'))
# yu_picture_path = os.path.join(os.path.dirname(__file__), 'static/system/baby_picture')
# admin.add_view(Yu_Picture_File(yu_picture_path, 'baby/static/system/baby_picture/', name='YuImage', category=u'Yu'))

# 接口访问路径
api = restful.Api(app)

api.add_resource(BabyList, '/restful/baby/list')
api.add_resource(BabyCollect, '/restful/baby/collect/list')
api.add_resource(DoctorInfo, '/restful/doctor/info')
api.add_resource(Search, '/restful/doctor/search')