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


class ListGetByDateResponseResults(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            list_name = schemas.StrSchema
            bestsellers_date = schemas.StrSchema
            published_date = schemas.StrSchema
            display_name = schemas.StrSchema
            normal_list_ends_at = schemas.IntSchema
            updated = schemas.StrSchema
        
            @staticmethod
            def books() -> typing.Type['ListGetByDateResponseResultsBooks']:
                return ListGetByDateResponseResultsBooks
        
            @staticmethod
            def corrections() -> typing.Type['ListGetByDateResponseResultsCorrections']:
                return ListGetByDateResponseResultsCorrections
            __annotations__ = {
                "list_name": list_name,
                "bestsellers_date": bestsellers_date,
                "published_date": published_date,
                "display_name": display_name,
                "normal_list_ends_at": normal_list_ends_at,
                "updated": updated,
                "books": books,
                "corrections": corrections,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_name"]) -> MetaOapg.properties.list_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bestsellers_date"]) -> MetaOapg.properties.bestsellers_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_date"]) -> MetaOapg.properties.published_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normal_list_ends_at"]) -> MetaOapg.properties.normal_list_ends_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["books"]) -> 'ListGetByDateResponseResultsBooks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["corrections"]) -> 'ListGetByDateResponseResultsCorrections': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["list_name", "bestsellers_date", "published_date", "display_name", "normal_list_ends_at", "updated", "books", "corrections", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_name"]) -> typing.Union[MetaOapg.properties.list_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bestsellers_date"]) -> typing.Union[MetaOapg.properties.bestsellers_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_date"]) -> typing.Union[MetaOapg.properties.published_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normal_list_ends_at"]) -> typing.Union[MetaOapg.properties.normal_list_ends_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["books"]) -> typing.Union['ListGetByDateResponseResultsBooks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["corrections"]) -> typing.Union['ListGetByDateResponseResultsCorrections', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list_name", "bestsellers_date", "published_date", "display_name", "normal_list_ends_at", "updated", "books", "corrections", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        list_name: typing.Union[MetaOapg.properties.list_name, str, schemas.Unset] = schemas.unset,
        bestsellers_date: typing.Union[MetaOapg.properties.bestsellers_date, str, schemas.Unset] = schemas.unset,
        published_date: typing.Union[MetaOapg.properties.published_date, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        normal_list_ends_at: typing.Union[MetaOapg.properties.normal_list_ends_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, str, schemas.Unset] = schemas.unset,
        books: typing.Union['ListGetByDateResponseResultsBooks', schemas.Unset] = schemas.unset,
        corrections: typing.Union['ListGetByDateResponseResultsCorrections', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListGetByDateResponseResults':
        return super().__new__(
            cls,
            *args,
            list_name=list_name,
            bestsellers_date=bestsellers_date,
            published_date=published_date,
            display_name=display_name,
            normal_list_ends_at=normal_list_ends_at,
            updated=updated,
            books=books,
            corrections=corrections,
            _configuration=_configuration,
            **kwargs,
        )

from nytimes_python_sdk.model.list_get_by_date_response_results_books import ListGetByDateResponseResultsBooks
from nytimes_python_sdk.model.list_get_by_date_response_results_corrections import ListGetByDateResponseResultsCorrections