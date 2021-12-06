# blip-python

The official python client library for the Blip API. For complete information, check out our [docs](https://docs.tryblip.com)

## Requirements.

Python >= 3.6

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/bliplabs/blip-python.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bliplabs/blip-python.git`)

Then import the package:

```python
import blip
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import blip
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import blip
from blip.api import billers_api
from blip.model.biller_create import BillerCreate

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

# The client must also configure the authentication and authorization parameters
# in accordance with the API server security policy.
configuration = blip.Configuration(
    host = 'http://localhost',
    username = 'YOUR_API_KEY',
)


# Enter a context with an instance of the API client
with blip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = billers_api.BillersApi(api_client)
    biller_create = [
        BillerCreate(
            name="name_example",
            domain="domain_example",
            login_url="login_url_example",
            url="url_example",
            categories=[
                "categories_example",
            ],
            origin_id="origin_id_example",
            origin_name="origin_name_example",
            display_name="display_name_example",
            logo_url="logo_url_example",
        ),
    ] # [BillerCreate] |

    try:
        # Add Billers
        api_response = api_instance.add_billers(biller_create)
        print(api_response)
    except blip.ApiException as e:
        print("Exception when calling BillersApi->add_billers: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to _http://localhost_

| Class             | Method                                                                           | HTTP request                     | Description              |
| ----------------- | -------------------------------------------------------------------------------- | -------------------------------- | ------------------------ |
| _BillersApi_      | [**add_billers**](docs/BillersApi.md#add_billers)                                | **POST** /v1/billers             | Add Billers              |
| _BillersApi_      | [**enhance_billers**](docs/BillersApi.md#enhance_billers)                        | **POST** /v1/billers/enhance     | Enhance Billers          |
| _BillersApi_      | [**get_biller**](docs/BillersApi.md#get_biller)                                  | **GET** /v1/billers/{id}         | Get Biller               |
| _BillersApi_      | [**get_billers_status**](docs/BillersApi.md#get_billers_status)                  | **GET** /v1/billers/status       | Get Billers Status       |
| _BillersApi_      | [**update_biller**](docs/BillersApi.md#update_biller)                            | **PUT** /v1/billers/{id}         | Update Biller            |
| _TransactionsApi_ | [**add_transactions**](docs/TransactionsApi.md#add_transactions)                 | **POST** /v1/transactions        | Add Transactions         |
| _TransactionsApi_ | [**get_transactions**](docs/TransactionsApi.md#get_transactions)                 | **GET** /v1/transactions         | Get Transactions         |
| _TransactionsApi_ | [**get_transactions_results**](docs/TransactionsApi.md#get_transactions_results) | **GET** /v1/transactions/results | Get Transactions Results |
| _TransactionsApi_ | [**get_transactions_status**](docs/TransactionsApi.md#get_transactions_status)   | **GET** /v1/transactions/status  | Get Transactions Status  |
| _TransactionsApi_ | [**update_transaction**](docs/TransactionsApi.md#update_transaction)             | **PUT** /v1/transactions/{id}    | Update Transaction       |

## Documentation For Models

- [Biller](docs/Biller.md)
- [BillerCreate](docs/BillerCreate.md)
- [BillerCreateMultiResponse](docs/BillerCreateMultiResponse.md)
- [BillerEnhanceCreate](docs/BillerEnhanceCreate.md)
- [BillerEnhanceResult](docs/BillerEnhanceResult.md)
- [BillerInResult](docs/BillerInResult.md)
- [BillerUpdate](docs/BillerUpdate.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [Transaction](docs/Transaction.md)
- [TransactionCreate](docs/TransactionCreate.md)
- [TransactionCreateMultiResponse](docs/TransactionCreateMultiResponse.md)
- [TransactionInResult](docs/TransactionInResult.md)
- [TransactionResultsResponse](docs/TransactionResultsResponse.md)
- [TransactionUpdate](docs/TransactionUpdate.md)
- [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

## HTTPBasic

- **Type**: HTTP basic authentication

## Author

## Notes for Large OpenAPI documents

If the OpenAPI document is large, imports in blip.apis and blip.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:

- `from blip.api.default_api import DefaultApi`
- `from blip.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:

```
import sys
sys.setrecursionlimit(1500)
import blip
from blip.apis import *
from blip.models import *
```
