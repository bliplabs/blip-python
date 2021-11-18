import blip
from config import API_KEY

blip.configuration.username = API_KEY

try:
    # Get Billers
    api_response = blip.billers.get_biller(id="1")
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling billers->get_biller: %s\n" % e)
