# coding: utf-8

"""
    Books API

    The Books API provides information about book reviews and The New York Times Best Sellers lists.  ## Best Sellers Lists Services ### List Names The lists/names service returns a list of all the NYT Best Sellers Lists.  Some lists are published weekly and others monthly.  The response includes when each list was first published and last published.  ``` /lists/names.json ```  ### List Data  The lists/{date}/{name} service returns the books on the best sellers list for the specified date and list name.  ``` /lists/2019-01-20/hardcover-fiction.json ```  Use \"current\" for {date} to get the latest list. ``` /lists/current/hardcover-fiction.json ```  ## Book Reviews Services  The book reviews service lets you get NYT book review by author, ISBN, or title.  ``` /reviews.json?author=Michelle+Obama ```  ``` /reviews.json?isbn=9781524763138 ```  ``` /reviews.json?title=Becoming ```  ## Example Calls  ``` https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key=yourkey ``` 

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import nytimes_python_sdk
from nytimes_python_sdk.model.list_get_by_date_response_results_books_item_isbns import ListGetByDateResponseResultsBooksItemIsbns
from nytimes_python_sdk import configuration


class TestListGetByDateResponseResultsBooksItemIsbns(unittest.TestCase):
    """ListGetByDateResponseResultsBooksItemIsbns unit test stubs"""
    pass


if __name__ == '__main__':
    unittest.main()
