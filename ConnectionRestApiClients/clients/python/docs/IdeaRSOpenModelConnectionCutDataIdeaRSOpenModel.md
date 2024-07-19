# IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plane_point** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**normal_vector** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**direction** | [**IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel**](IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel.md) |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from connection-restapi-client-poc.models.idea_rs_open_model_connection_cut_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_cut_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_cut_data_idea_rs_open_model_dict = idea_rs_open_model_connection_cut_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_cut_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_cut_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


