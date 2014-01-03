# coding: UTF-8
from baby.models.feature_model import Tracking
from sqlalchemy import desc, asc


def get_tracking_model(model, baby_id):
    """
    获取model
    """
    model_count = Tracking.query.filter(Tracking.baby_id == baby_id).count()
    if model_count > 1:
        models = Tracking.query.filter(Tracking.baby_id == baby_id).order_by(desc(Tracking.measure_date)).all()
        return models, model_count
    elif model_count == 1:
        model_result = Tracking.query.filter(Tracking.baby_id == baby_id).first()
        return model_result, model_count
    else:
        return 0,0