# ResultOnMember

Result of the member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**Member**](Member.md) |  | [optional] 
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**local_system_type** | [**ResultLocalSystemType**](ResultLocalSystemType.md) |  | [optional] 
**results** | **List[object]** | List of result | [optional] 

## Example

```python
from connection_restapi_client_poc.models.result_on_member import ResultOnMember

# TODO update the JSON string below
json = "{}"
# create an instance of ResultOnMember from a JSON string
result_on_member_instance = ResultOnMember.from_json(json)
# print the JSON string representation of the object
print(ResultOnMember.to_json())

# convert the object into a dict
result_on_member_dict = result_on_member_instance.to_dict()
# create an instance of ResultOnMember from a dict
result_on_member_from_dict = ResultOnMember.from_dict(result_on_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


