# coding: UTF-8


from baby.models.feature_model import Court, Brand, TypeOfMilk
from baby.util.others import flatten


def get_court():
    """
    获取院内，院外
    """
    court_count = Court.query.filter().count()
    if court_count > 1:
        court = Court.query.filter().all()
        return court, court_count
    elif court_count == 1:
        court = Court.query.filter().first()
        return court, court_count


def get_brand_in():
    """
    获得院内品牌
    """
    brand_count = Brand.query.filter(Brand.court_id == 1).count()
    if brand_count > 1:
        brand = Brand.query.filter(Brand.court_id == 1).all()
        return brand, brand_count
    elif brand_count == 1:
        brand = Brand.query.filter(Brand.court_id == 1).first()
        return brand, brand_count


def get_brand_out():
    """
    获取院外品牌
    """
    brand_count = Brand.query.filter(Brand.court_id == 2).count()
    if brand_count > 1:
        brand = Brand.query.filter(Brand.court_id == 2).all()
        return brand, brand_count
    elif brand_count == 1:
        brand = Brand.query.filter(Brand.court_id == 2).first()
        return brand, brand_count


def get_brand():
    """
    获得品牌
    """
    brand_count = Brand.query.filter().count()
    if brand_count > 1:
        brand = Brand.query.filter().all()
        return brand, brand_count
    elif brand_count == 1:
        brand = Brand.query.filter().first()
        return brand, brand_count


def get_kind():
    """
    获取种类
    """
    kind_count = TypeOfMilk.query.filter().count()
    if kind_count > 1:
        kind = TypeOfMilk.query.filter().all()
        return kind, kind_count
    else:
        kind = TypeOfMilk.query.filter().first()
        if kind:
            return kind, kind_count
        else:
            return 0,0


def change_to_flatten(model):
    """

    """
    if model:
        model_pic = flatten(model)
        return model_pic
    else:
        return ""


def is_list_court():
    court, court_count = get_court()
    store_list = []
    if court_count > 1:
        for c in court:
            court_pic = change_to_flatten(c)
            store_list.append(court_pic)
        return store_list
    elif court_count == 1:
        court_pic = change_to_flatten(court)
        store_list.append(court_pic)
        return store_list


def is_list_brand():
    court, court_count = get_brand()
    store_list = []
    if court_count > 1:
        for c in court:
            court_pic = change_to_flatten(c)
            store_list.append(court_pic)
        return store_list
    elif court_count == 1:
        court_pic = change_to_flatten(court)
        store_list.append(court_pic)
        return store_list


def is_list_kind():
    court, court_count = get_kind()
    store_list = []
    if court_count > 1:
        for c in court:
            court_pic = change_to_flatten(c)
            store_list.append(court_pic)
        return store_list
    elif court_count == 1:
        court_pic = change_to_flatten(court)
        store_list.append(court_pic)
        return store_list


def div_data(success):
    """
    层级显示
    """
    court_list, court_count = get_court()
    brand_list, brand_count = get_brand()
    kind_list, kind_count = get_kind()

    total_list = []
    brand_pic = ''
    court_pic = ''
    for court in court_list:
        court_pic = flatten(court)
        total_list.append(court_pic)
        court_pic['sub_brand'] = []
        for brand in brand_list:
            if brand.court_id == court.id:
                brand_pic = flatten(brand)
                court_pic['sub_brand'].append(brand_pic)
                brand_pic['sub_kind'] = []
            for kind in kind_list:
                if brand.id == kind.brand_id:
                    kind_pic = flatten(kind)
                    brand_pic['sub_kind'].append(kind_pic)
        success['total'].append(court_pic)
