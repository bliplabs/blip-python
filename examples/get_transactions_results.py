import blip
from config import API_KEY

blip.configuration.username = API_KEY

try:
    # Get Billers
    api_response = blip.transactions.get_transactions_results()
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling transactions->get_transactions: %s\n" % e)
