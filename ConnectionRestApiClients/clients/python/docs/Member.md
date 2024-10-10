# Member

Member identification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_type** | [**MemberType**](MemberType.md) |  | [optional] 
**id** | **int** | Id of member | [optional] 

## Example

```python
from ideastatica_connection_api.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print(Member.to_json())

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_from_dict = Member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


