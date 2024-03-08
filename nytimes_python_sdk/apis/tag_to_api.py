import typing_extensions

from nytimes_python_sdk.apis.tags import TagValues
from nytimes_python_sdk.apis.tags.model_list_api import ModelListApi
from nytimes_python_sdk.apis.tags.review_api import ReviewApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LIST: ModelListApi,
        TagValues.REVIEW: ReviewApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LIST: ModelListApi,
        TagValues.REVIEW: ReviewApi,
    }
)
