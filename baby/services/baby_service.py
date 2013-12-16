# coding: UTF-8

from ..models.baby_model import Baby, BabyPicture, ChildbirthStyle, Complication
from ..models import db
from ..models.feature_model import Collect, SearchHistory, SystemMessage
from ..util.seesion_query import *
from ..util.others import page_utils, flatten, time_diff, set_session_user
from ..models.feature_model import Collect
from werkzeug import secure_filename
from baby.setting.server import *
from baby.util.ex_file import *
import os


def format_baby(baby, resp_suc):
    """
        格式化baby对象
    """
    if baby:
        baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == baby.id).first()
        #childbirth_style = ChildbirthStyle.query.filter(ChildbirthStyle.id == baby.complication_id).first()
        #complication_id_list = baby.complication_id.split(',')
        baby_pic = flatten(baby)
        #get_complication(complication_id_list, baby_pic)
        if baby.born_birthday:
            baby_birthday = baby.born_birthday
            baby_pic['time'] = time_diff(baby_birthday)
        if baby_picture:
            if baby_picture.rel_path and baby_picture.picture_name:
                baby_pic['picture_path'] = baby_picture.rel_path + '/' + baby_picture.picture_name
        else:
            baby_pic['picture_path'] = ""
        #if childbirth_style:
        #    baby_pic['childbirth'] = childbirth_style.name
        resp_suc['baby_list'].append(baby_pic)


def get_complication(complication_list, baby_pic):
    """
       根据baby.complication_id
       得到合并症
    """
    complication_count = Complication.query.filter(Complication.id.in_(complication_list)).count()
    if complication_count > 1:
        complications = Complication.query.filter(Complication.id.in_(complication_list)).all()
        baby_pic['complication'] = ''
        for complication in complications:
            baby_pic['complication'] = baby_pic['complication'] + ',' + complication.name
    else:
        complication = Complication.query.filter(Complication.id.in_(complication_list)).first()
        if complication:
            baby_pic['complication'] = complication.name


def baby_list(page, doctor_id):
    """
        全部婴儿列表
    """
    set_session_user('', '', 'user_id', doctor_id)
    baby_count = Baby.query.filter().count()
    temp_page = page
    page, per_page = page_utils(baby_count, page)
    baby_collect_count = Collect.query.filter(Collect.doctor_id == doctor_id).count()
    if baby_count > 1:
        babys = Baby.query.filter().order_by(Baby.system_message_time.desc()).all()[per_page*(int(temp_page)-1):per_page*int(temp_page)]
        baby_collect_count = Collect.query.filter(Collect.doctor_id == doctor_id).count()
        if baby_collect_count > 1:
            baby_collects = Collect.query.filter(Collect.doctor_id == doctor_id).all()
            for baby in babys:
                for baby_collect in baby_collects:
                    if baby.id == baby_collect.type_id:
                        baby.is_collect = 0
                    else:
                        baby.is_collect = 1
        else:
            baby_collect = Collect.query.filter(Collect.doctor_id == doctor_id).first()
            if baby_collect:
                 for baby in babys:
                    if baby.id == baby_collect.type_id:
                        baby.is_collect = 0
                    else:
                        baby.is_collect = 1
            else:
                for baby in babys:
                    baby.is_collect = 1
        return babys
    else:
        baby = Baby.query.filter().first()
        if baby_collect_count > 1:
            baby_collects = Collect.query.filter(Collect.doctor_id == doctor_id).all()
            for baby_collect in baby_collects:
                if baby.id == baby_collect.type_id:
                    baby.is_collect = 0
                else:
                    baby.is_collect = 1
        else:
            baby_collect = Collect.query.filter(Collect.doctor_id == doctor_id).first()
            if baby_collect:
                if baby.id == baby_collect.type_id:
                    baby.is_collect = 0
                else:
                    baby.is_collect = 1
            else:
                baby.is_collect = 1
        return baby


def baby_collect_list(page, doctor_id, success):
    """
        得到医生收藏婴儿列表
            page: 分页，当前页
            doctor_id: 医生的id
    """
    collect_count = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').count()
    temp_page = page
    page, per_page = page_utils(collect_count, page)
    if collect_count > 1:
        collect_result = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'baby')[per_page*(int(temp_page)-1):per_page*int(temp_page)]
        if collect_result:
            for collect in collect_result:
                baby = Baby.query.filter(Baby.id == collect.type_id).first()
                baby.is_collect = 0
                format_baby(baby, success)
            return True
        else:
            return False
    else:
        collect = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').first()
        if collect:
            baby = Baby.query.filter(Baby.id == collect.type_id).first()
            baby.is_collect = 0
            format_baby(baby, success)
            return True
        else:
            return False
    #result_count = db.query(Baby). \
    #    filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').count()
    #temp_page = page
    #page, per_page = page_utils(result_count, page)
    #if result_count > 1:
    #    results = db.query(Baby).\
    #        filter(Collect.doctor_id == doctor_id, Collect.type == 'baby')[per_page*(int(temp_page)-1):per_page*int(temp_page)]
    #    for result in results:
    #        get_picture_by_id(result.id, result)
    #        result.is_collect = 0
    #    return results
    #else:
    #    result = db.query(Baby).\
    #        filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').first()
    #    get_picture_by_id(result.id, result)
    #    result.is_collect = 0
    #    return result


