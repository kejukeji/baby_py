# coding: UTF-8

from baby.models.baby_model import Baby, BabyPicture
from baby.models.hospital_model import Doctor, Province, Hospital, Department, Position
from baby.util.others import set_session_user, time_diff, flatten, get_session, page_utils
from baby.models.feature_model import Tracking
from baby.models.baby_model import Complication, ChildbirthStyle
from baby.models.database import db
from .tracking_service import get_tracking_model
from .baby_service import get_picture_by_id
from .formula import *
from baby.models.standard import *
from baby.models.nine_standard import *
import datetime


def check_login(login_name, login_pass, login_type):
    """
       login_name: 登陆名
       login_pass: 登陆密码
    """
    if login_type == 'mummy':
        baby = Baby.query.filter(Baby.patriarch_tel == login_name, Baby.baby_pass == login_pass).first()
        if baby != None:
            set_session_user('user', baby.login_name, 'user_id', baby.id)
            return baby
        else:
            return None
    if login_type == 'doctor':
        doctor = Doctor.query.filter(Doctor.doctor_name == login_name, Doctor.doctor_pass == login_pass).first()
        if doctor != None:
            set_session_user('user', doctor.doctor_name, 'user_id', doctor.id)
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


def by_id_alter_password(user_id, old_password, new_password):
    """
       通过user_id来获取信息
          判断old_password是否正确
             修改密码
    """
    entrance = get_session('entrance')
    if entrance == 'baby':
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
    elif entrance is None or entrance == 'doctor':
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


def get_tracking(id, types, show_date_way):
    """
    获得随访记录_身长，体重，头围
    """
    tracking_count = Tracking.query.filter(Tracking.baby_id == id).count()
    grow_line = []
    if tracking_count > 1:
        tracking_result = Tracking.query.filter(Tracking.baby_id == id).order_by(Tracking.measure_date).all()
        result = 0
        for tracking in tracking_result:
            if types == 'weight':
                grow_line.append(tracking.weight)
            if types == 'height':
                grow_line.append(tracking.height)
            if types == 'head':
                grow_line.append(tracking.head_wai)
        return grow_line
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.baby_id == id).first()
        if tracking:
            if types == 'weight':
                grow_line.append(tracking.weight)
            if types == 'height':
                grow_line.append(tracking.height)
            if types == 'head':
                grow_line.append(tracking.head_wai)
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
    is_gender = ''
    if baby:
        is_gender = baby.gender
    if types == 'weight' and is_gender == '男':
        standard = NineWeightBoy.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'weight' and is_gender == '女':
        standard = NineWeightGirl.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '女':
        standard = NineHeightGirl.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'height' and is_gender == '男':
        standard = NineHeightBoy.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '女':
        standard = NineHeadGirl.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95
    elif types == 'head' and is_gender == '男':
        standard = NineHeadBoy.query.filter().all()
        for s in standard:
            grow_p3.append(s.zero)
            grow_p15.append(s.positive1)
            grow_p75.append(s.positive2)
            grow_p95.append(s.positive3)
        return grow_p3, grow_p15, grow_p75, grow_p95


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
    count = 0
    if tracking_count > 1:
        tracking_result = Tracking.query.filter(Tracking.id == id).all()
        for tracking in tracking_result[:5]:
            grow_bar_breastfeeding.append(int(tracking.breast_milk_amount))
            grow_bar_formula_feeding.append(int(tracking.formula_feed_measure))
            count = count + 1
        return grow_bar_breastfeeding, grow_bar_formula_feeding
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.id == id).first()
        if tracking:
            grow_bar_breastfeeding.append(int(tracking.breast_milk_amount))
            grow_bar_formula_feeding.append(int(tracking.formula_feed_measure))
        return grow_bar_breastfeeding, grow_bar_formula_feeding
    else:
        return grow_bar_breastfeeding, grow_bar_formula_feeding


def is_null(measure_date):
    if measure_date:
        singe_time = str(measure_date)[:10]
        singe_time = singe_time.split('-')
        result = singe_time[1]
        return int(result) - 1
    return None


def insert_visit_record(baby_id, measure_date, weight, height, head, court_id, brand_id, breastfeeding, kind, nutrition):
    """
    新增随访记录
    """
    tracking = Tracking(baby_id=baby_id, measure_date=measure_date, weight=weight, height=height, head_wai=head,
                        court_id=court_id, brand_id=brand_id, breast_milk_amount=breastfeeding, type_of_milk_id=kind,
                        formula_feed_measure=nutrition)

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
                if kind:
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
            if kind:
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
            if s / 3600 / 24 >= 365:
                result = s / 3600 / 24 / 365
                return str(s / 3600 / 24 / 365) + " 年"
            elif s / 3600 / 24 >= 30:  # day_diff > 30, use month
                result = s / 3600 / 24 / 30
                return str(s / 3600 / 24 / 30) + " 个月"
            elif s / 3600 / 24 / 7 <= 7:  # day_diff > 7, use week
                result = s / 3600 / 24 / 7
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

#def entering_who():
#    """
#       录入who标准数据
#    """
#    read_file = open('/Users/K/Documents/User Data/baby Data/NINE_head_girl.txt')
#    result = {}
#    count = 0
#    for line in read_file:
#        ''''''
#        result[str(count)] = []
#        result[str(count)].append(line.replace('\n','').replace('\r','').split('    '))
#        count = count + 1
#    count = 0
#    length = result.__len__() - 1
#    # result.pop('0')
#    for keys in result.keys():
#        #print result[str(count)][0].__len__()
#        weight_boy_standard = NineHeadGirl(month=result[str(count)][0][0], negative3=result[str(count)][0][1],
#                                                negative2=result[str(count)][0][2], negative1=result[str(count)][0][3],
#                                                zero=result[str(count)][0][4], positive1=result[str(count)][0][5],
#                                                positive2=result[str(count)][0][6], positive3=result[str(count)][0][7])
#        db.add(weight_boy_standard)
#        db.commit()
#        count = count + 1
