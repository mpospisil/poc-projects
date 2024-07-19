# CIGeometry2DIRegion2DCIBasicTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline** | [**CIGeometry2DIPolyLine2DCIBasicTypes**](CIGeometry2DIPolyLine2DCIBasicTypes.md) |  | [optional] 
**openings** | [**List[CIGeometry2DIPolyLine2DCIBasicTypes]**](CIGeometry2DIPolyLine2DCIBasicTypes.md) |  | [optional] 
**arc_discr_angle** | **float** |  | [optional] 

## Example

```python
from connection-restapi-client-poc.models.ci_geometry2_di_region2_dci_basic_types import CIGeometry2DIRegion2DCIBasicTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CIGeometry2DIRegion2DCIBasicTypes from a JSON string
ci_geometry2_di_region2_dci_basic_types_instance = CIGeometry2DIRegion2DCIBasicTypes.from_json(json)
# print the JSON string representation of the object
print(CIGeometry2DIRegion2DCIBasicTypes.to_json())

# convert the object into a dict
ci_geometry2_di_region2_dci_basic_types_dict = ci_geometry2_di_region2_dci_basic_types_instance.to_dict()
# create an instance of CIGeometry2DIRegion2DCIBasicTypes from a dict
ci_geometry2_di_region2_dci_basic_types_from_dict = CIGeometry2DIRegion2DCIBasicTypes.from_dict(ci_geometry2_di_region2_dci_basic_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


