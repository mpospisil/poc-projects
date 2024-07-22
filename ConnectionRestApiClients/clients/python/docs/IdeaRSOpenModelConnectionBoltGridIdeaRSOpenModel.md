# IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bolt_assembly_ref** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_anchor** | **bool** |  | [optional] 
**anchor_len** | **float** |  | [optional] 
**hole_diameter** | **float** |  | [optional] 
**diameter** | **float** |  | [optional] 
**head_diameter** | **float** |  | [optional] 
**diagonal_head_diameter** | **float** |  | [optional] 
**head_height** | **float** |  | [optional] 
**bore_hole** | **float** |  | [optional] 
**tensile_stress_area** | **float** |  | [optional] 
**nut_thickness** | **float** |  | [optional] 
**bolt_assembly_name** | **str** |  | [optional] 
**standard** | **str** |  | [optional] 
**material** | **str** |  | [optional] 
**origin** | [**IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel**](IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**positions** | [**List[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel]**](IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**connected_plates** | **List[int]** |  | [optional] 
**connected_part_ids** | **List[str]** |  | [optional] 
**shear_in_thread** | **bool** |  | [optional] 
**bolt_interaction** | [**IdeaRSOpenModelParametersBoltShearTypeIdeaRSOpenModel**](IdeaRSOpenModelParametersBoltShearTypeIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_rs_open_model_connection_bolt_grid_idea_rs_open_model import IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_bolt_grid_idea_rs_open_model_instance = IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_bolt_grid_idea_rs_open_model_dict = idea_rs_open_model_connection_bolt_grid_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel from a dict
idea_rs_open_model_connection_bolt_grid_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_bolt_grid_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

