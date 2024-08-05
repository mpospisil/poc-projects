# ConnectionAnchorGridIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_block** | [**ConnectionConcreteBlockIdeaRSOpenModel**](ConnectionConcreteBlockIdeaRSOpenModel.md) |  | [optional] 
**anchor_type** | [**ParametersAnchorTypeIdeaRSOpenModel**](ParametersAnchorTypeIdeaRSOpenModel.md) |  | [optional] 
**washer_size** | **float** |  | [optional] 
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
**origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**positions** | [**List[Geometry3DPoint3DIdeaRSOpenModel]**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**connected_plates** | **List[int]** |  | [optional] 
**connected_part_ids** | **List[str]** |  | [optional] 
**shear_in_thread** | **bool** |  | [optional] 
**bolt_interaction** | [**ParametersBoltShearTypeIdeaRSOpenModel**](ParametersBoltShearTypeIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_anchor_grid_idea_rs_open_model import ConnectionAnchorGridIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionAnchorGridIdeaRSOpenModel from a JSON string
connection_anchor_grid_idea_rs_open_model_instance = ConnectionAnchorGridIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionAnchorGridIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_anchor_grid_idea_rs_open_model_dict = connection_anchor_grid_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionAnchorGridIdeaRSOpenModel from a dict
connection_anchor_grid_idea_rs_open_model_from_dict = ConnectionAnchorGridIdeaRSOpenModel.from_dict(connection_anchor_grid_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


