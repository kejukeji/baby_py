# coding: UTF-8

from baby.models.feature_model import TypeOfMilk
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
