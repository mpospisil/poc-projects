# CrossSectionStirrupIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**Geometry2DPolyLine2DIdeaRSOpenModel**](Geometry2DPolyLine2DIdeaRSOpenModel.md) |  | [optional] 
**diameter** | **float** |  | [optional] 
**material** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**anchorage_lenght** | **float** |  | [optional] 
**diameter_of_mandrel** | **float** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**distance** | **float** |  | [optional] 
**shear_check** | **bool** |  | [optional] 
**torsion_check** | **bool** |  | [optional] 

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


