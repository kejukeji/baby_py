# coding: UTF-8

from baby import app
from flask.ext import restful
from restfuls.doctor_restful import *
from restfuls.baby_restful import BabyInfo, ParentingGuide
from restfuls.login_register import DoLogin, RegisterData, AlterPassword, DoRegisterDoctor, CreateBabyAccount
from baby.controls.user_feature_control import *
from baby.controls.baby_control import *
from baby.controls.doctor_control import *
from baby.restfuls.feature_restful import AddFormula, AddVisitRecord

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

# html页面访问路劲
app.add_url_rule('/html/login.html', 'to_login', to_login, methods={ 'GET', 'POST'})
app.add_url_rule('/html/password.html', 'to_update_password', to_update_password, methods={'GET', 'POST'})
app.add_url_rule('/html/register.html', 'to_register', to_register, methods={'GET', 'POST'})
app.add_url_rule('/html/grow_line.html/<int:id>', 'to_grow_line', to_grow_line, methods={ 'GET', 'POST'})
app.add_url_rule('/html/raise.html', 'to_raise', to_raise, methods={'GET', 'POST'})
app.add_url_rule('/html/meeting.html', 'to_meeting', to_meeting, methods={'GET', 'POST'})
app.add_url_rule('/html/academic.html', 'to_academic', to_academic, methods={'GET', 'POST'})
app.add_url_rule('/html/formula.html', 'to_formula', to_formula, methods={'GET', 'POST'})
app.add_url_rule('/html/add_follow-up.html', 'to_additional_follow_up', to_additional_follow_up, methods={'GET', 'POST'})
app.add_url_rule('/html/visit_record.html/<int:baby_id>', 'to_record', to_record, methods={'GET', 'POST'})
app.add_url_rule('/html/create_baby.html', 'to_create_baby_account', to_create_baby_account, methods={'GET', 'POST'})
app.add_url_rule('/html/need.html', 'to_need', to_yy_need, methods={'GET', 'POST'})
app.add_url_rule('/html/meeting_notice.html', 'to_meeting_notice', to_meeting_notice, methods={'GET', 'POST'})
app.add_url_rule('/html/raise_dir.html', 'to_raise_dir', to_raise_dir, methods={'GET', 'POST'})
app.add_url_rule('/html/baby_detail.html/<int:baby_id>', 'to_baby_detail', to_baby_detail, methods={'GET', 'POST'})
app.add_url_rule('/html/grow_bar.html/<int:id>', 'to_grow_bar', to_grow_bar, methods={'GET', 'POST'})

# 接口访问路径
api = restful.Api(app)

api.add_resource(BabyList, '/restful/baby/list')
api.add_resource(BabyCollect, '/restful/baby/collect/list')
api.add_resource(DoctorInfo, '/restful/doctor/info')
api.add_resource(Search, '/restful/doctor/search')
api.add_resource(Search_View, '/restful/doctor/search/history')
api.add_resource(DeleteSearchHistoryAll, '/restful/doctor/delete/search_history')
api.add_resource(MeetingNotice, '/restful/doctor/meeting/notice')
api.add_resource(BabyInfo, '/restful/baby/info')
api.add_resource(ParentingGuide, '/restful/baby/parenting/guide')
api.add_resource(DoLogin, '/restful/html/do/login')
api.add_resource(RegisterData, '/restful/html/register/data')
api.add_resource(AlterPassword, '/restful/html/forget/password')
api.add_resource(DoRegisterDoctor, '/restful/html/do/register')
api.add_resource(AcademicAbstract, '/restful/html/academic')
api.add_resource(AddFormula, '/restful/html/add/formula')
api.add_resource(CreateBabyAccount, '/restful/html/create/baby')
api.add_resource(AddVisitRecord, '/restful/html/add/visit')