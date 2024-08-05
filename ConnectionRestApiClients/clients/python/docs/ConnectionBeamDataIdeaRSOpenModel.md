# ConnectionBeamDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**plates** | [**List[ConnectionPlateDataIdeaRSOpenModel]**](ConnectionPlateDataIdeaRSOpenModel.md) |  | [optional] 
**cross_section_type** | **str** |  | [optional] 
**mprl_name** | **str** |  | [optional] 
**original_model_id** | **str** |  | [optional] 
**cuts** | [**List[ConnectionCutDataIdeaRSOpenModel]**](ConnectionCutDataIdeaRSOpenModel.md) |  | [optional] 
**is_added** | **bool** |  | [optional] 
**added_member_length** | **float** |  | [optional] 
**is_negative_object** | **bool** |  | [optional] 
**added_member** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**mirror_y** | **bool** |  | [optional] 
**ref_line_in_center_of_gravity** | **bool** |  | [optional] 
**is_bearing_member** | **bool** |  | [optional] 
**auto_add_cut_by_workplane** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_beam_data_idea_rs_open_model import ConnectionBeamDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionBeamDataIdeaRSOpenModel from a JSON string
connection_beam_data_idea_rs_open_model_instance = ConnectionBeamDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionBeamDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_beam_data_idea_rs_open_model_dict = connection_beam_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionBeamDataIdeaRSOpenModel from a dict
connection_beam_data_idea_rs_open_model_from_dict = ConnectionBeamDataIdeaRSOpenModel.from_dict(connection_beam_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


