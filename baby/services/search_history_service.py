# coding: UTF-8

from ..models.feature_model import SearchHistory
from ..models import db


def search_history_list():
    """
        搜索历史记录
            根据id倒叙排序
    """
    search_history_count = SearchHistory.query.filter().order_by(SearchHistory.id.desc()).count()
    if search_history_count > 1:
        search_historys = SearchHistory.query.filter().order_by(SearchHistory.id.desc())[:3]
        return search_historys
    else:
        search_history = SearchHistory.query.filter().first()
        return search_history


def delete_all_search():
    """
        清楚历史记录
    """
    search_history_count = SearchHistory.query.filter().count()
    if search_history_count > 1:
        search_historys = SearchHistory.query.filter().all()
        for search in search_historys:
            db.delete(search)
            db.commit()
        return 0
    else:
        search_history = SearchHistory.query.filter().first()
        db.delete(search_history)
        db.commit()
        return 1
