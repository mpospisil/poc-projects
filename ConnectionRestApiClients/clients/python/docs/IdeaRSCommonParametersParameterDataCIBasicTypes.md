# IdeaRSCommonParametersParameterDataCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parameter_type** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**default_value** | **object** |  | [optional] 
**evaluated_value** | **object** |  | [optional] 
**evaluated_default_value** | **object** |  | [optional] 
**validation_value** | **str** |  | [optional] 
**evaluated_validation_value** | **str** |  | [optional] 
**validation_type** | [**IdeaRSCommonParametersValidationTypeCIBasicTypes**](IdeaRSCommonParametersValidationTypeCIBasicTypes.md) |  | [optional] 
**user_unit_id** | **int** |  | [optional] 
**is_visible_for_simple_connection** | **bool** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_rs_common_parameters_parameter_data_ci_basic_types import IdeaRSCommonParametersParameterDataCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSCommonParametersParameterDataCIBasicTypes from a JSON string
idea_rs_common_parameters_parameter_data_ci_basic_types_instance = IdeaRSCommonParametersParameterDataCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(IdeaRSCommonParametersParameterDataCIBasicTypes.to_json())

# convert the object into a dict
idea_rs_common_parameters_parameter_data_ci_basic_types_dict = idea_rs_common_parameters_parameter_data_ci_basic_types_instance.to_dict()
# create an instance of IdeaRSCommonParametersParameterDataCIBasicTypes from a dict
idea_rs_common_parameters_parameter_data_ci_basic_types_from_dict = IdeaRSCommonParametersParameterDataCIBasicTypes.from_dict(idea_rs_common_parameters_parameter_data_ci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


