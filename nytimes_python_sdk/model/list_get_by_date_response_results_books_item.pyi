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


class ListGetByDateResponseResultsBooksItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            rank = schemas.IntSchema
            rank_last_week = schemas.IntSchema
            weeks_on_list = schemas.IntSchema
            asterisk = schemas.IntSchema
            dagger = schemas.IntSchema
            primary_isbn10 = schemas.StrSchema
            primary_isbn13 = schemas.StrSchema
            publisher = schemas.StrSchema
            price = schemas.IntSchema
            author = schemas.StrSchema
            contributor = schemas.StrSchema
            contributor_note = schemas.StrSchema
            book_image = schemas.StrSchema
            amazon_product_url = schemas.StrSchema
            age_group = schemas.StrSchema
            book_review_link = schemas.StrSchema
            first_chapter_link = schemas.StrSchema
            sunday_review_link = schemas.StrSchema
            article_chapter_link = schemas.StrSchema
        
            @staticmethod
            def isbns() -> typing.Type['ListGetByDateResponseResultsBooksItemIsbns']:
                return ListGetByDateResponseResultsBooksItemIsbns
            __annotations__ = {
                "title": title,
                "description": description,
                "rank": rank,
                "rank_last_week": rank_last_week,
                "weeks_on_list": weeks_on_list,
                "asterisk": asterisk,
                "dagger": dagger,
                "primary_isbn10": primary_isbn10,
                "primary_isbn13": primary_isbn13,
                "publisher": publisher,
                "price": price,
                "author": author,
                "contributor": contributor,
                "contributor_note": contributor_note,
                "book_image": book_image,
                "amazon_product_url": amazon_product_url,
                "age_group": age_group,
                "book_review_link": book_review_link,
                "first_chapter_link": first_chapter_link,
                "sunday_review_link": sunday_review_link,
                "article_chapter_link": article_chapter_link,
                "isbns": isbns,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank_last_week"]) -> MetaOapg.properties.rank_last_week: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeks_on_list"]) -> MetaOapg.properties.weeks_on_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asterisk"]) -> MetaOapg.properties.asterisk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dagger"]) -> MetaOapg.properties.dagger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_isbn10"]) -> MetaOapg.properties.primary_isbn10: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_isbn13"]) -> MetaOapg.properties.primary_isbn13: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publisher"]) -> MetaOapg.properties.publisher: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> MetaOapg.properties.author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor"]) -> MetaOapg.properties.contributor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributor_note"]) -> MetaOapg.properties.contributor_note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["book_image"]) -> MetaOapg.properties.book_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amazon_product_url"]) -> MetaOapg.properties.amazon_product_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age_group"]) -> MetaOapg.properties.age_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["book_review_link"]) -> MetaOapg.properties.book_review_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_chapter_link"]) -> MetaOapg.properties.first_chapter_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sunday_review_link"]) -> MetaOapg.properties.sunday_review_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["article_chapter_link"]) -> MetaOapg.properties.article_chapter_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isbns"]) -> 'ListGetByDateResponseResultsBooksItemIsbns': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "rank", "rank_last_week", "weeks_on_list", "asterisk", "dagger", "primary_isbn10", "primary_isbn13", "publisher", "price", "author", "contributor", "contributor_note", "book_image", "amazon_product_url", "age_group", "book_review_link", "first_chapter_link", "sunday_review_link", "article_chapter_link", "isbns", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> typing.Union[MetaOapg.properties.rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank_last_week"]) -> typing.Union[MetaOapg.properties.rank_last_week, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeks_on_list"]) -> typing.Union[MetaOapg.properties.weeks_on_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asterisk"]) -> typing.Union[MetaOapg.properties.asterisk, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dagger"]) -> typing.Union[MetaOapg.properties.dagger, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_isbn10"]) -> typing.Union[MetaOapg.properties.primary_isbn10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_isbn13"]) -> typing.Union[MetaOapg.properties.primary_isbn13, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publisher"]) -> typing.Union[MetaOapg.properties.publisher, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union[MetaOapg.properties.author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor"]) -> typing.Union[MetaOapg.properties.contributor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributor_note"]) -> typing.Union[MetaOapg.properties.contributor_note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["book_image"]) -> typing.Union[MetaOapg.properties.book_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amazon_product_url"]) -> typing.Union[MetaOapg.properties.amazon_product_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age_group"]) -> typing.Union[MetaOapg.properties.age_group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["book_review_link"]) -> typing.Union[MetaOapg.properties.book_review_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_chapter_link"]) -> typing.Union[MetaOapg.properties.first_chapter_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sunday_review_link"]) -> typing.Union[MetaOapg.properties.sunday_review_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["article_chapter_link"]) -> typing.Union[MetaOapg.properties.article_chapter_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isbns"]) -> typing.Union['ListGetByDateResponseResultsBooksItemIsbns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "rank", "rank_last_week", "weeks_on_list", "asterisk", "dagger", "primary_isbn10", "primary_isbn13", "publisher", "price", "author", "contributor", "contributor_note", "book_image", "amazon_product_url", "age_group", "book_review_link", "first_chapter_link", "sunday_review_link", "article_chapter_link", "isbns", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        rank: typing.Union[MetaOapg.properties.rank, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rank_last_week: typing.Union[MetaOapg.properties.rank_last_week, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weeks_on_list: typing.Union[MetaOapg.properties.weeks_on_list, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        asterisk: typing.Union[MetaOapg.properties.asterisk, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dagger: typing.Union[MetaOapg.properties.dagger, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        primary_isbn10: typing.Union[MetaOapg.properties.primary_isbn10, str, schemas.Unset] = schemas.unset,
        primary_isbn13: typing.Union[MetaOapg.properties.primary_isbn13, str, schemas.Unset] = schemas.unset,
        publisher: typing.Union[MetaOapg.properties.publisher, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        author: typing.Union[MetaOapg.properties.author, str, schemas.Unset] = schemas.unset,
        contributor: typing.Union[MetaOapg.properties.contributor, str, schemas.Unset] = schemas.unset,
        contributor_note: typing.Union[MetaOapg.properties.contributor_note, str, schemas.Unset] = schemas.unset,
        book_image: typing.Union[MetaOapg.properties.book_image, str, schemas.Unset] = schemas.unset,
        amazon_product_url: typing.Union[MetaOapg.properties.amazon_product_url, str, schemas.Unset] = schemas.unset,
        age_group: typing.Union[MetaOapg.properties.age_group, str, schemas.Unset] = schemas.unset,
        book_review_link: typing.Union[MetaOapg.properties.book_review_link, str, schemas.Unset] = schemas.unset,
        first_chapter_link: typing.Union[MetaOapg.properties.first_chapter_link, str, schemas.Unset] = schemas.unset,
        sunday_review_link: typing.Union[MetaOapg.properties.sunday_review_link, str, schemas.Unset] = schemas.unset,
        article_chapter_link: typing.Union[MetaOapg.properties.article_chapter_link, str, schemas.Unset] = schemas.unset,
        isbns: typing.Union['ListGetByDateResponseResultsBooksItemIsbns', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListGetByDateResponseResultsBooksItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            rank=rank,
            rank_last_week=rank_last_week,
            weeks_on_list=weeks_on_list,
            asterisk=asterisk,
            dagger=dagger,
            primary_isbn10=primary_isbn10,
            primary_isbn13=primary_isbn13,
            publisher=publisher,
            price=price,
            author=author,
            contributor=contributor,
            contributor_note=contributor_note,
            book_image=book_image,
            amazon_product_url=amazon_product_url,
            age_group=age_group,
            book_review_link=book_review_link,
            first_chapter_link=first_chapter_link,
            sunday_review_link=sunday_review_link,
            article_chapter_link=article_chapter_link,
            isbns=isbns,
            _configuration=_configuration,
            **kwargs,
        )

from nytimes_python_sdk.model.list_get_by_date_response_results_books_item_isbns import ListGetByDateResponseResultsBooksItemIsbns
