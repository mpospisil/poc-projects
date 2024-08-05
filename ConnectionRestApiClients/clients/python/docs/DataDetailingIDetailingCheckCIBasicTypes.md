# DataDetailingIDetailingCheckCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_value** | **float** |  | [optional] 
**detailing_check_category** | [**DataDetailingCheckCategoryCIBasicTypes**](DataDetailingCheckCategoryCIBasicTypes.md) |  | [optional] 
**detailing_check_type** | [**DataDetailingCheckTypeCIBasicTypes**](DataDetailingCheckTypeCIBasicTypes.md) |  | [optional] 
**message_params** | **List[float]** |  | [optional] 
**target_element_id** | **int** |  | [optional] 
**target_element_name** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.data_detailing_i_detailing_check_ci_basic_types import DataDetailingIDetailingCheckCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DataDetailingIDetailingCheckCIBasicTypes from a JSON string
data_detailing_i_detailing_check_ci_basic_types_instance = DataDetailingIDetailingCheckCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(DataDetailingIDetailingCheckCIBasicTypes.to_json())

# convert the object into a dict
data_detailing_i_detailing_check_ci_basic_types_dict = data_detailing_i_detailing_check_ci_basic_types_instance.to_dict()
# create an instance of DataDetailingIDetailingCheckCIBasicTypes from a dict
data_detailing_i_detailing_check_ci_basic_types_from_dict = DataDetailingIDetailingCheckCIBasicTypes.from_dict(data_detailing_i_detailing_check_ci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


