import blip
from config import API_KEY

blip.configuration.username = API_KEY

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
    api_response = blip.transactions.add_transactions(transactions_in)
    print(api_response)
except blip.ApiException as e:
    print("Exception when calling transactions->add_transactions: %s\n" % e)