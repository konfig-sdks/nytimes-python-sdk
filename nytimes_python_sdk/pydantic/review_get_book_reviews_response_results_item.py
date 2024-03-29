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

from nytimes_python_sdk.pydantic.review_get_book_reviews_response_results_item_isbn13 import ReviewGetBookReviewsResponseResultsItemIsbn13

class ReviewGetBookReviewsResponseResultsItem(BaseModel):
    summary: typing.Optional[str] = Field(None, alias='summary')

    url: typing.Optional[str] = Field(None, alias='url')

    publication_dt: typing.Optional[str] = Field(None, alias='publication_dt')

    byline: typing.Optional[str] = Field(None, alias='byline')

    book_title: typing.Optional[str] = Field(None, alias='book_title')

    book_author: typing.Optional[str] = Field(None, alias='book_author')

    isbn13: typing.Optional[ReviewGetBookReviewsResponseResultsItemIsbn13] = Field(None, alias='isbn13')
    class Config:
        arbitrary_types_allowed = True
