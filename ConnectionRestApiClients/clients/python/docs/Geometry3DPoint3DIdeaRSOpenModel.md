# Geometry3DPoint3DIdeaRSOpenModel

Represents an x- , y- an z-coordinates in three-dimensional space.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | Gets or sets the X-coordinate value | [optional] 
**y** | **float** | Gets or sets the Y-coordinate value | [optional] 
**z** | **float** | Gets or sets the Z-coordinate value | [optional] 
**id** | **int** | Element Id | [optional] 

## Example

```python
from connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model import Geometry3DPoint3DIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry3DPoint3DIdeaRSOpenModel from a JSON string
geometry3_d_point3_d_idea_rs_open_model_instance = Geometry3DPoint3DIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(Geometry3DPoint3DIdeaRSOpenModel.to_json())

# convert the object into a dict
geometry3_d_point3_d_idea_rs_open_model_dict = geometry3_d_point3_d_idea_rs_open_model_instance.to_dict()
# create an instance of Geometry3DPoint3DIdeaRSOpenModel from a dict
geometry3_d_point3_d_idea_rs_open_model_from_dict = Geometry3DPoint3DIdeaRSOpenModel.from_dict(geometry3_d_point3_d_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


