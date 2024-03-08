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


class ListGetBestSellersResponseResultsItemBookDetailsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            contributor = schemas.StrSchema
            author = schemas.StrSchema
            contributor_note = schemas.StrSchema
            price = schemas.IntSchema
            age_group = schemas.StrSchema
            publisher = schemas.StrSchema
            primary_isbn13 = schemas.StrSchema
            primary_isbn10 = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "contributor": contributor,
                "author": author,
                "contributor_note": contributor_note,
                "price": price,
                "age_group": age_group,
                "publisher": publisher,
                "primary_isbn13": primary_isbn13,
                "primary_isbn10": primary_isbn10,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor"]) -> MetaOapg.properties.contributor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> MetaOapg.properties.author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor_note"]) -> MetaOapg.properties.contributor_note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age_group"]) -> MetaOapg.properties.age_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publisher"]) -> MetaOapg.properties.publisher: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_isbn13"]) -> MetaOapg.properties.primary_isbn13: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_isbn10"]) -> MetaOapg.properties.primary_isbn10: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "contributor", "author", "contributor_note", "price", "age_group", "publisher", "primary_isbn13", "primary_isbn10", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor"]) -> typing.Union[MetaOapg.properties.contributor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union[MetaOapg.properties.author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor_note"]) -> typing.Union[MetaOapg.properties.contributor_note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age_group"]) -> typing.Union[MetaOapg.properties.age_group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publisher"]) -> typing.Union[MetaOapg.properties.publisher, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_isbn13"]) -> typing.Union[MetaOapg.properties.primary_isbn13, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_isbn10"]) -> typing.Union[MetaOapg.properties.primary_isbn10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "contributor", "author", "contributor_note", "price", "age_group", "publisher", "primary_isbn13", "primary_isbn10", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        contributor: typing.Union[MetaOapg.properties.contributor, str, schemas.Unset] = schemas.unset,
        author: typing.Union[MetaOapg.properties.author, str, schemas.Unset] = schemas.unset,
        contributor_note: typing.Union[MetaOapg.properties.contributor_note, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        age_group: typing.Union[MetaOapg.properties.age_group, str, schemas.Unset] = schemas.unset,
        publisher: typing.Union[MetaOapg.properties.publisher, str, schemas.Unset] = schemas.unset,
        primary_isbn13: typing.Union[MetaOapg.properties.primary_isbn13, str, schemas.Unset] = schemas.unset,
        primary_isbn10: typing.Union[MetaOapg.properties.primary_isbn10, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListGetBestSellersResponseResultsItemBookDetailsItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            contributor=contributor,
            author=author,
            contributor_note=contributor_note,
            price=price,
            age_group=age_group,
            publisher=publisher,
            primary_isbn13=primary_isbn13,
            primary_isbn10=primary_isbn10,
            _configuration=_configuration,
            **kwargs,
        )
