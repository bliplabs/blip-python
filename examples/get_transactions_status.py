import blip
from config import API_KEY

blip.configuration.username = API_KEY

try:
    api_response = blip.transactions.get_transactions_status(
        batch_id="batch_iq9oEPhMJhqbE0cg7xDhU"
    )
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling transactions->get_transactions_status: %s\n" % e)
