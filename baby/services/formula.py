# coding: UTF-8


from baby.models.feature_model import Court, Brand


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