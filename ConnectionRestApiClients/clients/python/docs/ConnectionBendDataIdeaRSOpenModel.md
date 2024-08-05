# ConnectionBendDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plate1_id** | **int** |  | [optional] 
**plate2_id** | **int** |  | [optional] 
**radius** | **float** |  | [optional] 
**point1_of_side_boundary1** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**point2_of_side_boundary1** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**end_face_normal1** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**point1_of_side_boundary2** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**point2_of_side_boundary2** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_bend_data_idea_rs_open_model import ConnectionBendDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionBendDataIdeaRSOpenModel from a JSON string
connection_bend_data_idea_rs_open_model_instance = ConnectionBendDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionBendDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_bend_data_idea_rs_open_model_dict = connection_bend_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionBendDataIdeaRSOpenModel from a dict
connection_bend_data_idea_rs_open_model_from_dict = ConnectionBendDataIdeaRSOpenModel.from_dict(connection_bend_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


