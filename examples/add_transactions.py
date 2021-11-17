import blip
from blip.api import transactions_api
from config import API_KEY

# Add your API Key and configure the API Client
configuration = blip.Configuration(
    host="http://localhost", username=API_KEY, password=""
)
api_client = blip.ApiClient(configuration)

# Configure an API instance for your desired endpoint
api_instance = transactions_api.TransactionsApi(api_client)

transactions_in = [
    {
        "id": "jQfA2qMb6ZS8JEsdlDd5Y",
        "name": "VERIZON*RECURRING PAY",
        "date": "2019-09-16",
        "amount": -64.99,
        "transaction_account_id": "hl3EG5XCNTX3eMmzsn9Au",
        "user_id": "ibN0eluvlVQBbjIma3DDG",
    }
]


try:
    api_response = api_instance.add_transactions(transactions_in)
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling TransactionsApi->add_transactions: %s\n" % e)