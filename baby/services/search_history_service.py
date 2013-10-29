# coding: UTF-8

from ..models.feature_model import SearchHistory


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