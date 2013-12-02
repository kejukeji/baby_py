# coding: UTF-8

from baby.models.feature_model import Court


def get_court():
    court = Court.query.filter().all()
    return court
