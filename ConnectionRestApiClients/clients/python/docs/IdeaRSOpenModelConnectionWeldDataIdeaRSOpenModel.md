# IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**thickness** | **float** |  | [optional] 
**material** | **str** |  | [optional] 
**weld_material** | [**IdeaRSOpenModelReferenceElementIdeaRSOpenModel**](IdeaRSOpenModelReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**weld_type** | [**IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel**](IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel.md) |  | [optional] 
**connected_part_ids** | **List[str]** |  | [optional] 
**start** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**end** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection-restapi-client-poc.models.idea_rs_open_model_connection_weld_data_idea_rs_open_model import IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_weld_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_weld_data_idea_rs_open_model_dict = idea_rs_open_model_connection_weld_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_weld_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_weld_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


