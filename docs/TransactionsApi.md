# blip.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transactions**](TransactionsApi.md#add_transactions) | **POST** /v1/transactions | Add Transactions
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /v1/transactions | Get Transactions
[**get_transactions_results**](TransactionsApi.md#get_transactions_results) | **GET** /v1/transactions/results | Get Transactions Results
[**get_transactions_status**](TransactionsApi.md#get_transactions_status) | **GET** /v1/transactions/status | Get Transactions Status
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /v1/transactions/{id} | Update Transaction


# **add_transactions**
> TransactionCreateMultiResponse add_transactions(transaction_create)

Add Transactions

Add a new batch of transactions.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import transactions_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction_create_multi_response import TransactionCreateMultiResponse
from blip.model.transaction_create import TransactionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)

# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_create = [
        TransactionCreate(
            name="name_example",
            amount=3.14,
            date=dateutil_parser('1970-01-01').date(),
            account_id="account_id_example",
            origin_id="origin_id_example",
            user_id="user_id_example",
        ),
    ] # [TransactionCreate] | 

    # example passing only required values which don't have defaults set
    try:
        # Add Transactions
        api_response = api_instance.add_transactions(transaction_create)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling TransactionsApi->add_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_create** | [**[TransactionCreate]**](TransactionCreate.md)|  |

### Return type

[**TransactionCreateMultiResponse**](TransactionCreateMultiResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> [Transaction], none_type get_transactions()

Get Transactions

Get list of transactions.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import transactions_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction import Transaction
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)

# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    batch_id = "batch_gCu2LC4aWwWL9Y864DZta" # str, none_type |  (optional)
    limit = 500 # int |  (optional) if omitted the server will use the default value of 500
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Transactions
        api_response = api_instance.get_transactions(batch_id=batch_id, limit=limit, skip=skip)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str, none_type**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 500
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0

### Return type

[**[Transaction], none_type**](Transaction.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_results**
> [TransactionResultsResponse], none_type get_transactions_results()

Get Transactions Results

Get transaction results.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import transactions_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction_results_response import TransactionResultsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)

# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    batch_id = "batch_gCu2LC4aWwWL9Y864DZta" # str, none_type |  (optional)
    user_id = "user_id_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Transactions Results
        api_response = api_instance.get_transactions_results(batch_id=batch_id, user_id=user_id)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str, none_type**|  | [optional]
 **user_id** | **str, none_type**|  | [optional]

### Return type

[**[TransactionResultsResponse], none_type**](TransactionResultsResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_status**
> [TransactionCreateMultiResponse], none_type get_transactions_status()

Get Transactions Status

Get the status of the transactions.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import transactions_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction_create_multi_response import TransactionCreateMultiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)

# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    batch_id = "batch_gCu2LC4aWwWL9Y864DZta" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Transactions Status
        api_response = api_instance.get_transactions_status(batch_id=batch_id)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str, none_type**|  | [optional]

### Return type

[**[TransactionCreateMultiResponse], none_type**](TransactionCreateMultiResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> Transaction update_transaction(id, transaction_update)

Update Transaction

Update an transaction.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import transactions_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.transaction import Transaction
from blip.model.transaction_update import TransactionUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)

# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    id = "batch_gCu2LC4aWwWL9Y864DZta" # str | 
    transaction_update = TransactionUpdate(
        name="name_example",
        amount=3.14,
        date=None,
        account_id="account_id_example",
        origin_id="origin_id_example",
        user_id="user_id_example",
    ) # TransactionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update Transaction
        api_response = api_instance.update_transaction(id, transaction_update)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **transaction_update** | [**TransactionUpdate**](TransactionUpdate.md)|  |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

