# coding: UTF-8

from baby.models.baby_model import Baby, BabyPicture
from baby.models.hospital_model import Doctor, Province, Hospital, Department, Position
from baby.util.others import set_session_user, time_diff, flatten
from baby.models.feature_model import Tracking
from baby.models.database import db


def check_login(login_name, login_pass):
    """
       login_name: 登陆名
       login_pass: 登陆密码
    """
    baby = Baby.query.filter(Baby.login_name == login_name, Baby.baby_pass == login_pass).first()
    doctor = Doctor.query.filter(Doctor.doctor_name == login_name, Doctor.doctor_pass == login_pass).first()
    if baby != None or doctor != None:
        if baby != None:
            set_session_user(baby.login_name, baby.id)
            return baby
        if doctor != None:
            set_session_user(doctor.doctor_name, doctor.id)
            return doctor
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
    baby = Baby.query.filter(Baby.id == user_id).first()
    if baby:
        if baby.baby_pass == old_password:
            baby.baby_pass = new_password
            return True
        else:
            return False
    doctor = Doctor.query.filter(Doctor.id == user_id).first()
    if doctor:
        if doctor.doctor_pass == old_password:
            doctor.doctor_pass = new_password
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
            doctor_pic['user_id'] = result.id
            if result.rel_path and result.picture_name:
                doctor_pic['picture_path'] = result.rel_path + '/' + result.picture_name
            json_append(return_success, doctor_pic)
            return True
        else:
            return False
    else:
        return False


def get_tracking(id):
    """
    获得随访记录
    """
    tracking_count = Tracking.query.filter(Tracking.baby_id == id).count()
    weight = [0,0,0,0,0,0,0,0,0,0,0,0]
    if tracking_count > 1:
        tracking_result = Tracking.query.filter(Tracking.baby_id == id).all()
        for tracking in tracking_result:
            result = is_null(tracking.measure_date)
            weight[result] = (int(tracking.weight))
        return weight
    elif tracking_count == 1:
        tracking = Tracking.query.filter(Tracking.baby_id == id).first()
        if tracking:
            result = is_null(tracking.measure_date)
            weight[result] = (int(tracking.weight))
        return weight


def is_null(measure_date):
    if measure_date:
        singe_time = str(measure_date)[:10]
        singe_time = singe_time.split('-')
        result = singe_time[1]
        return int(result) - 1


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



#def entering_who():
#    """
#       录入who标准数据
#    """
#    read_file = open('/Users/K/Documents/User Data/baby Data/lhfa_girls_p_exp.txt')
#    result = {}
#    count = 0
#    for line in read_file:
#        ''''''
#        result[str(count)] = []
#        result[str(count)].append(line.replace('\n','').replace('\r','').split('\t'))
#        count = count + 1
#    count = 1
#    length = result.__len__() - 1
#    result.pop('0')
#    for keys in result.keys():
#        #print result[str(count)][0].__len__()
#        weight_boy_standard = HeadSurroundGirlStandard(age=result[str(count)][0][0], L=result[str(count)][0][1],
#                                                M=result[str(count)][0][2], S=result[str(count)][0][3],
#                                                P01=result[str(count)][0][4], P1=result[str(count)][0][5],
#                                                P3=result[str(count)][0][6], P5=result[str(count)][0][7],
#                                                P10=result[str(count)][0][8], P15=result[str(count)][0][9],
#                                                P25=result[str(count)][0][10], P50=result[str(count)][0][11],
#                                                P75=result[str(count)][0][12], P85=result[str(count)][0][13],
#                                                P90=result[str(count)][0][14], P95=result[str(count)][0][15],
#                                                P97=result[str(count)][0][16], P99=result[str(count)][0][17],
#                                                P999=result[str(count)][0][18])
#        db.add(weight_boy_standard)
#        db.commit()
#        count = count + 1