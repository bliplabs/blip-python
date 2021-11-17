import blip
from config import API_KEY

blip.configuration.username = API_KEY

billers_in = [
    {
        "name": "Verizon Fios",
        "url": "https://www.verizon.com/",
        "origin_id": "provider-1",
        "origin_name": "provider",
    }
]

try:
    api_response = blip.billers.add_billers(billers_in)
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling BillersApi->add_billers: %s\n" % e)
