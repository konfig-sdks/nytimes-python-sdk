<div align="left">

[![Visit The new york times](./header.png)](https://developer.nytimes.com)

# The new york times<a id="the-new-york-times"></a>

The Books API provides information about book reviews and The New York Times Best Sellers lists.

## Best Sellers Lists Services<a id="best-sellers-lists-services"></a>
### List Names<a id="list-names"></a>
The lists/names service returns a list of all the NYT Best Sellers Lists.  Some lists are published weekly and others monthly.  The response includes when each list was first published and last published.

```
/lists/names.json
```

### List Data<a id="list-data"></a>

The lists/{date}/{name} service returns the books on the best sellers list for the specified date and list name.

```
/lists/2019-01-20/hardcover-fiction.json
```

Use \"current\" for {date} to get the latest list.
```
/lists/current/hardcover-fiction.json
```

## Book Reviews Services<a id="book-reviews-services"></a>

The book reviews service lets you get NYT book review by author, ISBN, or title.

```
/reviews.json?author=Michelle+Obama
```

```
/reviews.json?isbn=9781524763138
```

```
/reviews.json?title=Becoming
```

## Example Calls<a id="example-calls"></a>

```
https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey
```

```
https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key=yourkey
```



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`nyt.list.get_all_best_sellers`](#nytlistget_all_best_sellers)
  * [`nyt.list.get_best_sellers`](#nytlistget_best_sellers)
  * [`nyt.list.get_best_sellers_overview`](#nytlistget_best_sellers_overview)
  * [`nyt.list.get_by_date`](#nytlistget_by_date)
  * [`nyt.list.get_history`](#nytlistget_history)
  * [`nyt.list.get_names`](#nytlistget_names)
  * [`nyt.review.get_book_reviews`](#nytreviewget_book_reviews)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=The%20New%20York%20Times&serviceName=Books&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from nytimes_python_sdk import Nyt, ApiException

nyt = Nyt(
    api_key="YOUR_API_KEY",
)

try:
    # Best Sellers List Full Overview
    get_all_best_sellers_response = nyt.list.get_all_best_sellers(
        published_date="0480-72-88",
    )
    print(get_all_best_sellers_response)
except ApiException as e:
    print("Exception when calling ModelListApi.get_all_best_sellers: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from nytimes_python_sdk import Nyt, ApiException

nyt = Nyt(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Best Sellers List Full Overview
        get_all_best_sellers_response = await nyt.list.aget_all_best_sellers(
            published_date="0480-72-88",
        )
        print(get_all_best_sellers_response)
    except ApiException as e:
        print("Exception when calling ModelListApi.get_all_best_sellers: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from nytimes_python_sdk import Nyt, ApiException

nyt = Nyt(
    api_key="YOUR_API_KEY",
)

try:
    # Best Sellers List Full Overview
    get_all_best_sellers_response = nyt.list.raw.get_all_best_sellers(
        published_date="0480-72-88",
    )
    pprint(get_all_best_sellers_response.body)
    pprint(get_all_best_sellers_response.body["status"])
    pprint(get_all_best_sellers_response.body["copyright"])
    pprint(get_all_best_sellers_response.body["num_results"])
    pprint(get_all_best_sellers_response.body["results"])
    pprint(get_all_best_sellers_response.headers)
    pprint(get_all_best_sellers_response.status)
    pprint(get_all_best_sellers_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ModelListApi.get_all_best_sellers: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `nyt.list.get_all_best_sellers`<a id="nytlistget_all_best_sellers"></a>

Get all books for all the Best Sellers lists for specified date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_best_sellers_response = nyt.list.get_all_best_sellers(
    published_date="0480-72-88",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### published_date: `str`<a id="published_date-str"></a>

YYYY-MM-DD  The best-seller list publication date. You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published date, the current week's best sellers lists will be returned.

#### 🔄 Return<a id="🔄-return"></a>

[`OverviewResponse`](./nytimes_python_sdk/pydantic/overview_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/full-overview.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.list.get_best_sellers`<a id="nytlistget_best_sellers"></a>

Get Best Sellers list.  If no date is provided returns the latest list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_best_sellers_response = nyt.list.get_best_sellers(
    _list="hardcover-fiction",
    bestsellers_date="0480-72-88",
    published_date="0480-72-88",
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _list: `str`<a id="_list-str"></a>

The name of the Times best sellers list (hardcover-fiction, paperback-nonfiction, ...). The /lists/names service returns all the list names. The encoded list names are lower case with hyphens instead of spaces (e.g. e-book-fiction, instead of E-Book Fiction).

##### bestsellers_date: `str`<a id="bestsellers_date-str"></a>

YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best sellers lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).

##### published_date: `str`<a id="published_date-str"></a>

YYYY-MM-DD  The date the best sellers list was published on NYTimes.com (different than bestsellers-date).  Use \"current\" for latest list.

##### offset: `int`<a id="offset-int"></a>

Sets the starting point of the result set (0, 20, ...).  Used to paginate thru books if list has more than 20. Defaults to 0.  The num_results field indicates how many books are in the list.

#### 🔄 Return<a id="🔄-return"></a>

[`ListGetBestSellersResponse`](./nytimes_python_sdk/pydantic/list_get_best_sellers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.list.get_best_sellers_overview`<a id="nytlistget_best_sellers_overview"></a>

Get top 5 books for all the Best Sellers lists for specified date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_best_sellers_overview_response = nyt.list.get_best_sellers_overview(
    published_date="0480-72-88",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### published_date: `str`<a id="published_date-str"></a>

YYYY-MM-DD  The best-seller list publication date. You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published date, the current week's best sellers lists will be returned.

#### 🔄 Return<a id="🔄-return"></a>

[`OverviewResponse`](./nytimes_python_sdk/pydantic/overview_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/overview.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.list.get_by_date`<a id="nytlistget_by_date"></a>

Get Best Sellers list by date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_date_response = nyt.list.get_by_date(
    date="current",
    _list="list_example",
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `str`<a id="date-str"></a>

YYYY-MM-DD or \"current\"  The date the best sellers list was published on NYTimes.com.  Use \"current\" to get latest list.

##### _list: `str`<a id="_list-str"></a>

Name of the Best Sellers List (e.g. hardcover-fiction). You can get the full list of names from the /lists/names.json service.

##### offset: `int`<a id="offset-int"></a>

Sets the starting point of the result set (0, 20, ...).  Used to paginate thru books if list has more than 20. Defaults to 0.  The num_results field indicates how many books are in the list.

#### 🔄 Return<a id="🔄-return"></a>

[`ListGetByDateResponse`](./nytimes_python_sdk/pydantic/list_get_by_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{date}/{list}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.list.get_history`<a id="nytlistget_history"></a>

Get Best Sellers list history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_response = nyt.list.get_history(
    age_group="string_example",
    author="string_example",
    contributor="string_example",
    isbn="string_example",
    offset=1,
    price="string_example",
    publisher="string_example",
    title="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### age_group: `str`<a id="age_group-str"></a>

The target age group for the best seller.

##### author: `str`<a id="author-str"></a>

The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author's first name.

##### contributor: `str`<a id="contributor-str"></a>

The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed.

##### isbn: `str`<a id="isbn-str"></a>

International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).

##### offset: `int`<a id="offset-int"></a>

Sets the starting point of the result set (0, 20, ...).  Used to paginate thru results if there are more than 20. Defaults to 0. The num_results field indicates how many results there are total.

##### price: `str`<a id="price-str"></a>

The publisher's list price of the best seller, including decimal point.

##### publisher: `str`<a id="publisher-str"></a>

The standardized name of the publisher

##### title: `str`<a id="title-str"></a>

The title of the best seller  When searching, you can specify a portion of a title or a full title.

#### 🔄 Return<a id="🔄-return"></a>

[`ListGetHistoryResponse`](./nytimes_python_sdk/pydantic/list_get_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/best-sellers/history.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.list.get_names`<a id="nytlistget_names"></a>

Get Best Sellers list names.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_names_response = nyt.list.get_names()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListGetNamesResponse`](./nytimes_python_sdk/pydantic/list_get_names_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/names.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nyt.review.get_book_reviews`<a id="nytreviewget_book_reviews"></a>

Get book reviews.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_book_reviews_response = nyt.review.get_book_reviews(
    isbn=1,
    title="string_example",
    author="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### isbn: `int`<a id="isbn-int"></a>

Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs.

##### title: `str`<a id="title-str"></a>

You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20.

##### author: `str`<a id="author-str"></a>

You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20.

#### 🔄 Return<a id="🔄-return"></a>

[`ReviewGetBookReviewsResponse`](./nytimes_python_sdk/pydantic/review_get_book_reviews_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reviews.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
