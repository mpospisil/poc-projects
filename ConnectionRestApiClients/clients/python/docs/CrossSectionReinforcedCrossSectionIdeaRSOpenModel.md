# CrossSectionReinforcedCrossSectionIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cross_section** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**bars** | [**List[CrossSectionReinforcedBarIdeaRSOpenModel]**](CrossSectionReinforcedBarIdeaRSOpenModel.md) |  | [optional] 
**stirrups** | [**List[CrossSectionStirrupIdeaRSOpenModel]**](CrossSectionStirrupIdeaRSOpenModel.md) |  | [optional] 
**tendon_bars** | [**List[CrossSectionTendonBarIdeaRSOpenModel]**](CrossSectionTendonBarIdeaRSOpenModel.md) |  | [optional] 
**tendon_ducts** | [**List[CrossSectionTendonDuctIdeaRSOpenModel]**](CrossSectionTendonDuctIdeaRSOpenModel.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cross_section_reinforced_cross_section_idea_rs_open_model import CrossSectionReinforcedCrossSectionIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of CrossSectionReinforcedCrossSectionIdeaRSOpenModel from a JSON string
cross_section_reinforced_cross_section_idea_rs_open_model_instance = CrossSectionReinforcedCrossSectionIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(CrossSectionReinforcedCrossSectionIdeaRSOpenModel.to_json())

# convert the object into a dict
cross_section_reinforced_cross_section_idea_rs_open_model_dict = cross_section_reinforced_cross_section_idea_rs_open_model_instance.to_dict()
# create an instance of CrossSectionReinforcedCrossSectionIdeaRSOpenModel from a dict
cross_section_reinforced_cross_section_idea_rs_open_model_from_dict = CrossSectionReinforcedCrossSectionIdeaRSOpenModel.from_dict(cross_section_reinforced_cross_section_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


