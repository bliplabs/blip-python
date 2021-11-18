import blip
from config import API_KEY

blip.configuration.username = API_KEY

try:
    api_response = blip.billers.get_billers_status()
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling billers->get_billers_status: %s\n" % e)
