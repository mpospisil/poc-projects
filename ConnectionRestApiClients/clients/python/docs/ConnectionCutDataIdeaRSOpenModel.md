# ConnectionCutDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plane_point** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**normal_vector** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**direction** | [**ConnectionCutOrientationIdeaRSOpenModel**](ConnectionCutOrientationIdeaRSOpenModel.md) |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_cut_data_idea_rs_open_model import ConnectionCutDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCutDataIdeaRSOpenModel from a JSON string
connection_cut_data_idea_rs_open_model_instance = ConnectionCutDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCutDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_cut_data_idea_rs_open_model_dict = connection_cut_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCutDataIdeaRSOpenModel from a dict
connection_cut_data_idea_rs_open_model_from_dict = ConnectionCutDataIdeaRSOpenModel.from_dict(connection_cut_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


