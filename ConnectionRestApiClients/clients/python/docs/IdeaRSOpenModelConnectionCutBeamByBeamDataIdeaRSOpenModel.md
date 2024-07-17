# IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_object** | [**IdeaRSOpenModelReferenceElementIdeaRSOpenModel**](IdeaRSOpenModelReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**cutting_object** | [**IdeaRSOpenModelReferenceElementIdeaRSOpenModel**](IdeaRSOpenModelReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**is_weld** | **bool** |  | [optional] 
**weld_thickness** | **float** |  | [optional] 
**weld_type** | [**IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel**](IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel.md) |  | [optional] 
**offset** | **float** |  | [optional] 
**method** | [**IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel**](IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel.md) |  | [optional] 
**orientation** | [**IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel**](IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel.md) |  | [optional] 
**plane_on_cutting_object** | [**IdeaRSOpenModelConnectionDistanceComparisonIdeaRSOpenModel**](IdeaRSOpenModelConnectionDistanceComparisonIdeaRSOpenModel.md) |  | [optional] 
**cut_part** | [**IdeaRSOpenModelConnectionCutPartIdeaRSOpenModel**](IdeaRSOpenModelConnectionCutPartIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model_dict = idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


