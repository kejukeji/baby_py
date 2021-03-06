# coding: UTF-8

from sqlalchemy import or_, and_
from baby.models.baby_model import Baby, BabyPicture
from baby.models.hospital_model import Doctor, Province, Hospital, Department, Position
from baby.util.others import set_session_user, time_diff, flatten, get_session, page_utils
from baby.models.feature_model import Tracking
from baby.models.baby_model import Complication, ChildbirthStyle
from baby.models.database import db, engine
from .tracking_service import get_tracking_model
from .baby_service import get_picture_by_id
from .formula import *
from baby.models.standard import *
from baby.models.nine_standard import *
from baby.models.fentong_standard import *
from baby.util.ex_time import *
import datetime
import math


def check_login(login_name, login_pass, login_type):
    """
       login_name: 登陆名
       login_pass: 登陆密码
    """
    if login_type == 'mummy':
        baby = Baby.query.filter(Baby.patriarch_tel == login_name, Baby.baby_pass == login_pass).first()
        if baby != None:
            set_session_user('user', baby.login_name, 'user_id', baby.id)
            set_session_user('login_type', login_type, '','')
            return baby
        else:
            return None
    if login_type == 'doctor':
        doctor = Doctor.query.filter(or_(and_(Doctor.doctor_name == login_name, Doctor.doctor_pass == login_pass), and_(Doctor.email == login_name, Doctor.doctor_pass == login_pass))).first()
        if doctor != None:
            set_session_user('user', doctor.doctor_name, 'user_id', doctor.id)
            set_session_user('login_type', login_type, '','')
            return doctor
        else:
            return None


def is_null(model):
    '''判断一个model是否为空'''
    if model:
        return True
    else:
        return False


def by_count(model, count):
    if count > 1:
        result_model = model.query.filter().all()
        return model
    else:
        result_model = model.query.filter().first()
        if result_model:
            return result_model


def get_province():
    '''得到注册所需要的省'''
    province_count = Province.query.filter().count()
    if province_count > 1:
        province = Province.query.filter().all()
    else:
        province = Province.query.filter().first()
    return province, province_count


def get_hospital():
    '''得到注册所需要的医院'''
    hospital_count = Hospital.query.filter().count()
    if hospital_count > 1:
        hospital = Hospital.query.filter().all()
    else:
        hospital = Hospital.query.filter().first()
    return hospital, hospital_count


def get_department():
    '''得到注册所需要的部门'''
    department_count = Department.query.filter().count()
    if department_count > 1:
        department = Department.query.filter().all()
    else:
        department = Department.query.filter().first()
    return department, department_count


def get_position():
    '''得到注册所需要的职位'''
    position_count = Position.query.filter().count()
    if position_count > 1:
        position = Position.query.filter().all()
    else:
        position = Position.query.filter().first()
    return position, position_count


def by_id_alter_password(user_id, old_password, new_password, type):
    """
       通过user_id来获取信息
          判断old_password是否正确
             修改密码
    """
    entrance = get_session('entrance')
    if type == 'baby':
        baby = Baby.query.filter(Baby.id == user_id).first()
        if baby:
            if baby.baby_pass == old_password:
                baby.baby_pass = new_password
                try:
                    db.commit()
                except:
                    return False
                return True
            else:
                return False
    elif type is None or type == 'doctor':
        doctor = Doctor.query.filter(Doctor.id == user_id).first()
        if doctor:
            if doctor.doctor_pass == old_password:
                doctor.doctor_pass = new_password
                try:
                    db.commit()
                except:
                    return False
                return True
            else:
                return False


def json_append(return_success, obj_pic):
    return_success['doctor_list'] = obj_pic


