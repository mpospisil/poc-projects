# CrossSectionReinforcedBarIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**Geometry2DPoint2DIdeaRSOpenModel**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**diameter** | **float** |  | [optional] 
**material** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cross_section_reinforced_bar_idea_rs_open_model import CrossSectionReinforcedBarIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of CrossSectionReinforcedBarIdeaRSOpenModel from a JSON string
cross_section_reinforced_bar_idea_rs_open_model_instance = CrossSectionReinforcedBarIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(CrossSectionReinforcedBarIdeaRSOpenModel.to_json())

# convert the object into a dict
cross_section_reinforced_bar_idea_rs_open_model_dict = cross_section_reinforced_bar_idea_rs_open_model_instance.to_dict()
# create an instance of CrossSectionReinforcedBarIdeaRSOpenModel from a dict
cross_section_reinforced_bar_idea_rs_open_model_from_dict = CrossSectionReinforcedBarIdeaRSOpenModel.from_dict(cross_section_reinforced_bar_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


