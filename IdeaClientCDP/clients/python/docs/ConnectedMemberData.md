# ConnectedMemberData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** |  | [optional] 
**typological_sector_code** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**lcs_rotatiton** | **float** |  | [optional] 
**continuity_type** | [**ContinuityType**](ContinuityType.md) |  | [optional] 
**css_meta_data** | [**CssData**](CssData.md) |  | [optional] 
**rigidity** | [**ConnectionRigidity**](ConnectionRigidity.md) |  | [optional] 
**dir_related_to_bearing** | [**ConnectionDirection**](ConnectionDirection.md) |  | [optional] 
**static_behaviour** | **int** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.connected_member_data import ConnectedMemberData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedMemberData from a JSON string
connected_member_data_instance = ConnectedMemberData.from_json(json)
# print the JSON string representation of the object
print(ConnectedMemberData.to_json())

# convert the object into a dict
connected_member_data_dict = connected_member_data_instance.to_dict()
# create an instance of ConnectedMemberData from a dict
connected_member_data_from_dict = ConnectedMemberData.from_dict(connected_member_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