def check_is_type(result, remember, return_success):
    """
       判断登陆是baby还是doctor
    """
    if result:
        if type(result) is Baby:
            baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == result.id).first()
            baby_pic = flatten(result)
            baby_pic['is_remember'] = int(remember)
            baby_pic.pop('id')
            baby_pic['user_id'] = result.id
            baby_pic['user_name'] = result.baby_name
            if result.born_birthday:
                baby_birthday = result.born_birthday
                baby_pic['time'] = time_diff(baby_birthday)
            if baby_picture:
                if baby_picture.rel_path and baby_picture.picture_name:
                    baby_pic['picture_path'] = baby_picture.rel_path + '/' + baby_picture.picture_name
            json_append(return_success, baby_pic)
            return True
        elif type(result) is Doctor:
            doctor_pic = flatten(result)
            doctor_pic['is_remember'] = int(remember)
            doctor_pic.pop('id')
            doctor_pic['user_name'] = result.real_name
            doctor_pic['user_id'] = result.id
            if result.rel_path and result.picture_name:
                doctor_pic['picture_path'] = result.rel_path + '/' + result.picture_name
            json_append(return_success, doctor_pic)
            return True
        else:
            return False
    else:
        return False


def dynamic_create_list(week, record_count):
    is_true = True
    count = 1
    app_list = []
    app_count = 18
    abs_week = int(math.fabs(week))
    app_count = app_count - abs_week + record_count
    while is_true:
        if count >= app_count:
            is_true = False
        app_list.append(0)
        count = count + 1
    return app_list


def dynamic_create(week, record_count):
    is_true = True
    count = 1
    app_list = []
    app_count = 18
    app_count = app_count + int(math.fabs(week)) + record_count
    while is_true:
        if count >= app_count:
            is_true = False
        app_list.append(0)
        count = count + 1
    return app_list


def add_is_compare(is_compare, due_time, baby):
    now_time = str(datetime.datetime.now()).replace('-','')[:8]
    temp_time = due_time
    temp_time = str(temp_time).replace('-','')[:8]
    if int(now_time) >= int(temp_time):
        is_compare = 45
    baby.is_compare = is_compare


def get_tracking_week(baby_id, types, show_date_way, data_type):
    tracking_count = db.query(Tracking).\
        filter(Tracking.baby_id == baby_id).\
        order_by(Tracking.measure_date).\
        group_by(Tracking.week).count()
    tracking_result = db.execute("select * from (select * from tracking where baby_id = "+str(baby_id)+" order by measure_date desc) as a group by a.week")
    tracking_count = tracking_result.rowcount
    grow_line = []
    baby = Baby.query.filter(Baby.id == baby_id).first()
    week = 0
    size = True
    if baby:
        if baby.due_date and baby.born_birthday:
            due_date = baby.due_date
            birthday = baby.born_birthday
            is_compare = ''
            s = int((birthday - due_date).total_seconds())
            week = s / 3600 / 24 / 7
            if birthday > due_date:
                if week > 10:
                    is_compare = 50
                else:
                    is_compare = 45
            elif birthday < due_date:
                is_compare = 40
                size = False
            else:
                is_compare = 45
            add_is_compare(is_compare, due_date, baby)
    result = []
    if tracking_count > 1:
        # tracking_result = Tracking.query.filter(Tracking.baby_id == baby_id).order_by(Tracking.measure_date).all()
        #tracking_result = db.query(Tracking).\
        #        filter(Tracking.baby_id == baby_id).\
        #        order_by(Tracking.measure_date).\
        #        group_by(Tracking.week).all()
        median = 18
        if data_type:
            if size:
                grow_line = dynamic_create(week, tracking_count)
            else:
                grow_line = dynamic_create_list(week, tracking_count)
        for tracking in tracking_result:
            result.append(tracking)
        for tracking in result:
            if types == 'weight':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.weight
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.weight
                    median = median + 1
                else:
                    grow_line.append(tracking.weight)
            if types == 'height':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.height
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.height
                    median = median + 1
                else:
                    grow_line.append(tracking.height)
            if types == 'head':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.head_wai
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.head_wai
                    median = median + 1
                else:
                    grow_line.append(tracking.head_wai)
        return grow_line
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.baby_id == baby_id).first()
        for tracking in tracking_result:
            result.append(tracking)
        if data_type:
            if size:
                grow_line = dynamic_create(week, tracking_count)
            else:
                grow_line = dynamic_create_list(week, tracking_count)
        if tracking:
            if types == 'weight':
                grow_line.append(result[0].weight)
            if types == 'height':
                grow_line.append(result[0].height)
            if types == 'head':
                grow_line.append(result[0].head_wai)
        return grow_line
    else:
        return grow_line


