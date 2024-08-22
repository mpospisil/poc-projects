# ConTypology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearing_member** | [**BearingMemberData**](BearingMemberData.md) |  | [optional] 
**connected_members** | [**List[ConnectedMemberData]**](ConnectedMemberData.md) |  | [optional] 
**typology_code** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_typology import ConTypology

# TODO update the JSON string below
json = "{}"
# create an instance of ConTypology from a JSON string
con_typology_instance = ConTypology.from_json(json)
# print the JSON string representation of the object
print(ConTypology.to_json())

# convert the object into a dict
con_typology_dict = con_typology_instance.to_dict()
# create an instance of ConTypology from a dict
con_typology_from_dict = ConTypology.from_dict(con_typology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


