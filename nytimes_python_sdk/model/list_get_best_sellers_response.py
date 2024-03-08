# coding: utf-8

"""
    Books API

    The Books API provides information about book reviews and The New York Times Best Sellers lists.  ## Best Sellers Lists Services ### List Names The lists/names service returns a list of all the NYT Best Sellers Lists.  Some lists are published weekly and others monthly.  The response includes when each list was first published and last published.  ``` /lists/names.json ```  ### List Data  The lists/{date}/{name} service returns the books on the best sellers list for the specified date and list name.  ``` /lists/2019-01-20/hardcover-fiction.json ```  Use \"current\" for {date} to get the latest list. ``` /lists/current/hardcover-fiction.json ```  ## Book Reviews Services  The book reviews service lets you get NYT book review by author, ISBN, or title.  ``` /reviews.json?author=Michelle+Obama ```  ``` /reviews.json?isbn=9781524763138 ```  ``` /reviews.json?title=Becoming ```  ## Example Calls  ``` https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key=yourkey ``` 

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nytimes_python_sdk import schemas  # noqa: F401


class ListGetBestSellersResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
            copyright = schemas.StrSchema
            num_results = schemas.IntSchema
            last_modified = schemas.StrSchema
        
            @staticmethod
            def results() -> typing.Type['ListGetBestSellersResponseResults']:
                return ListGetBestSellersResponseResults
            __annotations__ = {
                "status": status,
                "copyright": copyright,
                "num_results": num_results,
                "last_modified": last_modified,
                "results": results,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyright"]) -> MetaOapg.properties.copyright: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_results"]) -> MetaOapg.properties.num_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_modified"]) -> MetaOapg.properties.last_modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> 'ListGetBestSellersResponseResults': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "copyright", "num_results", "last_modified", "results", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyright"]) -> typing.Union[MetaOapg.properties.copyright, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_results"]) -> typing.Union[MetaOapg.properties.num_results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_modified"]) -> typing.Union[MetaOapg.properties.last_modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union['ListGetBestSellersResponseResults', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "copyright", "num_results", "last_modified", "results", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        copyright: typing.Union[MetaOapg.properties.copyright, str, schemas.Unset] = schemas.unset,
        num_results: typing.Union[MetaOapg.properties.num_results, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_modified: typing.Union[MetaOapg.properties.last_modified, str, schemas.Unset] = schemas.unset,
        results: typing.Union['ListGetBestSellersResponseResults', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListGetBestSellersResponse':
        return super().__new__(
            cls,
            *args,
            status=status,
            copyright=copyright,
            num_results=num_results,
            last_modified=last_modified,
            results=results,
            _configuration=_configuration,
            **kwargs,
        )

from nytimes_python_sdk.model.list_get_best_sellers_response_results import ListGetBestSellersResponseResults