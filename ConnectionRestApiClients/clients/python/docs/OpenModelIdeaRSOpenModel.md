# OpenModelIdeaRSOpenModel

Open model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Data format version | [optional] 
**origin_settings** | **object** | OriginProject | [optional] 
**point3_d** | [**List[Geometry3DPoint3DIdeaRSOpenModel]**](Geometry3DPoint3DIdeaRSOpenModel.md) | List of Point3D | [optional] 
**line_segment3_d** | [**List[Geometry3DLineSegment3DIdeaRSOpenModel]**](Geometry3DLineSegment3DIdeaRSOpenModel.md) | List of LineSegment3D | [optional] 
**arc_segment3_d** | [**List[Geometry3DArcSegment3DIdeaRSOpenModel]**](Geometry3DArcSegment3DIdeaRSOpenModel.md) | List of ArcSegment3D | [optional] 
**poly_line3_d** | [**List[Geometry3DPolyLine3DIdeaRSOpenModel]**](Geometry3DPolyLine3DIdeaRSOpenModel.md) | List of PolyLine3D | [optional] 
**region3_d** | [**List[Geometry3DRegion3DIdeaRSOpenModel]**](Geometry3DRegion3DIdeaRSOpenModel.md) | List of Region3D | [optional] 
**mat_concrete** | [**List[MaterialMatConcreteIdeaRSOpenModel]**](MaterialMatConcreteIdeaRSOpenModel.md) | List of MatConcrete | [optional] 
**mat_reinforcement** | [**List[MaterialMatReinforcementIdeaRSOpenModel]**](MaterialMatReinforcementIdeaRSOpenModel.md) | List of MatReinforcement | [optional] 
**mat_steel** | [**List[MaterialMatSteelIdeaRSOpenModel]**](MaterialMatSteelIdeaRSOpenModel.md) | List of MatSteel | [optional] 
**mat_prestress_steel** | [**List[MaterialMatPrestressSteelIdeaRSOpenModel]**](MaterialMatPrestressSteelIdeaRSOpenModel.md) | List of MatPrestressSteel | [optional] 
**mat_welding** | [**List[MaterialMatWeldingIdeaRSOpenModel]**](MaterialMatWeldingIdeaRSOpenModel.md) | List of MatWelding | [optional] 
**cross_section** | [**List[CrossSectionCrossSectionIdeaRSOpenModel]**](CrossSectionCrossSectionIdeaRSOpenModel.md) | List of CrossSection | [optional] 
**reinforced_cross_section** | [**List[CrossSectionReinforcedCrossSectionIdeaRSOpenModel]**](CrossSectionReinforcedCrossSectionIdeaRSOpenModel.md) | List of Reinforced CrossSection | [optional] 
**hinge_element1_d** | [**List[ModelHingeElement1DIdeaRSOpenModel]**](ModelHingeElement1DIdeaRSOpenModel.md) | List of hinge elements 1D | [optional] 
**opening** | [**List[DetailOpeningIdeaRSOpenModel]**](DetailOpeningIdeaRSOpenModel.md) | List of openings for Detail | [optional] 
**dapped_end** | [**List[DetailDappedEndIdeaRSOpenModel]**](DetailDappedEndIdeaRSOpenModel.md) | List of dapped ends in Detail | [optional] 
**patch_device** | [**List[DetailPatchDeviceIdeaRSOpenModel]**](DetailPatchDeviceIdeaRSOpenModel.md) | List of dapped ends in Detail | [optional] 
**element1_d** | [**List[ModelElement1DIdeaRSOpenModel]**](ModelElement1DIdeaRSOpenModel.md) | List of Elements 1D | [optional] 
**beam** | [**List[DetailBeamIdeaRSOpenModel]**](DetailBeamIdeaRSOpenModel.md) | List of Elements 1D | [optional] 
**member1_d** | [**List[ModelMember1DIdeaRSOpenModel]**](ModelMember1DIdeaRSOpenModel.md) | List of Member 1D | [optional] 
**element2_d** | [**List[ModelElement2DIdeaRSOpenModel]**](ModelElement2DIdeaRSOpenModel.md) | List of Elements 2D | [optional] 
**wall** | [**List[DetailWallIdeaRSOpenModel]**](DetailWallIdeaRSOpenModel.md) | List of Elements 2D | [optional] 
**member2_d** | [**List[ModelMember2DIdeaRSOpenModel]**](ModelMember2DIdeaRSOpenModel.md) | List of Member 2D | [optional] 
**rigid_link** | [**List[ModelRigidLinkIdeaRSOpenModel]**](ModelRigidLinkIdeaRSOpenModel.md) | List of Rigid link | [optional] 
**point_on_line3_d** | [**List[Geometry3DPointOnLine3DIdeaRSOpenModel]**](Geometry3DPointOnLine3DIdeaRSOpenModel.md) | List of Point on line 3D | [optional] 
**point_support_node** | [**List[ModelPointSupportNodeIdeaRSOpenModel]**](ModelPointSupportNodeIdeaRSOpenModel.md) | List of Point support in node | [optional] 
**line_support_segment** | [**List[ModelLineSupportSegmentIdeaRSOpenModel]**](ModelLineSupportSegmentIdeaRSOpenModel.md) | List of Line support on segment | [optional] 
**loads_in_point** | [**List[LoadingLoadInPointIdeaRSOpenModel]**](LoadingLoadInPointIdeaRSOpenModel.md) | List of point load impulses in this load case | [optional] 
**loads_on_line** | [**List[LoadingLoadOnLineIdeaRSOpenModel]**](LoadingLoadOnLineIdeaRSOpenModel.md) | List of line load impulses in this load case | [optional] 
**strain_loads_on_line** | [**List[LoadingStrainLoadOnLineIdeaRSOpenModel]**](LoadingStrainLoadOnLineIdeaRSOpenModel.md) | List of generalized strain load impulses along the line in this load case. | [optional] 
**point_loads_on_line** | [**List[LoadingPointLoadOnLineIdeaRSOpenModel]**](LoadingPointLoadOnLineIdeaRSOpenModel.md) | List of point load impulses in this load case | [optional] 
**loads_on_surface** | [**List[LoadingLoadOnSurfaceIdeaRSOpenModel]**](LoadingLoadOnSurfaceIdeaRSOpenModel.md) | List surafce load in this load case | [optional] 
**settlements** | [**List[LoadingSettlementIdeaRSOpenModel]**](LoadingSettlementIdeaRSOpenModel.md) | Settlements in this load case | [optional] 
**temperature_loads_on_line** | [**List[LoadingTemperatureLoadOnLineIdeaRSOpenModel]**](LoadingTemperatureLoadOnLineIdeaRSOpenModel.md) | List of temperature load in this load case | [optional] 
**load_group** | [**List[LoadingLoadGroupIdeaRSOpenModel]**](LoadingLoadGroupIdeaRSOpenModel.md) | List of Load groups | [optional] 
**load_case** | [**List[LoadingLoadCaseIdeaRSOpenModel]**](LoadingLoadCaseIdeaRSOpenModel.md) | List of Load cases | [optional] 
**combi_input** | [**List[LoadingCombiInputIdeaRSOpenModel]**](LoadingCombiInputIdeaRSOpenModel.md) | List of Combinations | [optional] 
**attribute** | **List[object]** | List of attributes | [optional] 
**connection_point** | [**List[ConnectionConnectionPointIdeaRSOpenModel]**](ConnectionConnectionPointIdeaRSOpenModel.md) | List of Connection Points | [optional] 
**connections** | [**List[ConnectionConnectionDataIdeaRSOpenModel]**](ConnectionConnectionDataIdeaRSOpenModel.md) | List of Connection data | [optional] 
**reinforcement** | [**List[DetailReinforcementIdeaRSOpenModel]**](DetailReinforcementIdeaRSOpenModel.md) | List of reinforcement in IDEA StatiCa Detail | [optional] 
**isd_model** | [**List[DetailISDModelIdeaRSOpenModel]**](DetailISDModelIdeaRSOpenModel.md) | List of Details | [optional] 
**initial_imperfection_of_point** | [**List[ModelInitialImperfectionOfPointIdeaRSOpenModel]**](ModelInitialImperfectionOfPointIdeaRSOpenModel.md) | List of InitialmperfectionOfPoint | [optional] 
**tendon** | [**List[ModelTendonIdeaRSOpenModel]**](ModelTendonIdeaRSOpenModel.md) | Tendon | [optional] 
**result_class** | [**List[LoadingResultClassIdeaRSOpenModel]**](LoadingResultClassIdeaRSOpenModel.md) | Result Class | [optional] 
**design_member** | [**List[ModelDesignMemberIdeaRSOpenModel]**](ModelDesignMemberIdeaRSOpenModel.md) | Design Member | [optional] 
**sub_structure** | [**List[ModelSubStructureIdeaRSOpenModel]**](ModelSubStructureIdeaRSOpenModel.md) | Design Member | [optional] 
**connection_setup** | [**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md) |  | [optional] 
**project_data** | **object** | Defines certain data about user project. | [optional] 
**check_member** | [**List[ModelCheckMemberIdeaRSOpenModel]**](ModelCheckMemberIdeaRSOpenModel.md) | List of the Check members | [optional] 
**concrete_check_section** | [**List[ConcreteCheckSectionIdeaRSOpenModel]**](ConcreteCheckSectionIdeaRSOpenModel.md) | List of the concrete check section | [optional] 
**concrete_setup** | [**ConcreteConcreteSetupIdeaRSOpenModel**](ConcreteConcreteSetupIdeaRSOpenModel.md) |  | [optional] 
**project_data_concrete** | **object** | Project data concrete | [optional] 
**rebar_shape** | [**List[ModelRebarShapeIdeaRSOpenModel]**](ModelRebarShapeIdeaRSOpenModel.md) | Gets or sets the rebars shapes | [optional] 
**rebar_general** | [**List[ModelRebarGeneralIdeaRSOpenModel]**](ModelRebarGeneralIdeaRSOpenModel.md) | Gets or sets the rebar General collection | [optional] 
**rebar_single** | [**List[ModelRebarSingleIdeaRSOpenModel]**](ModelRebarSingleIdeaRSOpenModel.md) | Gets or sets the rebar single collection | [optional] 
**rebar_stirrups** | [**List[ModelRebarStirrupsIdeaRSOpenModel]**](ModelRebarStirrupsIdeaRSOpenModel.md) | Gets or sets the rebar group (stirrups) collection | [optional] 
**taper** | [**List[ModelTaperIdeaRSOpenModel]**](ModelTaperIdeaRSOpenModel.md) |  | [optional] 
**span** | [**List[ModelSpanIdeaRSOpenModel]**](ModelSpanIdeaRSOpenModel.md) |  | [optional] 
**solid_blocks3_d** | [**List[DetailSolidBlock3DIdeaRSOpenModel]**](DetailSolidBlock3DIdeaRSOpenModel.md) | List of Solid Blocks 3D | [optional] 
**surface_supports3_d** | [**List[DetailSurfaceSupport3DIdeaRSOpenModel]**](DetailSurfaceSupport3DIdeaRSOpenModel.md) | List of Surface Supports 3D | [optional] 
**base_plates3_d** | [**List[DetailBasePlate3DIdeaRSOpenModel]**](DetailBasePlate3DIdeaRSOpenModel.md) | List of Base Plates 3D | [optional] 
**anchors3_d** | [**List[DetailAnchor3DIdeaRSOpenModel]**](DetailAnchor3DIdeaRSOpenModel.md) | List of Anchors 3D | [optional] 
**detail_load_case** | [**List[DetailLoadingDetailLoadCaseIdeaRSOpenModel]**](DetailLoadingDetailLoadCaseIdeaRSOpenModel.md) | List of Load cases | [optional] 
**detail_combination** | [**List[DetailLoadingDetailCombinationIdeaRSOpenModel]**](DetailLoadingDetailCombinationIdeaRSOpenModel.md) | List of Combinations | [optional] 

## Example

```python
from connection_restapi_client_poc.models.open_model_idea_rs_open_model import OpenModelIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of OpenModelIdeaRSOpenModel from a JSON string
open_model_idea_rs_open_model_instance = OpenModelIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(OpenModelIdeaRSOpenModel.to_json())

# convert the object into a dict
open_model_idea_rs_open_model_dict = open_model_idea_rs_open_model_instance.to_dict()
# create an instance of OpenModelIdeaRSOpenModel from a dict
open_model_idea_rs_open_model_from_dict = OpenModelIdeaRSOpenModel.from_dict(open_model_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