def search_by_keyword_time(keyword, time):
    """
        根据关键字或者时间来搜索
        关键字时间一起搜索
    """
    if keyword:
        baby = Baby.query.filter(Baby.baby_name.like('%' + keyword + '%')).first()
        search_history = SearchHistory(keyword=keyword)
        db.add(search_history)
        db.commit()
        return baby
    #if time:
    #    baby = Baby.quer.filter().first()
    #    return baby


def is_null(obj):
    '''判断是否为空'''
    if obj:
        if obj.rel_path and obj.picture_name:
            return True
    else:
        return False


def get_picture_by_id(baby_id, baby):
    '''通过baby_id来得到图片'''
    baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == baby_id).first()
    bool = is_null(baby_picture)
    if bool:
        baby.picture_path = baby_picture.rel_path + '/' + baby_picture.picture_name


def get_baby_info(baby_id, success):
    """
        得到婴儿信息
            baby_id：婴儿登录id
    """
    baby = Baby.query.filter(Baby.id == baby_id).first()
    format_baby(baby, success)
    return baby


def get_parenting_guide(baby_id):
    """
        得到育儿指南
            baby_id: 婴儿登录id
    """
    baby = Baby.query.filter(Baby.id == baby_id).first()
    if baby:
        system_message_count = SystemMessage.query.filter(SystemMessage.type == 'guide').count()
        if system_message_count > 1:
            system_messages = SystemMessage.query.filter(SystemMessage.type == 'guide')[:3]
            return system_messages
        else:
            system_message = SystemMessage.query.filter(SystemMessage.type == 'guide').first()
            return system_message


def update_baby(baby_id, patriarch_tel, baby_name, due_date, gender, born_weight, born_height, born_head, childbirth_style_id,
                complication_id, apagar_score, upload_image, success):
    '''修改婴儿资料'''
    baby = Baby.query.filter(Baby.id == baby_id).first()
    if baby:
        if patriarch_tel:
            baby.patriarch_tel = patriarch_tel
        if baby_name:
            baby.baby_name = baby_name
        if due_date:
            baby.due_date = due_date
        if gender:
            baby.gender = gender
        if born_weight:
            baby.born_weight = born_weight
        if born_height:
            baby.born_height = born_height
        if born_head:
            baby.born_head = born_head
        if childbirth_style_id:
            baby.childbirth_style_id = childbirth_style_id
        if complication_id:
            baby.complication_id = complication_id
        if apagar_score:
            baby.apgar_score = apagar_score
        if upload_image:
            if not allowed_file_extension(upload_image.stream.filename, HEAD_PICTURE_ALLOWED_EXTENSION):
                return False
            baby_picture = BabyPicture.query.filter(BabyPicture.baby_id == baby.id).first()
            old_picture = ''
            base_path = HEAD_PICTURE_BASE_PATH
            if baby_picture:
                if baby_picture:
                    old_picture = base_path + str(baby_picture.rel_path) + '/' + str(baby_picture.picture_name)
                baby_picture.rel_path = HEAD_PICTURE_UPLOAD_FOLDER
                baby_picture.picture_name = time_file_name(secure_filename(upload_image.stream.filename), sign=baby.id)
                upload_image.save(os.path.join(base_path + baby_picture.rel_path+'/', baby_picture.picture_name))
            else:
                picture_name = time_file_name(secure_filename(upload_image.stream.filename), sign=baby.id)
                baby_picture = BabyPicture(baby_id=baby_id, base_path=base_path, rel_path='/static/img/system/head_picture', picture_name=picture_name)
                try:
                    db.add(baby_picture)
                    db.commit()
                except:
                    pass
                upload_image.save(os.path.join(base_path + baby_picture.rel_path+'/', picture_name))
            try:
                os.remove(old_picture)
            except:
                pass
        format_baby(baby, success)
        db.commit()
        return True
    else:
        return False


def create_baby(patriarch_tel, baby_name, baby_pass, gender, due_date, born_birthday, born_weight, born_height, born_head, childbirth_style_id,
                complication_id):
    baby = Baby.query.filter(Baby.patriarch_tel == patriarch_tel).first()
    if baby:
        return 1
    else:
        baby = Baby(patriarch_tel=patriarch_tel, baby_name=baby_name, baby_pass=baby_pass, gender=gender, due_date=due_date, born_birthday=born_birthday, born_weight=born_weight,
                    born_height=born_height, born_head=born_head, childbirth_style=childbirth_style_id, complication=complication_id)
        try:
            db.add(baby)
            db.commit()
        except:
            return 0
        return baby.id