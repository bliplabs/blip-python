# TransactionResultsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** |  | 
**is_bill** | **bool** |  | 
**amount_mean** | **float** |  | 
**amount_std** | **float** |  | 
**date_diff_avg** | **int** |  | 
**first_transaction** | **date** |  | 
**last_transaction** | **date** |  | 
**transaction_count** | **int** |  | 
**transactions** | [**[TransactionInResult]**](TransactionInResult.md) |  | 
**suggested_billers** | [**[BillerInResult], none_type**](BillerInResult.md) |  | [optional]  if omitted the server will use the default value of []
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


