# CrossSectionStirrupIdeaRSOpenModel

Stirrup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**Geometry2DPolyLine2DIdeaRSOpenModel**](Geometry2DPolyLine2DIdeaRSOpenModel.md) |  | [optional] 
**diameter** | **float** | Diameter | [optional] 
**material** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**anchorage_lenght** | **float** | Anchorage Lenght | [optional] 
**diameter_of_mandrel** | **float** | Radius of stirrup mandrel - refering to stirrup axis | [optional] 
**is_closed** | **bool** | Open / Closed stirrup | [optional] 
**distance** | **float** | Longitudinal distance between stirrups | [optional] 
**shear_check** | **bool** | Status of shear check, not possible for detailing stirrup | [optional] 
**torsion_check** | **bool** | Status of torsion check, not possible for detailing stirrup | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cross_section_stirrup_idea_rs_open_model import CrossSectionStirrupIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of CrossSectionStirrupIdeaRSOpenModel from a JSON string
cross_section_stirrup_idea_rs_open_model_instance = CrossSectionStirrupIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(CrossSectionStirrupIdeaRSOpenModel.to_json())

# convert the object into a dict
cross_section_stirrup_idea_rs_open_model_dict = cross_section_stirrup_idea_rs_open_model_instance.to_dict()
# create an instance of CrossSectionStirrupIdeaRSOpenModel from a dict
cross_section_stirrup_idea_rs_open_model_from_dict = CrossSectionStirrupIdeaRSOpenModel.from_dict(cross_section_stirrup_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


