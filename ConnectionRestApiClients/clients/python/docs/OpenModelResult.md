# OpenModelResult

Results of open model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_on_members** | [**List[ResultOnMembers]**](ResultOnMembers.md) | Results on members | [optional] 

## Example

```python
from connection_restapi_client_poc.models.open_model_result import OpenModelResult

# TODO update the JSON string below
json = "{}"
# create an instance of OpenModelResult from a JSON string
open_model_result_instance = OpenModelResult.from_json(json)
# print the JSON string representation of the object
print(OpenModelResult.to_json())

# convert the object into a dict
open_model_result_dict = open_model_result_instance.to_dict()
# create an instance of OpenModelResult from a dict
open_model_result_from_dict = OpenModelResult.from_dict(open_model_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


