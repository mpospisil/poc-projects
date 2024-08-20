# MaterialMatPrestressSteelIdeaRSOpenModel

Material prestressing steel base class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diameter** | **float** | Diameter | [optional] 
**area** | **float** | Area | [optional] 
**number_of_wires** | **int** | number of wires in strand | [optional] 
**equivalent_diameter** | **float** | Equivalent diameter | [optional] 
**name** | **str** | Name of material | [optional] 
**load_from_library** | **bool** | Load from library - try override properties from library find material by name | [optional] 
**e** | **float** | Young&#39;s modulus | [optional] 
**g** | **float** | Shear modulus | [optional] 
**poisson** | **float** | Poisson&#39;s ratio | [optional] 
**unit_mass** | **float** | Unit weight | [optional] 
**specific_heat** | **float** | Specific heat capacity | [optional] 
**thermal_expansion** | **float** | Thermal expansion | [optional] 
**thermal_conductivity** | **float** | Thermal conductivity | [optional] 
**is_default_material** | **bool** | True if material is default material from the code | [optional] 
**order_in_code** | **int** | Order of this material in the code | [optional] 
**state_of_thermal_expansion** | [**MaterialThermalExpansionStateIdeaRSOpenModel**](MaterialThermalExpansionStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_conductivity** | [**MaterialThermalConductivityStateIdeaRSOpenModel**](MaterialThermalConductivityStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_specific_heat** | [**MaterialThermalSpecificHeatStateIdeaRSOpenModel**](MaterialThermalSpecificHeatStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_stress_strain** | [**MaterialThermalStressStrainStateIdeaRSOpenModel**](MaterialThermalStressStrainStateIdeaRSOpenModel.md) |  | [optional] 
**state_of_thermal_strain** | [**MaterialThermalStrainStateIdeaRSOpenModel**](MaterialThermalStrainStateIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_specific_heat_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_conductivity_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_expansion_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_strain_curvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**user_thermal_stress_strain_curvature** | [**List[Geometry2DTemperatureCurve2DIdeaRSOpenModel]**](Geometry2DTemperatureCurve2DIdeaRSOpenModel.md) | User-defined curvature for thermal stress,strain { Temperature &#x3D; Θ[K], {x &#x3D; ε[-], y &#x3D; σ[Pa]}} | [optional] 
**id** | **int** | Element Id | [optional] 

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


