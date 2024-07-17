# CIConnectionsDataDetailingIDetailingCheckCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_value** | **float** |  | [optional] 
**detailing_check_category** | [**IdeaStatiCaConnectionBasicTypesDataDetailingCheckCategoryCIBasicTypes**](IdeaStatiCaConnectionBasicTypesDataDetailingCheckCategoryCIBasicTypes.md) |  | [optional] 
**detailing_check_type** | [**IdeaStatiCaConnectionBasicTypesDataDetailingCheckTypeCIBasicTypes**](IdeaStatiCaConnectionBasicTypesDataDetailingCheckTypeCIBasicTypes.md) |  | [optional] 
**message_params** | **List[float]** |  | [optional] 
**target_element_id** | **int** |  | [optional] 
**target_element_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ci_connections_data_detailing_i_detailing_check_ci_basic_types import CIConnectionsDataDetailingIDetailingCheckCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CIConnectionsDataDetailingIDetailingCheckCIBasicTypes from a JSON string
ci_connections_data_detailing_i_detailing_check_ci_basic_types_instance = CIConnectionsDataDetailingIDetailingCheckCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(CIConnectionsDataDetailingIDetailingCheckCIBasicTypes.to_json())

# convert the object into a dict
ci_connections_data_detailing_i_detailing_check_ci_basic_types_dict = ci_connections_data_detailing_i_detailing_check_ci_basic_types_instance.to_dict()
# create an instance of CIConnectionsDataDetailingIDetailingCheckCIBasicTypes from a dict
ci_connections_data_detailing_i_detailing_check_ci_basic_types_from_dict = CIConnectionsDataDetailingIDetailingCheckCIBasicTypes.from_dict(ci_connections_data_detailing_i_detailing_check_ci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


