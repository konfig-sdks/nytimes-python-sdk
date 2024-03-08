# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nytimes_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    LISTS_JSON = "/lists.json"
    LISTS_DATE_LIST_JSON = "/lists/{date}/{list}.json"
    LISTS_FULLOVERVIEW_JSON = "/lists/full-overview.json"
    LISTS_OVERVIEW_JSON = "/lists/overview.json"
    LISTS_NAMES_JSON = "/lists/names.json"
    LISTS_BESTSELLERS_HISTORY_JSON = "/lists/best-sellers/history.json"
    REVIEWS_JSON = "/reviews.json"
