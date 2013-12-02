# coding: UTF-8


def get_model(model):
    """
    获取model
    """
    model_count = model.query.filter().count()
    if model_count > 1:
        models = model.query.filter().all()
        return models, model_count
    elif model_count == 1:
        model_result = model.query.filter().first()
        return model_result, model_count