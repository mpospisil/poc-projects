# IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plate1_id** | **int** |  | [optional] 
**plate2_id** | **int** |  | [optional] 
**radius** | **float** |  | [optional] 
**point1_of_side_boundary1** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**point2_of_side_boundary1** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**end_face_normal1** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**point1_of_side_boundary2** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**point2_of_side_boundary2** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_rs_open_model_connection_bend_data_idea_rs_open_model import IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_bend_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_bend_data_idea_rs_open_model_dict = idea_rs_open_model_connection_bend_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_bend_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_bend_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


