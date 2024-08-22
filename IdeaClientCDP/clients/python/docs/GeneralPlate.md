# GeneralPlate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**general_plate_type** | [**GeneralPlateType**](GeneralPlateType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.general_plate import GeneralPlate

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralPlate from a JSON string
general_plate_instance = GeneralPlate.from_json(json)
# print the JSON string representation of the object
print(GeneralPlate.to_json())

# convert the object into a dict
general_plate_dict = general_plate_instance.to_dict()
# create an instance of GeneralPlate from a dict
general_plate_from_dict = GeneralPlate.from_dict(general_plate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