def get_tracking(baby_id, types, show_date_way, data_type):
    """
    获得随访记录_身长，体重，头围
    """
    tracking_count = db.query(Tracking).\
            filter(Tracking.baby_id == baby_id).\
            order_by(Tracking.measure_date).\
            group_by(Tracking.common).count()
    # session.query(Address.user_id, func.count('*').\
    # sums = session.query(func.sum(Irterm.n).label('a1')).group_by(Irterm.item_id)
    # average = session.query(func.avg(sums.subquery().columns.a1)).scalar()
    # label('address_count')).\    group_by(Address.user_id).subquery()
    # subresult = engine.execute("""SELECT count(*) FROM (SELECT * FROM tracking where baby_id = 29 ORDER BY measure_date DESC) as t GROUP BY t.common ORDER BY t.measure_date""")
    # sub = db.query(Tracking.label('al'))
    tracking_result = db.execute("select * from (select * from tracking where baby_id = "+str(baby_id)+" order by measure_date desc) as a group by a.common")
    grow_line = []
    baby = Baby.query.filter(Baby.id == baby_id).first()
    week = 0
    size = True
    if baby:
        if baby.due_date and baby.born_birthday:
            due_date = baby.due_date
            birthday = baby.born_birthday
            is_compare = ''
            s = int((birthday - due_date).total_seconds())
            week = s / 3600 / 24 / 7
            if birthday > due_date:
                if week > 10:
                    is_compare = 50
                else:
                    is_compare = 45
            elif birthday < due_date:
                is_compare = 40
                size = False
            else:
                is_compare = 45
            add_is_compare(is_compare, due_date, baby)
    result = []
    if tracking_count > 1:
        # tracking_result = Tracking.query.filter(Tracking.baby_id == baby_id).order_by(Tracking.measure_date).all()
        tracking_result = db.query(Tracking).\
            filter(Tracking.baby_id == baby_id).\
            order_by(Tracking.measure_date).\
            group_by(Tracking.common).all()
        median = 18
        if data_type:
            if size:
                grow_line = dynamic_create(week, tracking_count)
            else:
                grow_line = dynamic_create_list(week, tracking_count)
        for tracking in tracking_result:
            result.append(tracking)
        for tracking in result:
            if types == 'weight':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.weight
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.weight
                    median = median + 1
                else:
                    grow_line.append(tracking.weight)
            if types == 'height':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.height
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.height
                    median = median + 1
                else:
                    grow_line.append(tracking.height)
            if types == 'head':
                if data_type:
                    if median > 28:
                        pass
                    elif size:
                        grow_line[(median + int(math.fabs(week)))] = tracking.head_wai
                    else:
                        grow_line[(median - int(math.fabs(week)))] = tracking.head_wai
                    median = median + 1
                else:
                    grow_line.append(tracking.head_wai)
        return grow_line
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.baby_id == baby_id).first()
        if data_type:
            if size:
                grow_line = dynamic_create(week, tracking_count)
            else:
                grow_line = dynamic_create_list(week, tracking_count)
        for tracking in tracking_result:
            result.append(tracking)
        if tracking:
            if types == 'weight':
                grow_line.append(result[0].weight)
            if types == 'height':
                grow_line.append(result[0].height)
            if types == 'head':
                grow_line.append(result[0].head_wai)
        return grow_line
    else:
        return grow_line


