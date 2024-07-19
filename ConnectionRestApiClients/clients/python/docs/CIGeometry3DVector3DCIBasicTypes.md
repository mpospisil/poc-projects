# CIGeometry3DVector3DCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction_x** | **float** |  | [optional] 
**direction_y** | **float** |  | [optional] 
**direction_z** | **float** |  | [optional] 
**normalize** | [**CIGeometry3DVector3DCIBasicTypes**](CIGeometry3DVector3DCIBasicTypes.md) |  | [optional] 
**magnitude** | **float** |  | [optional] [readonly] 
**magnitude_squared** | **float** |  | [optional] [readonly] 

## Example

```python
from connection-restapi-client-poc.models.ci_geometry3_d_vector3_dci_basic_types import CIGeometry3DVector3DCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CIGeometry3DVector3DCIBasicTypes from a JSON string
ci_geometry3_d_vector3_dci_basic_types_instance = CIGeometry3DVector3DCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(CIGeometry3DVector3DCIBasicTypes.to_json())

# convert the object into a dict
ci_geometry3_d_vector3_dci_basic_types_dict = ci_geometry3_d_vector3_dci_basic_types_instance.to_dict()
# create an instance of CIGeometry3DVector3DCIBasicTypes from a dict
ci_geometry3_d_vector3_dci_basic_types_from_dict = CIGeometry3DVector3DCIBasicTypes.from_dict(ci_geometry3_d_vector3_dci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


