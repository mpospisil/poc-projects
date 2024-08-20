# ConnectionPlateDataIdeaRSOpenModel

Provides data of the single plate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the plate | [optional] 
**thickness** | **float** | Thickness of the plate | [optional] 
**material** | **str** | Name of the material | [optional] 
**outline_points** | [**List[Geometry2DPoint2DIdeaRSOpenModel]**](Geometry2DPoint2DIdeaRSOpenModel.md) | Outline points | [optional] 
**origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**region** | **str** | Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry | [optional] 
**geometry** | [**Geometry2DRegion2DIdeaRSOpenModel**](Geometry2DRegion2DIdeaRSOpenModel.md) |  | [optional] 
**original_model_id** | **str** | Get or set the identification in the original model  In the case of the imported connection from another application | [optional] 
**is_negative_object** | **bool** | Is negative object | [optional] 
**id** | **int** | Element Id | [optional] 

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


