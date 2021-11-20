"""
    API Reference

      The Blip API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). This data is only available through HTTPS to ensure the security of the data being transferred.  | Base URL                | | ------------------------| | https://api.tryblip.com |  # Authentication  The Blip API uses API Keys to authenticate requests. Test mode secret keys have the prefix **`key_test_`** and live mode secret keys have the prefix **`key_live_`**. Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, etc. Authentication to the API is performed via [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication). Provide your API key as the basic auth username value. You do not need to provide a password. All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.  # Errors  Blip uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with Blip's servers (these are rare). Some 4xx errors that could be handled programmatically include an error code that briefly explains the error reported.  | Code | Type | Description | | --- | --- | --- | | 200 | OK | Everything worked as expected. | | 402 | Request Failed | The request was unacceptable. | | 401 | Unauthorized | The API key provided was invalid. | | 403 | Forbidden | The API key does not have permissions to access the resource. | | 404 | Not Found | The requested resource does not exist. | | 429 | Too Many Requests | Too many requests hit the API too quickly. | | 500, 502, 503, 504 | Server Error | Something went wrong with Blip's server. |   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from blip.api_client import ApiClient, Endpoint as _Endpoint
from blip.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction import Transaction
from blip.model.transaction_create import TransactionCreate
from blip.model.transaction_create_multi_response import TransactionCreateMultiResponse
from blip.model.transaction_update import TransactionUpdate


class TransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_transactions_endpoint = _Endpoint(
            settings={
                "response_type": (TransactionCreateMultiResponse,),
                "auth": ["HTTPBasic"],
                "endpoint_path": "/v1/transactions",
                "operation_id": "add_transactions",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "transaction_create",
                ],
                "required": [
                    "transaction_create",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "transaction_create",
                ],
            },
            root_map={
                "validations": {
                    ("transaction_create",): {
                        "max_items": 1000,
                        "min_items": 1,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "transaction_create": ([TransactionCreate],),
                },
                "attribute_map": {},
                "location_map": {
                    "transaction_create": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.get_transactions_endpoint = _Endpoint(
            settings={
                "response_type": (
                    [Transaction],
                    none_type,
                ),
                "auth": ["HTTPBasic"],
                "endpoint_path": "/v1/transactions",
                "operation_id": "get_transactions",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "batch_id",
                    "limit",
                    "skip",
                ],
                "required": [],
                "nullable": [
                    "batch_id",
                ],
                "enum": [],
                "validation": [
                    "batch_id",
                    "limit",
                ],
            },
            root_map={
                "validations": {
                    ("batch_id",): {
                        "regex": {
                            "pattern": r"(batch_)([a-zA-Z0-9]{21})",  # noqa: E501
                        },
                    },
                    ("limit",): {
                        "inclusive_maximum": 1000,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "batch_id": (
                        str,
                        none_type,
                    ),
                    "limit": (int,),
                    "skip": (int,),
                },
                "attribute_map": {
                    "batch_id": "batch_id",
                    "limit": "limit",
                    "skip": "skip",
                },
                "location_map": {
                    "batch_id": "query",
                    "limit": "query",
                    "skip": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_transactions_results_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": ["HTTPBasic"],
                "endpoint_path": "/v1/transactions/results",
                "operation_id": "get_transactions_results",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_transactions_status_endpoint = _Endpoint(
            settings={
                "response_type": (TransactionCreateMultiResponse,),
                "auth": ["HTTPBasic"],
                "endpoint_path": "/v1/transactions/status",
                "operation_id": "get_transactions_status",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "batch_id",
                ],
                "required": [
                    "batch_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "batch_id",
                ],
            },
            root_map={
                "validations": {
                    ("batch_id",): {
                        "regex": {
                            "pattern": r"(batch_)([a-zA-Z0-9]{21})",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "batch_id": (str,),
                },
                "attribute_map": {
                    "batch_id": "batch_id",
                },
                "location_map": {
                    "batch_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.update_transaction_endpoint = _Endpoint(
            settings={
                "response_type": (Transaction,),
                "auth": ["HTTPBasic"],
                "endpoint_path": "/v1/transactions/{id}",
                "operation_id": "update_transaction",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "transaction_update",
                ],
                "required": [
                    "id",
                    "transaction_update",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "id",
                ],
            },
            root_map={
                "validations": {
                    ("id",): {
                        "regex": {
                            "pattern": r"(batch_)([a-zA-Z0-9]{21})",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "id": (str,),
                    "transaction_update": (TransactionUpdate,),
                },
                "attribute_map": {
                    "id": "id",
                },
                "location_map": {
                    "id": "path",
                    "transaction_update": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

    def add_transactions(self, transaction_create, **kwargs):
        """Add Transactions  # noqa: E501

        Add a new batch of transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_transactions(transaction_create, async_req=True)
        >>> result = thread.get()

        Args:
            transaction_create ([TransactionCreate]):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionCreateMultiResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["transaction_create"] = transaction_create
        return self.add_transactions_endpoint.call_with_http_info(**kwargs)

    def get_transactions(self, **kwargs):
        """Get Transactions  # noqa: E501

        Get list of transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transactions(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            batch_id (str, none_type): [optional]
            limit (int): [optional] if omitted the server will use the default value of 500
            skip (int): [optional] if omitted the server will use the default value of 0
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Transaction], none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_transactions_endpoint.call_with_http_info(**kwargs)

    def get_transactions_results(self, **kwargs):
        """Get Transactions Results  # noqa: E501

        Get the suggested billers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transactions_results(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_transactions_results_endpoint.call_with_http_info(**kwargs)

    def get_transactions_status(self, batch_id, **kwargs):
        """Get Transactions Status  # noqa: E501

        Get the status of the transactions batch.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transactions_status(batch_id, async_req=True)
        >>> result = thread.get()

        Args:
            batch_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionCreateMultiResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["batch_id"] = batch_id
        return self.get_transactions_status_endpoint.call_with_http_info(**kwargs)

    def update_transaction(self, id, transaction_update, **kwargs):
        """Update Transaction  # noqa: E501

        Update an transaction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_transaction(id, transaction_update, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
            transaction_update (TransactionUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Transaction
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["id"] = id
        kwargs["transaction_update"] = transaction_update
        return self.update_transaction_endpoint.call_with_http_info(**kwargs)
