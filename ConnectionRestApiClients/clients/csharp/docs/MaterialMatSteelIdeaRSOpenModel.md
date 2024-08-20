# connection_restapi_client_poc.Model.MaterialMatSteelIdeaRSOpenModel
Material steel base class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of material | [optional] 
**LoadFromLibrary** | **bool** | Load from library - try override properties from library find material by name | [optional] 
**E** | **double** | Young&#39;s modulus | [optional] 
**G** | **double** | Shear modulus | [optional] 
**Poisson** | **double** | Poisson&#39;s ratio | [optional] 
**UnitMass** | **double** | Unit weight | [optional] 
**SpecificHeat** | **double** | Specific heat capacity | [optional] 
**ThermalExpansion** | **double** | Thermal expansion | [optional] 
**ThermalConductivity** | **double** | Thermal conductivity | [optional] 
**IsDefaultMaterial** | **bool** | True if material is default material from the code | [optional] 
**OrderInCode** | **int** | Order of this material in the code | [optional] 
**StateOfThermalExpansion** | **MaterialThermalExpansionStateIdeaRSOpenModel** |  | [optional] 
**StateOfThermalConductivity** | **MaterialThermalConductivityStateIdeaRSOpenModel** |  | [optional] 
**StateOfThermalSpecificHeat** | **MaterialThermalSpecificHeatStateIdeaRSOpenModel** |  | [optional] 
**StateOfThermalStressStrain** | **MaterialThermalStressStrainStateIdeaRSOpenModel** |  | [optional] 
**StateOfThermalStrain** | **MaterialThermalStrainStateIdeaRSOpenModel** |  | [optional] 
**UserThermalSpecificHeatCurvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**UserThermalConductivityCurvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**UserThermalExpansionCurvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**UserThermalStrainCurvature** | [**Geometry2DPolygon2DIdeaRSOpenModel**](Geometry2DPolygon2DIdeaRSOpenModel.md) |  | [optional] 
**UserThermalStressStrainCurvature** | [**List&lt;Geometry2DTemperatureCurve2DIdeaRSOpenModel&gt;**](Geometry2DTemperatureCurve2DIdeaRSOpenModel.md) | User-defined curvature for thermal stress,strain { Temperature &#x3D; Θ[K], {x &#x3D; ε[-], y &#x3D; σ[Pa]}} | [optional] 
**Id** | **int** | Element Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

