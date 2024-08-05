# ConnectionConcreteBlockDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**depth** | **float** |  | [optional] 
**material** | **str** |  | [optional] 
**center** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**outline_points** | [**List[Geometry2DPoint2DIdeaRSOpenModel]**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**region** | **str** |  | [optional] 
**original_model_id** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_concrete_block_data_idea_rs_open_model import ConnectionConcreteBlockDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConcreteBlockDataIdeaRSOpenModel from a JSON string
connection_concrete_block_data_idea_rs_open_model_instance = ConnectionConcreteBlockDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionConcreteBlockDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_concrete_block_data_idea_rs_open_model_dict = connection_concrete_block_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionConcreteBlockDataIdeaRSOpenModel from a dict
connection_concrete_block_data_idea_rs_open_model_from_dict = ConnectionConcreteBlockDataIdeaRSOpenModel.from_dict(connection_concrete_block_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


