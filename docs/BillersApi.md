# blip.BillersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billers**](BillersApi.md#add_billers) | **POST** /v1/billers | Add Billers
[**get_biller**](BillersApi.md#get_biller) | **GET** /v1/billers/{id} | Get Biller
[**get_billers_status**](BillersApi.md#get_billers_status) | **GET** /v1/billers/status | Get Billers Status
[**update_biller**](BillersApi.md#update_biller) | **PUT** /v1/billers/{id} | Update Biller


# **add_billers**
> BillerCreateMultiResponse add_billers(biller_create)

Add Billers

Add billers.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import billers_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.biller_create_multi_response import BillerCreateMultiResponse
from blip.model.biller_create import BillerCreate
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
    api_instance = billers_api.BillersApi(api_client)
    biller_create = [
        BillerCreate(
            name="name_example",
            domain="domain_example",
            logo_url="logo_url_example",
            login_url="login_url_example",
            url="url_example",
            categories=[
                "categories_example",
            ],
            origin_id="origin_id_example",
            origin_name="origin_name_example",
            display_name="display_name_example",
        ),
    ] # [BillerCreate] | 

    # example passing only required values which don't have defaults set
    try:
        # Add Billers
        api_response = api_instance.add_billers(biller_create)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->add_billers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biller_create** | [**[BillerCreate]**](BillerCreate.md)|  |

### Return type

[**BillerCreateMultiResponse**](BillerCreateMultiResponse.md)

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

# **get_biller**
> Biller get_biller(id)

Get Biller

Get a biller.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import billers_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.biller import Biller
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
    api_instance = billers_api.BillersApi(api_client)
    id = 0.0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Biller
        api_response = api_instance.get_biller(id)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->get_biller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Biller**](Biller.md)

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

# **get_billers_status**
> BillerCreateMultiResponse get_billers_status()

Get Billers Status

Get the status of the billers index.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import billers_api
from blip.model.biller_create_multi_response import BillerCreateMultiResponse
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
    api_instance = billers_api.BillersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Billers Status
        api_response = api_instance.get_billers_status()
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->get_billers_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BillerCreateMultiResponse**](BillerCreateMultiResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_biller**
> Biller update_biller(id, biller_update)

Update Biller

Update a biller.

### Example

* Basic Authentication (HTTPBasic):

```python
import time
import blip
from blip.api import billers_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.biller import Biller
from blip.model.biller_update import BillerUpdate
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
    api_instance = billers_api.BillersApi(api_client)
    id = 0.0 # int | 
    biller_update = BillerUpdate(
        name="name_example",
        domain="domain_example",
        logo_url="logo_url_example",
        login_url="login_url_example",
        url="url_example",
        categories=[
            "categories_example",
        ],
        display_name="display_name_example",
    ) # BillerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update Biller
        api_response = api_instance.update_biller(id, biller_update)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->update_biller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **biller_update** | [**BillerUpdate**](BillerUpdate.md)|  |

### Return type

[**Biller**](Biller.md)

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

