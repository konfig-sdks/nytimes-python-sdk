# coding: utf-8

"""
    Books API

    The Books API provides information about book reviews and The New York Times Best Sellers lists.  ## Best Sellers Lists Services ### List Names The lists/names service returns a list of all the NYT Best Sellers Lists.  Some lists are published weekly and others monthly.  The response includes when each list was first published and last published.  ``` /lists/names.json ```  ### List Data  The lists/{date}/{name} service returns the books on the best sellers list for the specified date and list name.  ``` /lists/2019-01-20/hardcover-fiction.json ```  Use \"current\" for {date} to get the latest list. ``` /lists/current/hardcover-fiction.json ```  ## Book Reviews Services  The book reviews service lets you get NYT book review by author, ISBN, or title.  ``` /reviews.json?author=Michelle+Obama ```  ``` /reviews.json?isbn=9781524763138 ```  ``` /reviews.json?title=Becoming ```  ## Example Calls  ``` https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/books/v3/reviews.json?author=Stephen+King&api-key=yourkey ``` 

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from nytimes_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from nytimes_python_sdk.api_response import AsyncGeneratorResponse
from nytimes_python_sdk import api_client, exceptions
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

from nytimes_python_sdk.model.review_get_book_reviews_response import ReviewGetBookReviewsResponse as ReviewGetBookReviewsResponseSchema

from nytimes_python_sdk.type.review_get_book_reviews_response import ReviewGetBookReviewsResponse

from ...api_client import Dictionary
from nytimes_python_sdk.pydantic.review_get_book_reviews_response import ReviewGetBookReviewsResponse as ReviewGetBookReviewsResponsePydantic

# Query params
IsbnSchema = schemas.IntSchema
TitleSchema = schemas.StrSchema
AuthorSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'isbn': typing.Union[IsbnSchema, decimal.Decimal, int, ],
        'title': typing.Union[TitleSchema, str, ],
        'author': typing.Union[AuthorSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_isbn = api_client.QueryParameter(
    name="isbn",
    style=api_client.ParameterStyle.FORM,
    schema=IsbnSchema,
    explode=True,
)
request_query_title = api_client.QueryParameter(
    name="title",
    style=api_client.ParameterStyle.FORM,
    schema=TitleSchema,
    explode=True,
)
request_query_author = api_client.QueryParameter(
    name="author",
    style=api_client.ParameterStyle.FORM,
    schema=AuthorSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ReviewGetBookReviewsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReviewGetBookReviewsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReviewGetBookReviewsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_book_reviews_mapped_args(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if isbn is not None:
            _query_params["isbn"] = isbn
        if title is not None:
            _query_params["title"] = title
        if author is not None:
            _query_params["author"] = author
        args.query = _query_params
        return args

    async def _aget_book_reviews_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Reviews
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_isbn,
            request_query_title,
            request_query_author,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/reviews.json',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_book_reviews_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Reviews
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_isbn,
            request_query_title,
            request_query_author,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/reviews.json',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetBookReviewsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_book_reviews(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_book_reviews_mapped_args(
            isbn=isbn,
            title=title,
            author=author,
        )
        return await self._aget_book_reviews_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_book_reviews(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_book_reviews_mapped_args(
            isbn=isbn,
            title=title,
            author=author,
        )
        return self._get_book_reviews_oapg(
            query_params=args.query,
        )

class GetBookReviews(BaseApi):

    async def aget_book_reviews(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReviewGetBookReviewsResponsePydantic:
        raw_response = await self.raw.aget_book_reviews(
            isbn=isbn,
            title=title,
            author=author,
            **kwargs,
        )
        if validate:
            return ReviewGetBookReviewsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReviewGetBookReviewsResponsePydantic, raw_response.body)
    
    
    def get_book_reviews(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ReviewGetBookReviewsResponsePydantic:
        raw_response = self.raw.get_book_reviews(
            isbn=isbn,
            title=title,
            author=author,
        )
        if validate:
            return ReviewGetBookReviewsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReviewGetBookReviewsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_book_reviews_mapped_args(
            isbn=isbn,
            title=title,
            author=author,
        )
        return await self._aget_book_reviews_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        isbn: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_book_reviews_mapped_args(
            isbn=isbn,
            title=title,
            author=author,
        )
        return self._get_book_reviews_oapg(
            query_params=args.query,
        )

