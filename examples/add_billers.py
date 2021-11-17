import blip
from blip.api import billers_api
from blip.model.biller_create import BillerCreate
from config import API_KEY

# Add your API Key and configure the API Client
configuration = blip.Configuration(
    host="http://localhost", username=API_KEY, password=""
)
api_client = blip.ApiClient(configuration)

# Configure an API instance for your desired endpoint
api_instance = billers_api.BillersApi(api_client)

billers_in = [
    {
        "name": "Verizon Fios",
        "url": "https://www.verizon.com/",
        "origin_id": "provider-1",
        "origin_name": "provider",
    }
]


try:
    # Add Billers
    api_response = api_instance.add_billers(billers_in)
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling BillersApi->add_billers: %s\n" % e)
