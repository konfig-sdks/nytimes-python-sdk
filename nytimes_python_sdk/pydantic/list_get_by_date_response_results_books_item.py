# coding: utf-8

"""
    Books API

    The Books API provides information about book reviews and The New York Times Best Sellers lists.  ## Best Sellers Lists Services ### List Names The lists/names service returns a list of all the NYT Best Sellers Lists.  Some lists are published weekly and others monthly.  The response includes when each list was first published and last published.  ``` /lists/names.json ```  ### List Data  The lists/{date}/{name} service returns the books on the best sellers list for the specified date and list name.  ``` /lists/2019-01-20/hardcover-fiction.json ```  Use \"current\" for {date} to get the latest list. ``` /lists/current/hardcover-fiction.json ```  ## Book Reviews Services  The book reviews service lets you get NYT book review by author, ISBN, or title.  ``` /reviews.json?author=Michelle+Obama ```  ``` /reviews.json?isbn=9781524763138 ```  ``` /reviews.json?title=Becoming ```  ## Example Calls  ``` https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key=yourkey ``` 

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from nytimes_python_sdk.pydantic.list_get_by_date_response_results_books_item_isbns import ListGetByDateResponseResultsBooksItemIsbns

class ListGetByDateResponseResultsBooksItem(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    rank: typing.Optional[int] = Field(None, alias='rank')

    rank_last_week: typing.Optional[int] = Field(None, alias='rank_last_week')

    weeks_on_list: typing.Optional[int] = Field(None, alias='weeks_on_list')

    asterisk: typing.Optional[int] = Field(None, alias='asterisk')

    dagger: typing.Optional[int] = Field(None, alias='dagger')

    primary_isbn10: typing.Optional[str] = Field(None, alias='primary_isbn10')

    primary_isbn13: typing.Optional[str] = Field(None, alias='primary_isbn13')

    publisher: typing.Optional[str] = Field(None, alias='publisher')

    price: typing.Optional[int] = Field(None, alias='price')

    author: typing.Optional[str] = Field(None, alias='author')

    contributor: typing.Optional[str] = Field(None, alias='contributor')

    contributor_note: typing.Optional[str] = Field(None, alias='contributor_note')

    book_image: typing.Optional[str] = Field(None, alias='book_image')

    amazon_product_url: typing.Optional[str] = Field(None, alias='amazon_product_url')

    age_group: typing.Optional[str] = Field(None, alias='age_group')

    book_review_link: typing.Optional[str] = Field(None, alias='book_review_link')

    first_chapter_link: typing.Optional[str] = Field(None, alias='first_chapter_link')

    sunday_review_link: typing.Optional[str] = Field(None, alias='sunday_review_link')

    article_chapter_link: typing.Optional[str] = Field(None, alias='article_chapter_link')

    isbns: typing.Optional[ListGetByDateResponseResultsBooksItemIsbns] = Field(None, alias='isbns')
    class Config:
        arbitrary_types_allowed = True
