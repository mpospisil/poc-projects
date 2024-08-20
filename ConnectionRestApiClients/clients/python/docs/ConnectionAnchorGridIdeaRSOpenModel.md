# ConnectionAnchorGridIdeaRSOpenModel

Data of the anchor grid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_block** | [**ConnectionConcreteBlockIdeaRSOpenModel**](ConnectionConcreteBlockIdeaRSOpenModel.md) |  | [optional] 
**anchor_type** | [**ParametersAnchorTypeIdeaRSOpenModel**](ParametersAnchorTypeIdeaRSOpenModel.md) |  | [optional] 
**washer_size** | **float** | Washer Size used if AnchorType is washer | [optional] 
**bolt_assembly_ref** | **str** |  | [optional] 
**id** | **int** | Unique Id of the bolt grid | [optional] 
**is_anchor** | **bool** | Is Anchor | [optional] 
**anchor_len** | **float** | Anchor lenght | [optional] 
**hole_diameter** | **float** | The diameter of the hole | [optional] 
**diameter** | **float** | The diameter of bolt | [optional] 
**head_diameter** | **float** | The head diameter of bolt | [optional] 
**diagonal_head_diameter** | **float** | The Diagonal Head Diameter of bolt | [optional] 
**head_height** | **float** | The Head Height of bolt | [optional] 
**bore_hole** | **float** | The BoreHole of bolt | [optional] 
**tensile_stress_area** | **float** | The Tensile Stress Area of bolt | [optional] 
**nut_thickness** | **float** | The Nut Thickness of bolt | [optional] 
**bolt_assembly_name** | **str** | The description of the bolt assembly | [optional] 
**standard** | **str** | The standard of the bolt assembly | [optional] 
**material** | **str** | The material of the bolt assembly | [optional] 
**origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**axis_x** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_y** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**axis_z** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**positions** | [**List[Geometry3DPoint3DIdeaRSOpenModel]**](Geometry3DPoint3DIdeaRSOpenModel.md) | Positions of holes in the local coodinate system of the bolt grid | [optional] 
**connected_plates** | **List[int]** | Identifiers of the connected plates | [optional] 
**connected_part_ids** | **List[str]** | Id of the weld | [optional] 
**shear_in_thread** | **bool** | Indicates, whether a shear plane is in the thread of a bolt. | [optional] 
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


