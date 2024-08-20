# CrossSectionTendonBarIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tendon_type** | [**CrossSectionTendonBarTypeIdeaRSOpenModel**](CrossSectionTendonBarTypeIdeaRSOpenModel.md) |  | [optional] 
**point** | [**Geometry2DPoint2DIdeaRSOpenModel**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**material** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**prestressing_order** | **int** |  | [optional] 
**num_strands_in_tendon** | **int** |  | [optional] 
**prestress_reinforcement_type** | [**CrossSectionFatigueTypeOfPrestressingSteelIdeaRSOpenModel**](CrossSectionFatigueTypeOfPrestressingSteelIdeaRSOpenModel.md) |  | [optional] 
**phase** | **int** |  | [optional] 
**tendon_duct** | [**CrossSectionTendonDuctIdeaRSOpenModel**](CrossSectionTendonDuctIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cross_section_tendon_bar_idea_rs_open_model import CrossSectionTendonBarIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of CrossSectionTendonBarIdeaRSOpenModel from a JSON string
cross_section_tendon_bar_idea_rs_open_model_instance = CrossSectionTendonBarIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(CrossSectionTendonBarIdeaRSOpenModel.to_json())

# convert the object into a dict
cross_section_tendon_bar_idea_rs_open_model_dict = cross_section_tendon_bar_idea_rs_open_model_instance.to_dict()
# create an instance of CrossSectionTendonBarIdeaRSOpenModel from a dict
cross_section_tendon_bar_idea_rs_open_model_from_dict = CrossSectionTendonBarIdeaRSOpenModel.from_dict(cross_section_tendon_bar_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


