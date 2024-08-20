# ConnectionCutBeamByBeamDataIdeaRSOpenModel

Provides data of the cut objec by object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the cut | [optional] 
**modified_object** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**cutting_object** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**is_weld** | **bool** | is cut welded | [optional] 
**weld_thickness** | **float** | Thickness of the weld - value 0 &#x3D; recommended size | [optional] 
**weld_type** | [**ConnectionWeldTypeIdeaRSOpenModel**](ConnectionWeldTypeIdeaRSOpenModel.md) |  | [optional] 
**offset** | **float** | Offset | [optional] 
**method** | [**ConnectionCutMethodIdeaRSOpenModel**](ConnectionCutMethodIdeaRSOpenModel.md) |  | [optional] 
**orientation** | [**ConnectionCutOrientationIdeaRSOpenModel**](ConnectionCutOrientationIdeaRSOpenModel.md) |  | [optional] 
**plane_on_cutting_object** | [**ConnectionDistanceComparisonIdeaRSOpenModel**](ConnectionDistanceComparisonIdeaRSOpenModel.md) |  | [optional] 
**cut_part** | [**ConnectionCutPartIdeaRSOpenModel**](ConnectionCutPartIdeaRSOpenModel.md) |  | [optional] 
**extend_before_cut** | **bool** | Extend before cut - for cuts where user can decide if modified beam will be extended or not | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_cut_beam_by_beam_data_idea_rs_open_model import ConnectionCutBeamByBeamDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCutBeamByBeamDataIdeaRSOpenModel from a JSON string
connection_cut_beam_by_beam_data_idea_rs_open_model_instance = ConnectionCutBeamByBeamDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCutBeamByBeamDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_cut_beam_by_beam_data_idea_rs_open_model_dict = connection_cut_beam_by_beam_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCutBeamByBeamDataIdeaRSOpenModel from a dict
connection_cut_beam_by_beam_data_idea_rs_open_model_from_dict = ConnectionCutBeamByBeamDataIdeaRSOpenModel.from_dict(connection_cut_beam_by_beam_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


