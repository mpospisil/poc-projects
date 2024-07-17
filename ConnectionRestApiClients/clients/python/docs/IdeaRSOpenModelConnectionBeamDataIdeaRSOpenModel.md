# IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**plates** | [**List[IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.md) |  | [optional] 
**cross_section_type** | **str** |  | [optional] 
**mprl_name** | **str** |  | [optional] 
**original_model_id** | **str** |  | [optional] 
**cuts** | [**List[IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel.md) |  | [optional] 
**is_added** | **bool** |  | [optional] 
**added_member_length** | **float** |  | [optional] 
**is_negative_object** | **bool** |  | [optional] 
**added_member** | [**IdeaRSOpenModelReferenceElementIdeaRSOpenModel**](IdeaRSOpenModelReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**mirror_y** | **bool** |  | [optional] 
**ref_line_in_center_of_gravity** | **bool** |  | [optional] 
**is_bearing_member** | **bool** |  | [optional] 
**auto_add_cut_by_workplane** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.idea_rs_open_model_connection_beam_data_idea_rs_open_model import IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_beam_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_beam_data_idea_rs_open_model_dict = idea_rs_open_model_connection_beam_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_beam_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_beam_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


