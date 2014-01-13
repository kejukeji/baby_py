# coding: UTF-8

from baby.models.feature_model import AcademicAbstract, Collect
from baby.util.others import page_utils, flatten


def get_academic_abstract(page, doctor_id, success):
    """
    获取文摘
    """
    success['academic_list'] = []
    academic_count = AcademicAbstract.query.filter().count()
    temp_page = page
    page, per_page = page_utils(academic_count, page, per_page=3)
    collect_count = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').count()
    if academic_count > 1:
        if collect_count > 1:
            collects = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').all()
            academic_result = AcademicAbstract.query.filter().all()[per_page * (temp_page - 1): per_page * page]
            if academic_result:
                check_abstract_list(academic_result, collects, success)
                return True
            else:
                return False
        else:
            collects = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').first()
            academic_result = AcademicAbstract.query.filter().all()[per_page * (temp_page - 1): per_page * page]
            if academic_result:
                check_abstract_list(academic_result, collects, success)
                return True
            else:
                return False
    else:
        if collect_count > 1:
            collects = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').all()
            academic_result = AcademicAbstract.query.filter().first()
            if academic_result:
                check_abstract_list(academic_result, collects, success)
                return True
            else:
                return False
        else:
            collects = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').first()
            academic_result = AcademicAbstract.query.filter().first()
            if academic_result:
                check_abstract_list(academic_result, collects, success)
                return True
            else:
                return False


def collect_abstract(academic_result, success):
    '''序列化json对象'''
    academic_pic = flatten(academic_result)
    success['academic_list'].append(academic_pic)


def check_abstract_list(abstract, collect, success):
    if type(abstract) is list:
        abstract_is_list(abstract, collect, success)
    else:
        abstract_is_object(abstract, collect, success)


def abstract_is_list(abstract, collect, success):
    if type(collect) is list:
        for p in abstract:
            for c in collect:
                if p.id == c.type_id:
                    p.is_collect = True
                    break
                else:
                    p.is_collect = False
            collect_abstract(p, success)
    elif type(collect) is Collect:
        for p in abstract:
            if p.id == collect.type_id:
                p.is_collect = True
            else:
                p.is_collect = False
            collect_abstract(p, success)
    else:
        for p in abstract:
            p.is_collect = False
            collect_abstract(p, success)


def abstract_is_object(abstract, collect, success):
    if type(collect) is list:
        for c in collect:
            if abstract.id == c.type_id:
                abstract.is_collect = True
                break
            else:
                abstract.is_collect = False
        collect_abstract(abstract, success)
    elif type(collect) is Collect:
        if abstract.id == collect.type_id:
            abstract.is_collect = True
        else:
            abstract.is_collect = False
        collect_abstract(abstract, success)
    else:
        abstract.is_collect = False
        collect_abstract(abstract, success)


def get_abstract_by_id(id, doctor_id, success):
    """
    根据id获取文摘
    """
    abstract = AcademicAbstract.query.filter(AcademicAbstract.id == id).first()
    collect_result = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type_id == abstract.id).first()
    if abstract:
        if collect_result:
            abstract.is_collect = True
        else:
            abstract.is_collect = False
        abstract_pic = flatten(abstract)
        success['abstract'] = abstract_pic
        return True
    else:
        return False


def get_collect_abstract(doctor_id, page, success):
    """
    获取医生收藏文摘
    """
    success['academic'] = []
    abstract = AcademicAbstract.query.filter().all()
    collect_count = Collect.query.filter(Collect.doctor_id == doctor_id).count()
    temp_page = page
    page, per_page = page_utils(collect_count, page, per_page=3)
    if collect_count > 1:
        collect_result = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract')[per_page * (temp_page - 1): per_page * page]
        if collect_result:
            for collect in collect_result:
                for a in abstract:
                    if a.id == collect.type_id:
                        a.is_collect = True
                        a_pic = flatten(a)
                        success['academic'].append(a_pic)
            return True
        else:
            return False
    else:
        collect = Collect.query.filter(Collect.doctor_id == doctor_id, Collect.type == 'abstract').first()
        if collect:
            for a in abstract:
                if a.id == collect.type_id:
                    a.is_collect = True
                    a_pic = flatten(a)
                    success['academic'].append(a_pic)
            return True
        else:
            return False
