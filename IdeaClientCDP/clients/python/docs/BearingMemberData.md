# BearingMemberData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**inclination** | **float** |  | [optional] 
**continuity_type** | [**ContinuityType**](ContinuityType.md) |  | [optional] 
**css_meta_data** | [**CssData**](CssData.md) |  | [optional] 
**rigidity** | [**ConnectionRigidity**](ConnectionRigidity.md) |  | [optional] 
**static_behaviour** | **int** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.bearing_member_data import BearingMemberData

# TODO update the JSON string below
json = "{}"
# create an instance of BearingMemberData from a JSON string
bearing_member_data_instance = BearingMemberData.from_json(json)
# print the JSON string representation of the object
print(BearingMemberData.to_json())

# convert the object into a dict
bearing_member_data_dict = bearing_member_data_instance.to_dict()
# create an instance of BearingMemberData from a dict
bearing_member_data_from_dict = BearingMemberData.from_dict(bearing_member_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


