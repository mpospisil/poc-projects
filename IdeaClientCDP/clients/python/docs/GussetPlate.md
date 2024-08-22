# GussetPlate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**gusset_plate_type** | [**MaterialType**](MaterialType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.gusset_plate import GussetPlate

# TODO update the JSON string below
json = "{}"
# create an instance of GussetPlate from a JSON string
gusset_plate_instance = GussetPlate.from_json(json)
# print the JSON string representation of the object
print(GussetPlate.to_json())

# convert the object into a dict
gusset_plate_dict = gusset_plate_instance.to_dict()
# create an instance of GussetPlate from a dict
gusset_plate_from_dict = GussetPlate.from_dict(gusset_plate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


