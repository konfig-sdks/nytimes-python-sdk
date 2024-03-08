import typing_extensions

from nytimes_python_sdk.paths import PathValues
from nytimes_python_sdk.apis.paths.lists_json import ListsJson
from nytimes_python_sdk.apis.paths.lists_date_list_json import ListsDateListJson
from nytimes_python_sdk.apis.paths.lists_full_overview_json import ListsFullOverviewJson
from nytimes_python_sdk.apis.paths.lists_overview_json import ListsOverviewJson
from nytimes_python_sdk.apis.paths.lists_names_json import ListsNamesJson
from nytimes_python_sdk.apis.paths.lists_best_sellers_history_json import ListsBestSellersHistoryJson
from nytimes_python_sdk.apis.paths.reviews_json import ReviewsJson

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.LISTS_JSON: ListsJson,
        PathValues.LISTS_DATE_LIST_JSON: ListsDateListJson,
        PathValues.LISTS_FULLOVERVIEW_JSON: ListsFullOverviewJson,
        PathValues.LISTS_OVERVIEW_JSON: ListsOverviewJson,
        PathValues.LISTS_NAMES_JSON: ListsNamesJson,
        PathValues.LISTS_BESTSELLERS_HISTORY_JSON: ListsBestSellersHistoryJson,
        PathValues.REVIEWS_JSON: ReviewsJson,
    }
)

path_to_api = PathToApi(
    {
        PathValues.LISTS_JSON: ListsJson,
        PathValues.LISTS_DATE_LIST_JSON: ListsDateListJson,
        PathValues.LISTS_FULLOVERVIEW_JSON: ListsFullOverviewJson,
        PathValues.LISTS_OVERVIEW_JSON: ListsOverviewJson,
        PathValues.LISTS_NAMES_JSON: ListsNamesJson,
        PathValues.LISTS_BESTSELLERS_HISTORY_JSON: ListsBestSellersHistoryJson,
        PathValues.REVIEWS_JSON: ReviewsJson,
    }
)