def get_who_standard(id, types):
    """
    获取who标准数据
    """
    baby = Baby.query.filter(Baby.id == id).first()
    grow_p3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p15 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p75 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p95 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    is_gender = ''
    if baby:
        is_gender = baby.gender
    if types == 'weight' and is_gender == '男':
        standard = WeightBoyStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'weight' and is_gender == '女':
        standard = WeightGirlStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '女':
        standard = HeightGirlStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '男':
        standard = HeightBoyStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '女':
        standard = HeadSurroundGirlStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '男':
        standard = HeadSurroundBoyStandardWeek.query.filter()[:13]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95


def get_nine_standard(id, types):
    """
    获取who标准数据
    """
    baby = Baby.query.filter(Baby.id == id).first()
    grow_p3 = []
    grow_p15 = []
    grow_p75 = []
    grow_p95 = []
    grow_negative3 = []
    grow_negative2 = []
    grow_negative1 = []
    is_gender = ''
    if baby:
        is_gender = baby.gender
    if types == 'weight' and is_gender == '男':
        standard = NineWeightBoy.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1
    elif types == 'weight' and is_gender == '女':
        standard = NineWeightGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1
    elif types == 'height' and is_gender == '女':
        standard = NineHeightGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1
    elif types == 'height' and is_gender == '男':
        standard = NineHeightBoy.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1
    elif types == 'head' and is_gender == '女':
        standard = NineHeadGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1
    elif types == 'head' and is_gender == '男':
        standard = NineHeadBoy.query.filter().all()
        for s in standard:
            grow_negative3.append(s.negative3)
            grow_negative2.append(s.negative2)
            grow_negative1.append(s.negative1)
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1


def get_fen_tong_standard(id, types):
    """
    获取who标准数据
    """
    baby = Baby.query.filter(Baby.id == id).first()
    grow_p3 = []
    grow_p15 = []
    grow_p75 = []
    grow_p95 = []
    grow_negative3 = []
    is_gender = ''
    if baby:
        is_gender = baby.gender
    if types == 'weight' and is_gender == '男':
        standard = FenTongWeightBoy.query.filter().order_by(FenTongWeightBoy.id).all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3
    elif types == 'weight' and is_gender == '女':
        standard = FenTongWeightGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3
    elif types == 'height' and is_gender == '女':
        standard = FenTongHeightGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3
    elif types == 'height' and is_gender == '男':
        standard = FenTongHeightBoy.query.filter().all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3
    elif types == 'head' and is_gender == '女':
        standard = FenTongHeadGirl.query.filter().all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3
    elif types == 'head' and is_gender == '男':
        standard = FenTongHeadBoy.query.filter().all()
        for s in standard:
            grow_negative3.append(s.degree_ninety_seven)
            grow_p3.append(s.degree_three)
            grow_p15.append(s.degree_ten)
            grow_p75.append(s.degree_fifty)
            grow_p95.append(s.degree_ninety)
        return grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3


def get_who_standard_month(id, types):
    """
    获取who标准数据
    """
    baby = Baby.query.filter(Baby.id == id).first()
    grow_p3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p15 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p75 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    grow_p95 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    is_gender = ''
    if baby:
        is_gender = baby.gender
    if types == 'weight' and is_gender == '男':
        standard = WeightBoyStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'weight' and is_gender == '女':
        standard = WeightGirlStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '女':
        standard = HeightGirlStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '男':
        standard = HeightBoyStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '女':
        standard = HeadSurroundGirlStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '男':
        standard = HeadSurroundBoyStandardYear.query.filter()[:25]
        count = 0
        for s in standard:
            grow_p3[count] = s.P3
            grow_p15[count] = s.P15
            grow_p75[count] = s.P75
            grow_p95[count] = s.P95
            count = count + 1
        return grow_p3, grow_p15, grow_p75, grow_p95



