import blip
from blip.api import billers_api
from config import API_KEY

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host="http://localhost", username=API_KEY, password=""
)

api_client = blip.ApiClient(configuration)
api_instance = billers_api.BillersApi(api_client)


try:
    # Get Billers
    api_response = api_instance.get_biller(id="1")
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling BillersApi->add_billers: %s\n" % e)
