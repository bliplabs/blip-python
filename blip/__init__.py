# flake8: noqa

"""
    API Reference

      The Blip API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). This data is only available through HTTPS to ensure the security of the data being transferred.  | Base URL                | | ------------------------| | https://api.tryblip.com |  # Authentication  The Blip API uses API Keys to authenticate requests. Test mode secret keys have the prefix **`key_test_`** and live mode secret keys have the prefix **`key_live_`**. Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, etc. Authentication to the API is performed via [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication). Provide your API key as the basic auth username value. You do not need to provide a password. All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.  # Errors  Blip uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with Blip's servers (these are rare). Some 4xx errors that could be handled programmatically include an error code that briefly explains the error reported.  | Code | Type | Description | | --- | --- | --- | | 200 | OK | Everything worked as expected. | | 402 | Request Failed | The request was unacceptable. | | 401 | Unauthorized | The API key provided was invalid. | | 403 | Forbidden | The API key does not have permissions to access the resource. | | 404 | Not Found | The requested resource does not exist. | | 429 | Too Many Requests | Too many requests hit the API too quickly. | | 500, 502, 503, 504 | Server Error | Something went wrong with Blip's server. |   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import ApiClient
from blip.api_client import ApiClient

# import Configuration
from blip.configuration import Configuration

# import exceptions
from blip.exceptions import OpenApiException
from blip.exceptions import ApiAttributeError
from blip.exceptions import ApiTypeError
from blip.exceptions import ApiValueError
from blip.exceptions import ApiKeyError
from blip.exceptions import ApiException

# Custom additions for easier configuration and usage
from blip.api import billers_api, transactions_api

host = "http://localhost"

configuration = Configuration(host=host, username="", password="")
api_client = ApiClient(configuration)

billers = billers_api.BillersApi(api_client)
transactions = transactions_api.TransactionsApi(api_client)
