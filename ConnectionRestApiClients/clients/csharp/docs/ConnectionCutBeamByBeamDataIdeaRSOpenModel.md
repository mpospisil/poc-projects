# connection_restapi_client_poc.Model.ConnectionCutBeamByBeamDataIdeaRSOpenModel
Provides data of the cut objec by object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the cut | [optional] 
**ModifiedObject** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**CuttingObject** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**IsWeld** | **bool** | is cut welded | [optional] 
**WeldThickness** | **double** | Thickness of the weld - value 0 &#x3D; recommended size | [optional] 
**WeldType** | **ConnectionWeldTypeIdeaRSOpenModel** |  | [optional] 
**Offset** | **double** | Offset | [optional] 
**Method** | **ConnectionCutMethodIdeaRSOpenModel** |  | [optional] 
**Orientation** | **ConnectionCutOrientationIdeaRSOpenModel** |  | [optional] 
**PlaneOnCuttingObject** | **ConnectionDistanceComparisonIdeaRSOpenModel** |  | [optional] 
**CutPart** | **ConnectionCutPartIdeaRSOpenModel** |  | [optional] 
**ExtendBeforeCut** | **bool** | Extend before cut - for cuts where user can decide if modified beam will be extended or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

