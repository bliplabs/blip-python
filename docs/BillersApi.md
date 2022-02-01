# blip.BillersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_biller**](BillersApi.md#get_biller) | **GET** /v1/billers/{origin_id} | Get Biller
[**search_billers**](BillersApi.md#search_billers) | **POST** /v1/billers/search | Search Billers


# **get_biller**
> Biller get_biller(origin_id)

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
    origin_id = "origin_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Biller
        api_response = api_instance.get_biller(origin_id)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->get_biller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_id** | **str**|  |

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

# **search_billers**
> BillerSearchResults search_billers(biller_search_params)

Search Billers

Get a biller.

### Example


```python
import time
import blip
from blip.api import billers_api
from blip.model.http_validation_error import HTTPValidationError
from blip.model.biller_search_results import BillerSearchResults
from blip.model.biller_search_params import BillerSearchParams
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.


# Enter a context with an instance of the API client
with blip.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = billers_api.BillersApi(api_client)
    biller_search_params = BillerSearchParams(
        q="",
        offset=0,
        limit=20,
        filter=None,
        facets_distribution=[
            "facets_distribution_example",
        ],
        attributes_to_retrieve=["*"],
        attributes_to_crop=[
            "attributes_to_crop_example",
        ],
        crop_length=200,
        attributes_to_highlight=[
            "attributes_to_highlight_example",
        ],
        matches=False,
        sort=[
            "sort_example",
        ],
    ) # BillerSearchParams | 

    # example passing only required values which don't have defaults set
    try:
        # Search Billers
        api_response = api_instance.search_billers(biller_search_params)
        pprint(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->search_billers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biller_search_params** | [**BillerSearchParams**](BillerSearchParams.md)|  |

### Return type

[**BillerSearchResults**](BillerSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

