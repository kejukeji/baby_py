# coding: UTF-8

from ..models.feature_model import SearchHistory


def search_history_list():
    """
        搜索历史记录
            根据id倒叙排序
    """
    search_history = SearchHistory.query.filter().order_by(SearchHistory.id.desc())
    return search_history