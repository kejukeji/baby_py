# coding: UTF-8

from baby.models.feature_model import TypeOfMilk, Court, Brand
from baby.services.base_service import get_model
from baby import db



def insert_formula(court_id, brand_id, type, energy, protein, carbon_compound, axunge):
    """

    """
    type_of_milk = TypeOfMilk(court_id=court_id, bran_id=brand_id, type=type, energy=energy, protein=protein,
                            carbon_compound=carbon_compound, axunge=axunge)
    db.add(type_of_milk)
    try:
        db.commit()
    except:
        return False
    return True


def get_court():
    """
    获取院内/外
    """
    court, court_count = get_model(Court)
    return court, court_count


def get_brand():
    """
    获取品牌
    """
    brand, brand_count = get_model(Brand)
    return brand, brand_count


def get_formula():
    """
    获取奶粉
    """
    formula, formula_count = get_model(TypeOfMilk)
    return formula, formula_count
