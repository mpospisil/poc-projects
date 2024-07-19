# IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**thickness** | **float** |  | [optional] 
**material** | **str** |  | [optional] 
**outline_points** | [**List[IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel]**](IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**origin** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**region** | **str** |  | [optional] 
**geometry** | [**IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel**](IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel.md) |  | [optional] 
**original_model_id** | **str** |  | [optional] 
**is_negative_object** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_plate_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_plate_data_idea_rs_open_model_dict = idea_rs_open_model_connection_plate_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_plate_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_plate_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