def get_tracking_bar(id, types):
    """
    获得随访记录——配方奶
    """
    tracking_count = Tracking.query.filter(Tracking.id == id).count()
    grow_bar_breastfeeding = []
    grow_bar_formula_feeding = []
    grow_time = []
    count = 0
    if tracking_count > 1:
        tracking_result = Tracking.query.filter(Tracking.id == id).all()
        for tracking in tracking_result[:5]:
            temp_time = str(tracking.measure_date)
            grow_time.append(temp_time)
            grow_bar_breastfeeding.append(int(tracking.breast_milk_amount))
            grow_bar_formula_feeding.append(int(tracking.formula_feed_measure))
            count = count + 1
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.id == id).first()
        if tracking:
            temp_time = str(tracking.measure_date)
            grow_time.append(temp_time)
            grow_bar_breastfeeding.append(int(tracking.breast_milk_amount))
            grow_bar_formula_feeding.append(int(tracking.formula_feed_measure))
    else:
        pass
    return grow_bar_breastfeeding, grow_bar_formula_feeding, grow_time


def is_null(measure_date):
    if measure_date:
        singe_time = str(measure_date)[:10]
        singe_time = singe_time.split('-')
        result = singe_time[1]
        return int(result) - 1
    return None


def check_week(measure_date, tracking):
    '''判断是否是同一周时间'''
    dt = string_convert_to_time(measure_date)
    tracking_dt = tracking.measure_date
    dt_seconds = 1
    s = int((dt - tracking_dt).total_seconds())
    w = s / 3600 / 24 / 7
    #tracking_week = tracking_dt.isoweekday() # 得到是星期几
    #seconds = tracking_dt.microseconds # 得到秒数
    #min_time = seconds - tracking_week * 3600 * 24 # 一周开始时间
    #max_time = seconds + (7 - tracking_week) * 3600 * 24 # 一周结束时间
    #if dt_seconds >= min_time and dt_seconds <= max_time: # true：是相同一周
    #    week = tracking.week # 是同一周，week就等于tracking.week
    #else:
    #    week = int(tracking.week) + 1 # 不是同一周，就等于tracking.week 加1 周
    #return week
    if w == 0: # 同一周
        t = Tracking.query.filter(Tracking.week == tracking.week).order_by(Tracking.measure_date).first()
        tracking_dt = t.measure_date
        s = int((dt - tracking_dt).total_seconds())
        w = s / 3600 / 24 / 7
        if w == 0:
            week = t.week
        else:
            week = int(t.week) + 1
    elif w > 0: # 不是同一周
        week = int(tracking.week) + 1
    return week


def check_is_week(week, baby_id, measure_date):
    tracking_count = Tracking.query.filter(Tracking.baby_id == baby_id).count()
    if tracking_count == 0: # 如果是第一次记录那么周肯定是第一周
        week = 1
    elif tracking_count > 1: # 如果不是第一次记录，取出最近一条记录
        tracking = Tracking.query.filter(Tracking.baby_id == baby_id)[-1] # 得到最后一条
        week = check_week(measure_date, tracking)
    else:
        tracking = Tracking.query.filter(Tracking.baby_id == baby_id).first()
        week = check_week(measure_date, tracking)
    return week


def insert_visit_record(baby_id, measure_date, weight, height, head, court_id, brand_id, breastfeeding, kind, nutrition, add_type):
    """
    新增随访记录
    """
    common = 0
    week = 0
    try:
        temp = measure_date
        temp = temp.replace('-','')
        common = temp[:6]
        week = check_is_week(week, baby_id, measure_date)
    except:
        pass
    if add_type:
        tracking = Tracking(baby_id=baby_id, measure_date=measure_date, weight=weight, height=height, head_wai=head,
                            court_id=court_id, brand_id=brand_id, breast_milk_amount=breastfeeding, type_of_milk_id=kind,
                            formula_feed_measure=nutrition, add_type=add_type, common=common, week=week)
    else:
        tracking = Tracking(baby_id=baby_id, measure_date=measure_date, weight=weight, height=height, head_wai=head,
                            court_id=court_id, brand_id=brand_id, breast_milk_amount=breastfeeding, type_of_milk_id=kind,
                            formula_feed_measure=nutrition, common=common, week=week)
    try:
        db.add(tracking)
        db.commit()
    except:
        return False
    return True


