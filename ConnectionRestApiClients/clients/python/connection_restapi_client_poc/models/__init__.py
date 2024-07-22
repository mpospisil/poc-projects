# coding: utf-8

# flake8: noqa
"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from connection_restapi_client_poc.models.ci_connections_data_auto_design_bolt_coordinate_system_ci_basic_types import CIConnectionsDataAutoDesignBoltCoordinateSystemCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_auto_design_internal_shear_forces_ci_basic_types import CIConnectionsDataAutoDesignInternalShearForcesCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_auto_design_shear_forces_in_shear_planes_ci_basic_types import CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_bolt_ci_basic_types import CIConnectionsDataDetailingDetailingChecksBoltCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_pin_ci_basic_types import CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_weld_ci_basic_types import CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes
from connection_restapi_client_poc.models.ci_connections_data_detailing_i_detailing_check_ci_basic_types import CIConnectionsDataDetailingIDetailingCheckCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_poly_line2_dci_basic_types import CIGeometry2DIPolyLine2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_region2_dci_basic_types import CIGeometry2DIRegion2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_segment2_dci_basic_types import CIGeometry2DISegment2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_d_ida_com_point2_dci_basic_types import CIGeometry2DIdaComPoint2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry3_d_vector3_dci_basic_types import CIGeometry3DVector3DCIBasicTypes
from connection_restapi_client_poc.models.cigi_cl2_d_path2_d_segment_ci_geometry2_d import CIGiCL2DPath2DSegmentCIGeometry2D
from connection_restapi_client_poc.models.cigi_cl2_d_point2_dci_geometry2_d import CIGiCL2DPoint2DCIGeometry2D
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_analysis_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInAnalysisCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_base_plate_shear_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_bolt_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_buckling_check_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBucklingCheckDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_check_results_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_bolt_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemBoltIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_steel_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemSteelIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_weld_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemWeldIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_fatigue_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_load_effect_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInLoadEffectDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_pin_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_plate_check_local_deformation_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_project_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInProjectCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_stiffness_chek_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInStiffnessChekDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_stiffness_chek_data_load_component_idea_stati_ca_connection_checks import ConModelerConnectionPlugInStiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_summary_check_res_data_context_idea_stati_ca_connection_checks import ConModelerConnectionPlugInSummaryCheckResDataContextIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_summary_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInSummaryCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_summary_check_res_data_message_context_idea_stati_ca_connection_checks import ConModelerConnectionPlugInSummaryCheckResDataMessageContextIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_weld_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_weld_data_load_level_idea_stati_ca_connection_checks import ConModelerConnectionPlugInWeldDataLoadLevelIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.idea_rs_common_parameters_parameter_data_ci_basic_types import IdeaRSCommonParametersParameterDataCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_common_parameters_validation_type_ci_basic_types import IdeaRSCommonParametersValidationTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connection_calculator_fire_design_fire_temperature_calculation_data_idea_rs_connection_calculator import IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator
from connection_restapi_client_poc.models.idea_rs_connections_data_anchor_type_ci_basic_types import IdeaRSConnectionsDataAnchorTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_base_plate_contact_type_ci_basic_types import IdeaRSConnectionsDataBasePlateContactTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_bolt_shear_type_ci_basic_types import IdeaRSConnectionsDataBoltShearTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_e_purpose_idea_rs_connections import IdeaRSConnectionsDataEPurposeIdeaRSConnections
from connection_restapi_client_poc.models.idea_rs_connections_data_shear_force_transfer_methods_ci_basic_types import IdeaRSConnectionsDataShearForceTransferMethodsCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_thin_plate_validity_ci_basic_types import IdeaRSConnectionsDataThinPlateValidityCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_thin_plate_validity_criterion_ci_basic_types import IdeaRSConnectionsDataThinPlateValidityCriterionCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_weld_type_code_ci_basic_types import IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_open_model_concrete_check_section_idea_rs_open_model import IdeaRSOpenModelConcreteCheckSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_concrete_concrete_setup_idea_rs_open_model import IdeaRSOpenModelConcreteConcreteSetupIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_cone_breakout_check_type_idea_rs_open_model import IdeaRSOpenModelConeBreakoutCheckTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_anchor_grid_idea_rs_open_model import IdeaRSOpenModelConnectionAnchorGridIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_beam_data_idea_rs_open_model import IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_bend_data_idea_rs_open_model import IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_bolt_grid_idea_rs_open_model import IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_buckling_res_idea_rs_open_model import IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_anchor_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_bolt_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_concrete_block_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_plate_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_summary_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_weld_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model import IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_idea_rs_open_model import IdeaRSOpenModelConnectionConcreteBlockIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_connection_check_res_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_connection_data_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_connection_point_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionPointIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_method_idea_rs_open_model import IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_orientation_idea_rs_open_model import IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_part_idea_rs_open_model import IdeaRSOpenModelConnectionCutPartIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_distance_comparison_idea_rs_open_model import IdeaRSOpenModelConnectionDistanceComparisonIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_folded_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_weld_data_idea_rs_open_model import IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_weld_type_idea_rs_open_model import IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_cross_section_cross_section_idea_rs_open_model import IdeaRSOpenModelCrossSectionCrossSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_cross_section_reinforced_cross_section_idea_rs_open_model import IdeaRSOpenModelCrossSectionReinforcedCrossSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_crt_comp_check_is_idea_rs_open_model import IdeaRSOpenModelCrtCompCheckISIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_anchor3_d_idea_rs_open_model import IdeaRSOpenModelDetailAnchor3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_base_plate3_d_idea_rs_open_model import IdeaRSOpenModelDetailBasePlate3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_beam_idea_rs_open_model import IdeaRSOpenModelDetailBeamIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_dapped_end_idea_rs_open_model import IdeaRSOpenModelDetailDappedEndIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_isd_model_idea_rs_open_model import IdeaRSOpenModelDetailISDModelIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_loading_detail_combination_idea_rs_open_model import IdeaRSOpenModelDetailLoadingDetailCombinationIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_loading_detail_load_case_idea_rs_open_model import IdeaRSOpenModelDetailLoadingDetailLoadCaseIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_opening_idea_rs_open_model import IdeaRSOpenModelDetailOpeningIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_patch_device_idea_rs_open_model import IdeaRSOpenModelDetailPatchDeviceIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_reinforcement_idea_rs_open_model import IdeaRSOpenModelDetailReinforcementIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_solid_block3_d_idea_rs_open_model import IdeaRSOpenModelDetailSolidBlock3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_surface_support3_d_idea_rs_open_model import IdeaRSOpenModelDetailSurfaceSupport3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_detail_wall_idea_rs_open_model import IdeaRSOpenModelDetailWallIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DPolyLine2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_arc_segment3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DArcSegment3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_line_segment3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DLineSegment3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point_on_line3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPointOnLine3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_poly_line3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPolyLine3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_region3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DRegion3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_combi_input_idea_rs_open_model import IdeaRSOpenModelLoadingCombiInputIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_load_case_idea_rs_open_model import IdeaRSOpenModelLoadingLoadCaseIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_load_group_idea_rs_open_model import IdeaRSOpenModelLoadingLoadGroupIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_load_in_point_idea_rs_open_model import IdeaRSOpenModelLoadingLoadInPointIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_load_on_line_idea_rs_open_model import IdeaRSOpenModelLoadingLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_load_on_surface_idea_rs_open_model import IdeaRSOpenModelLoadingLoadOnSurfaceIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_point_load_on_line_idea_rs_open_model import IdeaRSOpenModelLoadingPointLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_result_class_idea_rs_open_model import IdeaRSOpenModelLoadingResultClassIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_settlement_idea_rs_open_model import IdeaRSOpenModelLoadingSettlementIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_strain_load_on_line_idea_rs_open_model import IdeaRSOpenModelLoadingStrainLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_loading_temperature_load_on_line_idea_rs_open_model import IdeaRSOpenModelLoadingTemperatureLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_material_mat_concrete_idea_rs_open_model import IdeaRSOpenModelMaterialMatConcreteIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_material_mat_prestress_steel_idea_rs_open_model import IdeaRSOpenModelMaterialMatPrestressSteelIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_material_mat_reinforcement_idea_rs_open_model import IdeaRSOpenModelMaterialMatReinforcementIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_material_mat_steel_idea_rs_open_model import IdeaRSOpenModelMaterialMatSteelIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_material_mat_welding_idea_rs_open_model import IdeaRSOpenModelMaterialMatWeldingIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_message_message_number_idea_rs_open_model import IdeaRSOpenModelMessageMessageNumberIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_message_open_message_idea_rs_open_model import IdeaRSOpenModelMessageOpenMessageIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_message_open_messages_idea_rs_open_model import IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_check_member_idea_rs_open_model import IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_design_member_idea_rs_open_model import IdeaRSOpenModelModelDesignMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_element1_d_idea_rs_open_model import IdeaRSOpenModelModelElement1DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_element2_d_idea_rs_open_model import IdeaRSOpenModelModelElement2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_hinge_element1_d_idea_rs_open_model import IdeaRSOpenModelModelHingeElement1DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_initial_imperfection_of_point_idea_rs_open_model import IdeaRSOpenModelModelInitialImperfectionOfPointIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_line_support_segment_idea_rs_open_model import IdeaRSOpenModelModelLineSupportSegmentIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_member1_d_idea_rs_open_model import IdeaRSOpenModelModelMember1DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_member2_d_idea_rs_open_model import IdeaRSOpenModelModelMember2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_point_support_node_idea_rs_open_model import IdeaRSOpenModelModelPointSupportNodeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_rebar_general_idea_rs_open_model import IdeaRSOpenModelModelRebarGeneralIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_rebar_shape_idea_rs_open_model import IdeaRSOpenModelModelRebarShapeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_rebar_single_idea_rs_open_model import IdeaRSOpenModelModelRebarSingleIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_rebar_stirrups_idea_rs_open_model import IdeaRSOpenModelModelRebarStirrupsIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_rigid_link_idea_rs_open_model import IdeaRSOpenModelModelRigidLinkIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_span_idea_rs_open_model import IdeaRSOpenModelModelSpanIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_sub_structure_idea_rs_open_model import IdeaRSOpenModelModelSubStructureIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_taper_idea_rs_open_model import IdeaRSOpenModelModelTaperIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_model_tendon_idea_rs_open_model import IdeaRSOpenModelModelTendonIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_open_element_id_idea_rs_open_model import IdeaRSOpenModelOpenElementIdIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_open_model_container_idea_rs_open_model import IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_open_model_idea_rs_open_model import IdeaRSOpenModelOpenModelIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_parameters_anchor_type_idea_rs_open_model import IdeaRSOpenModelParametersAnchorTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_parameters_bolt_shear_type_idea_rs_open_model import IdeaRSOpenModelParametersBoltShearTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model import IdeaRSOpenModelReferenceElementIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_loading_idea_rs_open_model import IdeaRSOpenModelResultLoadingIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_loading_type_idea_rs_open_model import IdeaRSOpenModelResultLoadingTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_member_idea_rs_open_model import IdeaRSOpenModelResultMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_member_type_idea_rs_open_model import IdeaRSOpenModelResultMemberTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_open_model_result_idea_rs_open_model import IdeaRSOpenModelResultOpenModelResultIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_result_local_system_type_idea_rs_open_model import IdeaRSOpenModelResultResultLocalSystemTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_result_on_member_idea_rs_open_model import IdeaRSOpenModelResultResultOnMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_result_on_members_idea_rs_open_model import IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_result_type_idea_rs_open_model import IdeaRSOpenModelResultResultTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_weld_evaluation_idea_rs_open_model import IdeaRSOpenModelWeldEvaluationIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_american_subcode_ci_basic_types import IdeaRSWsLibCssServiceAmericanSubcodeCIBasicTypes
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_code_type_ci_basic_types import IdeaRSWsLibCssServiceCodeTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_anchor_tensile_calculation_ausci_basic_types import IdeaStatiCaConnectionBasicTypesDataAnchorTensileCalculationAUSCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_check_outcome_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataCheckOutcomeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_cone_breakout_check_type_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataConeBreakoutCheckTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_crt_comp_check_isci_basic_types import IdeaStatiCaConnectionBasicTypesDataCrtCompCheckISCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_detailing_check_category_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataDetailingCheckCategoryCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_detailing_check_type_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataDetailingCheckTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_thread_type_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataThreadTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_weld_check_method_hkci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldCheckMethodHKCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_weld_position_snipci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldPositionSNIPCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_welding_type_snipci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldingTypeSNIPCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_analysis_type_enum_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_member_load_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectMemberLoadIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_position_enum_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectPositionEnumIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_section_load_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectSectionLoadIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_missing_weld_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_operation_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConOperationIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_production_cost_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConProductionCostIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_data_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_result_con_result_summary_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_settings_con_loading_options_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelSettingsConLoadingOptionsIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_base_template_conversion_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateBaseTemplateConversionIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_con_template_apply_param_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_con_template_mapping_get_param_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateMappingGetParamIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_selected_element_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_table_container_type_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateTableContainerTypeIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_template_conversions_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin
from connection_restapi_client_poc.models.microsoft_asp_net_core_mvc_ok_object_result_microsoft_asp_net_core_mvc_core import MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore
from connection_restapi_client_poc.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
