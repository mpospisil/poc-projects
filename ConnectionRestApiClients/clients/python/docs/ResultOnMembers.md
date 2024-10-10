# ResultOnMembers

Result of the member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loading** | [**Loading**](Loading.md) |  | [optional] 
**members** | [**List[ResultOnMember]**](ResultOnMember.md) | List of result of members | [optional] 

## Example

```python
from ideastatica_connection_api.models.result_on_members import ResultOnMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ResultOnMembers from a JSON string
result_on_members_instance = ResultOnMembers.from_json(json)
# print the JSON string representation of the object
print(ResultOnMembers.to_json())

# convert the object into a dict
result_on_members_dict = result_on_members_instance.to_dict()
# create an instance of ResultOnMembers from a dict
result_on_members_from_dict = ResultOnMembers.from_dict(result_on_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