def get_visit_record(baby_id):
    """
    根据baby_id获取随访记录
    """
    tracking, tracking_count = get_tracking_model(Tracking, baby_id)
    baby = Baby.query.filter(Baby.id == baby_id).first()
    if baby:
        if baby.due_date and baby.born_birthday:
            due_date = baby.due_date
            birthday = baby.born_birthday
            is_compare = ''
            s = int((birthday - due_date).total_seconds())
            week = s / 3600 / 24 / 7
            if birthday > due_date:
                if week > 10:
                    is_compare = 50
                else:
                    is_compare = 45
            elif birthday < due_date:
                is_compare = 40
            else:
                is_compare = 45
            add_is_compare(is_compare, due_date, baby)
    time_birthday_week(baby)
    baby_nutrition_feeding_energy = 0
    baby_nutrition_feeding_protein = 0
    milk = [0,0,0,0,0]
    milk_date = ['','','','','']
    baby.milk = []
    if tracking != 0:
        if type(tracking) is list:
            count = 0
            for t in tracking:
                if count < 5:
                    milk[count] = t.breast_milk_amount
                    if t.measure_date:
                        temp_milk = str(t.measure_date)[2:10]
                    milk_date[count] = temp_milk
                count = count + 1
                kind = get_kind_by_id(t.type_of_milk_id)
                if kind and kind.energy and kind.protein:
                    baby_nutrition_feeding_energy = baby_nutrition_feeding_energy + int(kind.energy)
                    baby_nutrition_feeding_protein = baby_nutrition_feeding_protein + int(kind.protein)
                t.birthday_time = time_birthday_time_compare(t.measure_date, baby)
                t.measure_date = str(t.measure_date)[:10]
            baby.milk = milk
            baby.milk_date = milk_date
        else:
            tracking.birthday_time = time_birthday_time_compare(tracking.measure_date, baby)
            tracking.measure_date = str(tracking.measure_date)[:10]
            milk[0] = tracking.breast_milk_amount
            if tracking.measure_date:
                temp_milk = str(tracking.measure_date)[2:10]
            milk_date[0] = temp_milk
            kind = get_kind_by_id(tracking.type_of_milk_id)
            if kind and kind.energy and kind.protein:
                baby_nutrition_feeding_energy = baby_nutrition_feeding_energy + int(kind.energy)
                baby_nutrition_feeding_protein = baby_nutrition_feeding_protein + int(kind.protein)
            baby.milk = milk
            baby.milk_date = milk_date
        if baby:
            baby.energy = baby_nutrition_feeding_energy
            baby.protein = baby_nutrition_feeding_protein
            get_picture_by_id(baby.id, baby)
        return tracking, tracking_count, baby
    else:
        if baby:
            baby.energy = baby_nutrition_feeding_energy
            baby.protein = baby_nutrition_feeding_protein
            baby.milk = milk
            baby.milk_date = milk_date
            get_picture_by_id(baby.id, baby)
            return 0,0, baby
        else:
            return 0,0,0


def check_baby_birthday(baby):
    """
    检查baby是否是早产儿
    """
    due_date = baby.due_date


def check_baby_is_week_or_month(baby):
    """
    根据baby的生日来判断显示周，还是月数据
    """
    days = 13 * 7
    if baby:
        baby_birthday = baby.born_birthday
        now_date = datetime.datetime.now()
        difference_date = (now_date - baby_birthday).days
        if difference_date <= days:
            return 'week'
        else:
            return 'month'


