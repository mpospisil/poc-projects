# ConMissingWeld


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_plate** | **str** |  | [optional] 
**surface_plate** | **str** |  | [optional] 
**edge_index** | **int** |  | [optional] 
**surface_index** | **int** |  | [optional] 
**weld_size** | **float** |  | [optional] 
**weld_type_code** | **str** |  | [optional] 
**weld_material_name** | **str** |  | [optional] 
**is_hollow_or_uncoiled_section** | **bool** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.con_missing_weld import ConMissingWeld

# TODO update the JSON string below
json = "{}"
# create an instance of ConMissingWeld from a JSON string
con_missing_weld_instance = ConMissingWeld.from_json(json)
# print the JSON string representation of the object
print(ConMissingWeld.to_json())

# convert the object into a dict
con_missing_weld_dict = con_missing_weld_instance.to_dict()
# create an instance of ConMissingWeld from a dict
con_missing_weld_from_dict = ConMissingWeld.from_dict(con_missing_weld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


