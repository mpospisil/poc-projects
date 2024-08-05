# ConnectionPlateDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**thickness** | **float** |  | [optional] 
**material** | **str** |  | [optional] 
**outline_points** | [**List[Geometry2DPoint2DIdeaRSOpenModel]**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**region** | **str** |  | [optional] 
**geometry** | [**Geometry2DRegion2DIdeaRSOpenModel**](Geometry2DRegion2DIdeaRSOpenModel.md) |  | [optional] 
**original_model_id** | **str** |  | [optional] 
**is_negative_object** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_plate_data_idea_rs_open_model import ConnectionPlateDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPlateDataIdeaRSOpenModel from a JSON string
connection_plate_data_idea_rs_open_model_instance = ConnectionPlateDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionPlateDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_plate_data_idea_rs_open_model_dict = connection_plate_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionPlateDataIdeaRSOpenModel from a dict
connection_plate_data_idea_rs_open_model_from_dict = ConnectionPlateDataIdeaRSOpenModel.from_dict(connection_plate_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