def get_analysis_data(id):
    """
    获取喂养量分析
    """
    analysis_data = Tracking.query.filter(Tracking.id == id).first()
    baby = Baby.query.filter(Baby.id == analysis_data.baby_id).first()
    if analysis_data.measure_date:
        analysis_data.measure_date = str(analysis_data.measure_date)[2:10]
    if analysis_data:
        if baby:
            analysis_data.baby_name = baby.baby_name
        return analysis_data
    else:
        return None



def time_birthday_time_compare(dt, baby):
    if dt:
        dt = datetime.datetime.strptime(str(dt), "%Y-%m-%d %H:%M:%S")
        # today = datetime.datetime.today()
        if baby.born_birthday:
            birthday = baby.born_birthday
            s = int((dt - birthday).total_seconds())
            result = 0
            # day_diff > 365, use year
            if math.fabs(s / 3600 / 24) >= 365:
                result = s / 3600 / 24 / 365
                return str(s / 3600 / 24 / 365) + " 年"
            elif math.fabs(s / 3600 / 24) >= 30:  # day_diff > 30, use month
                result = s / 3600 / 24 / 30
                return str(s / 3600 / 24 / 30) + " 个月"
            elif math.fabs(s / 3600 / 24 / 7) >= 7:  # day_diff > 7, use week
                result = math.fabs(s / 3600 / 24 / 7)
                if result == 0:
                    return "1周"
                return str(s / 3600 / 24 / 7) + "周"
            else:  # hour_diff > 24, use day
                return str(s / 3600 / 24) + " 天"

    return ""


def time_birthday_week(baby):
    if baby.born_birthday:
        dt = datetime.datetime.strptime(str(baby.born_birthday), "%Y-%m-%d %H:%M:%S")
        today = datetime.datetime.today()
        s = int((today - dt).total_seconds())

        # day_diff > 365, use year
        if s / 3600 / 24 >= 365:
            baby.birthday =  str(s / 3600 / 24 / 365) + " 年"
        elif s / 3600 / 24 >= 30:  # day_diff > 30, use month
            baby.birthday =  str(s / 3600 / 24 / 30) + " 个月"
        elif s / 3600 / 24 >= 7:  # day_diff > 7, use week
            baby.birthday = str(s / 3600 / 24 / 7) + "周"
        elif s / 3600 >= 24:  # hour_diff > 24, use day
            baby.birthday = str(s / 3600 / 24) + " 天"
        elif s / 60 > 60:  # minite_diff > 60, use hour
            baby.birthday = str(s / 3600) + " 小时"
        elif s > 60:  # second_diff > 60, use minite
            baby.birthday = str(s / 60) + " 分钟"
        else:  # use "just now"
            baby.birthday = ''


def get_baby_by_id(baby_id):
    """
    获得baby
    """
    baby = Baby.query.filter(Baby.id == baby_id).first()
    get_picture_by_id(baby.id, baby)
    if baby.id <= 9 and baby.id >= 1:
        baby.id = '1000' + str(baby.id)
    if baby.id <= 99 and baby.id >= 10:
        baby.id = '100' + str(baby.id)
    if baby.id <= 999 and baby.id >= 100:
        baby.id = '10' + str(baby.id)
    if baby.id <= 9999 and baby.id >= 1000:
        baby.id = '1' + str(baby.id)
#    childbirth = ChildbirthStyle.query.filter(ChildbirthStyle.id == baby.childbirth_style_id).first()
    #complication = Complication.query.filter(Complication.id == baby.complication_id).first()
    #baby.complication = complication.name
    #baby.childbirth_style = childbirth.name
    if baby.due_date:
        baby.due_date = str(baby.due_date)[:10]
    return baby


