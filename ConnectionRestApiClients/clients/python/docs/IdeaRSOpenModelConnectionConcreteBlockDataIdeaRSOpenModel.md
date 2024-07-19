# IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**depth** | **float** |  | [optional] 
**material** | **str** |  | [optional] 
**center** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**outline_points** | [**List[IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel]**](IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**origin** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**region** | **str** |  | [optional] 
**original_model_id** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model import IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model_dict = idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


