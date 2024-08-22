# ConnectingPlate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**connecting_plate_type** | [**MaterialType**](MaterialType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.connecting_plate import ConnectingPlate

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectingPlate from a JSON string
connecting_plate_instance = ConnectingPlate.from_json(json)
# print the JSON string representation of the object
print(ConnectingPlate.to_json())

# convert the object into a dict
connecting_plate_dict = connecting_plate_instance.to_dict()
# create an instance of ConnectingPlate from a dict
connecting_plate_from_dict = ConnectingPlate.from_dict(connecting_plate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


