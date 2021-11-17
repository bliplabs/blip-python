"""
    API Reference

      The Blip API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). This data is only available through HTTPS to ensure the security of the data being transferred.  # Authentication  The Blip API uses API Keys to authenticate requests.  Test mode secret keys have the prefix **`key_test_`** and live mode secret keys have the prefix **`key_live_`**.   Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, etc.  Authentication to the API is performed via [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication). Provide your API key as the basic auth username value. You do not need to provide a password.  All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.  # Errors  Blip uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with Blip's servers (these are rare).  Some 4xx errors that could be handled programmatically include an error code that briefly explains the error reported.  | Code | Type | Description | | --- | --- | --- | | 200 | OK | Everything worked as expected. | | 402 | Request Failed | The request was unacceptable. | | 401 | Unauthorized | The API key provided was invalid. | | 403 | Forbidden | The API key does not have permissions to access the resource. | | 404 | Not Found | The requested resource does not exist. | | 429 | Too Many Requests | Too many requests hit the API too quickly. | | 500, 502, 503, 504 | Server Error | Something went wrong with Blip's server. |   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import blip
from blip.model.transaction_create_multi_response import TransactionCreateMultiResponse


class TestTransactionCreateMultiResponse(unittest.TestCase):
    """TransactionCreateMultiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionCreateMultiResponse(self):
        """Test TransactionCreateMultiResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionCreateMultiResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
