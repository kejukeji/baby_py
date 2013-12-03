# coding: UTF-8


def get_tracking_model(model, baby_id):
    """
    获取model
    """
    model_count = model.query.filter(model.baby_id == baby_id).count()
    if model_count > 1:
        models = model.query.filter(model.baby_id == baby_id).order_by(model.measure_date.desc()).all()
        return models, model_count
    elif model_count == 1:
        model_result = model.query.filter(model.baby_id == baby_id).first()
        return model_result, model_count
    else:
        return 0,0