def get_tracking_test(id, types, show_date_way):
    """
    获得随访记录_身长，体重，头围
    """
    tracking_count = Tracking.query.filter(Tracking.baby_id == id).count()
    grow_line = []
    if tracking_count > 1:
        tracking_result = Tracking.query.filter(Tracking.baby_id == id).all()
        result = 0
        count = 1
        weight = 0
        height = 0
        head = 0
        temp_date = 0
        for tracking in tracking_result:
            temp_date = str(tracking.measure_date)[5:7]
            
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.baby_id == id).first()
        if tracking:
            if types == 'weight':
                grow_line.append(int(tracking.weight))
            if types == 'height':
                grow_line.append(int(tracking.height))
            if types == 'head':
                grow_line.append(int(tracking.head_wai))
        return 0
    else:
        return 0


def get_record_time_and_rate(baby_id):
    tracking_count = Tracking.query.filter(Tracking.baby_id == baby_id).count()
    baby = Baby.query.filter(Baby.id == baby_id).first()
    grow_time = []
    grow_rate = []
    if baby.due_date and baby.born_birthday:
        due_date = baby.due_date
        birthday = baby.born_birthday
        s = int((birthday - due_date).total_seconds())
        week = s / 3600 / 24 / 7 # 得到早产多少周
        count = 1
        if tracking_count > 1:
            tracking = Tracking.query.filter(Tracking.baby_id == baby_id).order_by(Tracking.measure_date).all()
            for t in tracking:
                get_energy_protein(baby, t)
                get_rate(grow_time, grow_rate, t, baby, week, count)
                count = count + 1 # 多次记录
        else:
            tracking = Tracking.query.filter(Tracking.baby_id == baby_id).first()
            if tracking:
                get_energy_protein(baby, tracking)
                get_rate(grow_time, grow_rate, tracking, baby, week, count)
    else:
        pass
    return grow_time, grow_rate, baby


def get_rate(grow_time, grow_rate, t, baby, week, count):
    temp_time = str(t.measure_date)[2:10] # 得到添加随访记录时间,进行截取
    grow_time.append(temp_time)
    birthday = baby.born_birthday
    age_s = int((birthday - t.measure_date).total_seconds())
    actual_age = age_s / 3600 / 24 / 7 # 得到实际年龄
    #if math.fabs(actual_age) < math.fabs(week):
    #    baby.s = '您的宝宝还没有足月'
    #redress_age = math.fabs(actual_age) - math.fabs(week) # 得到矫正年龄
    rate = 0
    try:
        rate = (t.weight * count) / (math.fabs(actual_age) * count) # 得到速率,x * n / t * n(x体重，n记录次数,t矫正年龄)
    except:
        pass
    grow_rate.append(float('%0.2f'%rate))


def get_energy_protein(baby, tracking):
    kind = TypeOfMilk.query.filter(TypeOfMilk.id == tracking.type_of_milk_id).first()
    energy = 0
    protein = 0
    if kind and kind.energy and kind.protein:
        energy = energy + float(kind.energy)
        protein = protein + float(kind.protein)
    baby.energy = energy
    baby.protein = protein


#def entering_who():
#    """
#       录入who标准数据
#    """
#    read_file = open('/Users/K/Documents/User Data/baby Data/fentong_height_girl.txt')
#    result = {}
#    count = 0
#    for line in read_file:
#        ''''''
#        result[str(count)] = []
#        result[str(count)].append(line.replace('\n','').replace('\r','').split('\t'))
#        count = count + 1
#    count = 0
#    length = result.__len__() - 1
#    # result.pop('0')
#    for keys in result.keys():
#        #print result[str(count)][0].__len__()
#        weight_boy_standard = FenTongHeightGirl(week=result[str(count)][0][0], degree_three=result[str(count)][0][1],
#                                                degree_ten=result[str(count)][0][2], degree_fifty=result[str(count)][0][3],
#                                                degree_ninety=result[str(count)][0][4], degree_ninety_seven=result[str(count)][0][5])
#        db.add(weight_boy_standard)
#        db.commit()
#        count = count + 1
