# DataThinPlateValidityCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_plate_name** | **str** |  | [optional] 
**validity_criteria** | [**List[DataThinPlateValidityCriterionCIBasicTypes]**](DataThinPlateValidityCriterionCIBasicTypes.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.data_thin_plate_validity_ci_basic_types import DataThinPlateValidityCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DataThinPlateValidityCIBasicTypes from a JSON string
data_thin_plate_validity_ci_basic_types_instance = DataThinPlateValidityCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(DataThinPlateValidityCIBasicTypes.to_json())

# convert the object into a dict
data_thin_plate_validity_ci_basic_types_dict = data_thin_plate_validity_ci_basic_types_instance.to_dict()
# create an instance of DataThinPlateValidityCIBasicTypes from a dict
data_thin_plate_validity_ci_basic_types_from_dict = DataThinPlateValidityCIBasicTypes.from_dict(data_thin_plate_validity_ci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


