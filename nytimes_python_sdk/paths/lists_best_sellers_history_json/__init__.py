# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nytimes_python_sdk.paths.lists_best_sellers_history_json import Api

from nytimes_python_sdk.paths import PathValues

path = PathValues.LISTS_BESTSELLERS_HISTORY_JSON