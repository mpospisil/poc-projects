# CIGeometry2DIPolyLine2DCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_point** | [**CIGeometry2DIdaComPoint2DCIBasicTypes**](CIGeometry2DIdaComPoint2DCIBasicTypes.md) |  | [optional] 
**is_closed** | **bool** |  | [optional] [readonly] 
**segments** | [**List[CIGeometry2DISegment2DCIBasicTypes]**](CIGeometry2DISegment2DCIBasicTypes.md) |  | [optional] [readonly] 
**length** | **float** |  | [optional] [readonly] 
**bounds** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ci_geometry2_di_poly_line2_dci_basic_types import CIGeometry2DIPolyLine2DCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CIGeometry2DIPolyLine2DCIBasicTypes from a JSON string
ci_geometry2_di_poly_line2_dci_basic_types_instance = CIGeometry2DIPolyLine2DCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(CIGeometry2DIPolyLine2DCIBasicTypes.to_json())

# convert the object into a dict
ci_geometry2_di_poly_line2_dci_basic_types_dict = ci_geometry2_di_poly_line2_dci_basic_types_instance.to_dict()
# create an instance of CIGeometry2DIPolyLine2DCIBasicTypes from a dict
ci_geometry2_di_poly_line2_dci_basic_types_from_dict = CIGeometry2DIPolyLine2DCIBasicTypes.from_dict(ci_geometry2_di_poly_line2_dci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


