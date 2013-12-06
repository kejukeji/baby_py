# coding: UTF-8

from baby.models.feature_model import AcademicAbstract
from baby.util.others import page_utils, flatten


def get_academic_abstract(page, success):
    """
    获取文摘
    """
    success['academic_list'] = []
    academic_count = AcademicAbstract.query.filter().count()
    temp_page = page
    page, per_page = page_utils(academic_count, page, per_page=3)
    if academic_count > 1:
        academic_result = AcademicAbstract.query.filter().all()[per_page * (temp_page - 1): per_page * page]
        if academic_result:
            for academic in academic_result:
                academic_pic = flatten(academic)
                success['academic_list'].append(academic_pic)
            return True
        else:
            return False
    else:
        academic = AcademicAbstract.query.filter().first()
        if academic:
            academic_pic = flatten(academic)
            success['academic_list'].append(academic_pic)
            return True
        else:
            return False


def get_abstract_by_id(id, success):
    """
    根据id获取文摘
    """
    abstract = AcademicAbstract.query.filter(AcademicAbstract.id == id).first()
    if abstract:
        abstract_pic = flatten(abstract)
        success['abstract'] = abstract_pic
        return True
    else:
        return False