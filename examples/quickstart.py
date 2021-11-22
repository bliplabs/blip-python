import blip
from config import API_KEY

blip.configuration.username = API_KEY

# 1) Biller configuration
#    This example uses the default configuration.

# 2) Submit transactions
transactions_in = [
    {
        "origin_id": "3fX1poGI7twHNKANdLal9",
        "name": "AMERICAN EXPRESS ACH PMT    M0000           WEB ID: 1111111111",
        "date": "2019-11-04",
        "amount": -293.88,
        "account_id": "hl3EG5XCNTX3eMmzsn9Au",
        "user_id": "ibN0eluvlVQBbjIma3DDG",
    },
    {
        "id": "jQfA2qMb6ZS8JEsdlDd5Y",
        "name": "VERIZON*RECURRING PAY",
        "date": "2019-09-16",
        "amount": -64.99,
        "transaction_account_id": "hl3EG5XCNTX3eMmzsn9Au",
        "user_id": "ibN0eluvlVQBbjIma3DDG",
    },
]

try:
    api_response = blip.transactions.add_transactions(transactions_in)
    print(api_response)

    transactions_status_resp = blip.transactions.get_transactions_status(
        batch_id=api_response["batch_id"]
    )
    print(transactions_status_resp)

    while transactions_status_resp[0].get("complete") == False:
        transactions_status_resp = blip.transactions.get_transactions_status(
            batch_id=api_response["batch_id"]
        )
        print(transactions_status_resp)

    results_resp = blip.transactions.get_transactions_results(
        batch_id=api_response["batch_id"]
    )
    print(results_resp)

except blip.ApiException as e:
    print("Blip API Exception: %s\n" % e)