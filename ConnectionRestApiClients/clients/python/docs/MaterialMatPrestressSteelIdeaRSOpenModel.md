# MaterialMatPrestressSteelIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diameter** | **float** |  | [optional] 
**area** | **float** |  | [optional] 
**number_of_wires** | **int** |  | [optional] 
**equivalent_diameter** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**load_from_library** | **bool** |  | [optional] 
**e** | **float** |  | [optional] 
**g** | **float** |  | [optional] 
**poisson** | **float** |  | [optional] 
**unit_mass** | **float** |  | [optional] 
**specific_heat** | **float** |  | [optional] 
**thermal_expansion** | **float** |  | [optional] 
**thermal_conductivity** | **float** |  | [optional] 
**is_default_material** | **bool** |  | [optional] 
**order_in_code** | **int** |  | [optional] 
**state_of_thermal_expansion** | [**MaterialThermalExpansionStateIdeaRSOpenModel**](MaterialThermalExpansionStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_conductivity** | [**MaterialThermalConductivityStateIdeaRSOpenModel**](MaterialThermalConductivityStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_specific_heat** | [**MaterialThermalSpecificHeatStateIdeaRSOpenModel**](MaterialThermalSpecificHeatStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_stress_strain** | [**MaterialThermalStressStrainStateIdeaRSOpenModel**](MaterialThermalStressStrainStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_strain** | [**MaterialThermalStrainStateIdeaRSOpenModel**](MaterialThermalStrainStateIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_specific_heat_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_conductivity_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_expansion_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_strain_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_stress_strain_curvature** | [**List[Geometry2DTemperatureCurve2DIdeaRSOpenModel]**](Geometry2DTemperatureCurve2DIdeaRSOpenModel.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.material_mat_prestress_steel_idea_rs_open_model import MaterialMatPrestressSteelIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialMatPrestressSteelIdeaRSOpenModel from a JSON string
material_mat_prestress_steel_idea_rs_open_model_instance = MaterialMatPrestressSteelIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(MaterialMatPrestressSteelIdeaRSOpenModel.to_json())

# convert the object into a dict
material_mat_prestress_steel_idea_rs_open_model_dict = material_mat_prestress_steel_idea_rs_open_model_instance.to_dict()
# create an instance of MaterialMatPrestressSteelIdeaRSOpenModel from a dict
material_mat_prestress_steel_idea_rs_open_model_from_dict = MaterialMatPrestressSteelIdeaRSOpenModel.from_dict(material_mat_prestress_steel_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


