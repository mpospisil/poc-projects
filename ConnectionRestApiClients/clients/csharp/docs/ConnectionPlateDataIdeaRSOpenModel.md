# connection_restapi_client_poc.Model.ConnectionPlateDataIdeaRSOpenModel
Provides data of the single plate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the plate | [optional] 
**Thickness** | **double** | Thickness of the plate | [optional] 
**Material** | **string** | Name of the material | [optional] 
**OutlinePoints** | [**List&lt;Geometry2DPoint2DIdeaRSOpenModel&gt;**](Geometry2DPoint2DIdeaRSOpenModel.md) | Outline points | [optional] 
**Origin** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**AxisX** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**AxisY** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**AxisZ** | [**Geometry3DVector3DIdeaRSOpenModel**](Geometry3DVector3DIdeaRSOpenModel.md) |  | [optional] 
**Region** | **string** | Geometry of the plate in svg format. In next version will be mark as OBSOLETE! New use property Geometry | [optional] 
**Geometry** | [**Geometry2DRegion2DIdeaRSOpenModel**](Geometry2DRegion2DIdeaRSOpenModel.md) |  | [optional] 
**OriginalModelId** | **string** | Get or set the identification in the original model  In the case of the imported connection from another application | [optional] 
**IsNegativeObject** | **bool** | Is negative object | [optional] 
**Id** | **int** | Element Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

