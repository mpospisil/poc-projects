# coding: utf-8

# flake8: noqa

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "24.0.5.0406"

# import apis into sdk package
from connection_restapi_client_poc.api.calculation_api import CalculationApi
from connection_restapi_client_poc.api.connection_api import ConnectionApi
from connection_restapi_client_poc.api.export_api import ExportApi
from connection_restapi_client_poc.api.load_effect_api import LoadEffectApi
from connection_restapi_client_poc.api.material_api import MaterialApi
from connection_restapi_client_poc.api.member_api import MemberApi
from connection_restapi_client_poc.api.parameter_api import ParameterApi
from connection_restapi_client_poc.api.project_api import ProjectApi
from connection_restapi_client_poc.api.template_api import TemplateApi

# import ApiClient
from connection_restapi_client_poc.api_response import ApiResponse
from connection_restapi_client_poc.api_client import ApiClient
from connection_restapi_client_poc.configuration import Configuration
from connection_restapi_client_poc.exceptions import OpenApiException
from connection_restapi_client_poc.exceptions import ApiTypeError
from connection_restapi_client_poc.exceptions import ApiValueError
from connection_restapi_client_poc.exceptions import ApiKeyError
from connection_restapi_client_poc.exceptions import ApiAttributeError
from connection_restapi_client_poc.exceptions import ApiException

# import models into sdk package
from connection_restapi_client_poc.models.analysis_check_res_data_idea_stati_ca_connection_checks import AnalysisCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.base_plate_shear_check_res_data_idea_stati_ca_connection_checks import BasePlateShearCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_idea_stati_ca_connection_checks import BoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_info_idea_stati_ca_connection_checks import BoltCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_timber_idea_stati_ca_connection_checks import BoltCheckResDataTimberIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.buckling_check_data_idea_stati_ca_connection_checks import BucklingCheckDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.ci_geometry2_di_poly_line2_dci_basic_types import CIGeometry2DIPolyLine2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_region2_dci_basic_types import CIGeometry2DIRegion2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_segment2_dci_basic_types import CIGeometry2DISegment2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_d_ida_com_point2_dci_basic_types import CIGeometry2DIdaComPoint2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry3_d_vector3_dci_basic_types import CIGeometry3DVector3DCIBasicTypes
from connection_restapi_client_poc.models.cigi_cl2_d_path2_d_segment_ci_geometry2_d import CIGiCL2DPath2DSegmentCIGeometry2D
from connection_restapi_client_poc.models.cigi_cl2_d_point2_dci_geometry2_d import CIGiCL2DPoint2DCIGeometry2D
from connection_restapi_client_poc.models.check_results_data_idea_stati_ca_connection_checks import CheckResultsDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.concrete_block_check_res_data_idea_stati_ca_connection_checks import ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.concrete_check_section_idea_rs_open_model import ConcreteCheckSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.concrete_concrete_setup_idea_rs_open_model import ConcreteConcreteSetupIdeaRSOpenModel
from connection_restapi_client_poc.models.cone_breakout_check_type_idea_rs_open_model import ConeBreakoutCheckTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_anchor_grid_idea_rs_open_model import ConnectionAnchorGridIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_beam_data_idea_rs_open_model import ConnectionBeamDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_bend_data_idea_rs_open_model import ConnectionBendDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_bolt_grid_idea_rs_open_model import ConnectionBoltGridIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_buckling_res_idea_rs_open_model import ConnectionBucklingResIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_anchor_idea_rs_open_model import ConnectionCheckResAnchorIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_bolt_idea_rs_open_model import ConnectionCheckResBoltIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_concrete_block_idea_rs_open_model import ConnectionCheckResConcreteBlockIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_plate_idea_rs_open_model import ConnectionCheckResPlateIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_summary_idea_rs_open_model import ConnectionCheckResSummaryIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_check_res_weld_idea_rs_open_model import ConnectionCheckResWeldIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_concrete_block_data_idea_rs_open_model import ConnectionConcreteBlockDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_concrete_block_idea_rs_open_model import ConnectionConcreteBlockIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_connection_check_res_idea_rs_open_model import ConnectionConnectionCheckResIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_connection_data_idea_rs_open_model import ConnectionConnectionDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_connection_point_idea_rs_open_model import ConnectionConnectionPointIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_cut_beam_by_beam_data_idea_rs_open_model import ConnectionCutBeamByBeamDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_cut_data_idea_rs_open_model import ConnectionCutDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_cut_method_idea_rs_open_model import ConnectionCutMethodIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_cut_orientation_idea_rs_open_model import ConnectionCutOrientationIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_cut_part_idea_rs_open_model import ConnectionCutPartIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_distance_comparison_idea_rs_open_model import ConnectionDistanceComparisonIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_folded_plate_data_idea_rs_open_model import ConnectionFoldedPlateDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_plate_data_idea_rs_open_model import ConnectionPlateDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_setup_idea_rs_open_model import ConnectionSetupIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_weld_data_idea_rs_open_model import ConnectionWeldDataIdeaRSOpenModel
from connection_restapi_client_poc.models.connection_weld_type_idea_rs_open_model import ConnectionWeldTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.cost_estimation_item_bolt_idea_stati_ca_connection_checks import CostEstimationItemBoltIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.cost_estimation_item_steel_idea_stati_ca_connection_checks import CostEstimationItemSteelIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.cost_estimation_item_weld_idea_stati_ca_connection_checks import CostEstimationItemWeldIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.cost_estimation_results_idea_stati_ca_connection_checks import CostEstimationResultsIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.cross_section_cross_section_idea_rs_open_model import CrossSectionCrossSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.cross_section_reinforced_cross_section_idea_rs_open_model import CrossSectionReinforcedCrossSectionIdeaRSOpenModel
from connection_restapi_client_poc.models.crt_comp_check_is_idea_rs_open_model import CrtCompCheckISIdeaRSOpenModel
from connection_restapi_client_poc.models.data_anchor_tensile_calculation_ausci_basic_types import DataAnchorTensileCalculationAUSCIBasicTypes
from connection_restapi_client_poc.models.data_anchor_type_ci_basic_types import DataAnchorTypeCIBasicTypes
from connection_restapi_client_poc.models.data_auto_design_bolt_coordinate_system_ci_basic_types import DataAutoDesignBoltCoordinateSystemCIBasicTypes
from connection_restapi_client_poc.models.data_auto_design_internal_shear_forces_ci_basic_types import DataAutoDesignInternalShearForcesCIBasicTypes
from connection_restapi_client_poc.models.data_auto_design_shear_forces_in_shear_planes_ci_basic_types import DataAutoDesignShearForcesInShearPlanesCIBasicTypes
from connection_restapi_client_poc.models.data_base_plate_contact_type_ci_basic_types import DataBasePlateContactTypeCIBasicTypes
from connection_restapi_client_poc.models.data_bolt_shear_type_ci_basic_types import DataBoltShearTypeCIBasicTypes
from connection_restapi_client_poc.models.data_check_outcome_ci_basic_types import DataCheckOutcomeCIBasicTypes
from connection_restapi_client_poc.models.data_cone_breakout_check_type_ci_basic_types import DataConeBreakoutCheckTypeCIBasicTypes
from connection_restapi_client_poc.models.data_crt_comp_check_isci_basic_types import DataCrtCompCheckISCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_check_category_ci_basic_types import DataDetailingCheckCategoryCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_check_type_ci_basic_types import DataDetailingCheckTypeCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_detailing_checks_bolt_ci_basic_types import DataDetailingDetailingChecksBoltCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_detailing_checks_pin_ci_basic_types import DataDetailingDetailingChecksPinCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_detailing_checks_weld_ci_basic_types import DataDetailingDetailingChecksWeldCIBasicTypes
from connection_restapi_client_poc.models.data_detailing_i_detailing_check_ci_basic_types import DataDetailingIDetailingCheckCIBasicTypes
from connection_restapi_client_poc.models.data_e_purpose_idea_rs_connections import DataEPurposeIdeaRSConnections
from connection_restapi_client_poc.models.data_shear_force_transfer_methods_ci_basic_types import DataShearForceTransferMethodsCIBasicTypes
from connection_restapi_client_poc.models.data_thin_plate_validity_ci_basic_types import DataThinPlateValidityCIBasicTypes
from connection_restapi_client_poc.models.data_thin_plate_validity_criterion_ci_basic_types import DataThinPlateValidityCriterionCIBasicTypes
from connection_restapi_client_poc.models.data_thread_type_ci_basic_types import DataThreadTypeCIBasicTypes
from connection_restapi_client_poc.models.data_weld_check_method_hkci_basic_types import DataWeldCheckMethodHKCIBasicTypes
from connection_restapi_client_poc.models.data_weld_position_snipci_basic_types import DataWeldPositionSNIPCIBasicTypes
from connection_restapi_client_poc.models.data_weld_type_code_ci_basic_types import DataWeldTypeCodeCIBasicTypes
from connection_restapi_client_poc.models.data_welding_type_snipci_basic_types import DataWeldingTypeSNIPCIBasicTypes
from connection_restapi_client_poc.models.detail_anchor3_d_idea_rs_open_model import DetailAnchor3DIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_base_plate3_d_idea_rs_open_model import DetailBasePlate3DIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_beam_idea_rs_open_model import DetailBeamIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_dapped_end_idea_rs_open_model import DetailDappedEndIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_isd_model_idea_rs_open_model import DetailISDModelIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_loading_detail_combination_idea_rs_open_model import DetailLoadingDetailCombinationIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_loading_detail_load_case_idea_rs_open_model import DetailLoadingDetailLoadCaseIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_opening_idea_rs_open_model import DetailOpeningIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_patch_device_idea_rs_open_model import DetailPatchDeviceIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_reinforcement_idea_rs_open_model import DetailReinforcementIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_solid_block3_d_idea_rs_open_model import DetailSolidBlock3DIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_surface_support3_d_idea_rs_open_model import DetailSurfaceSupport3DIdeaRSOpenModel
from connection_restapi_client_poc.models.detail_wall_idea_rs_open_model import DetailWallIdeaRSOpenModel
from connection_restapi_client_poc.models.fatigue_bolt_check_res_data_idea_stati_ca_connection_checks import FatigueBoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.fatigue_check_res_data_idea_stati_ca_connection_checks import FatigueCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.fire_temperature_calculation_data_idea_rs_connection_calculator import FireTemperatureCalculationDataIdeaRSConnectionCalculator
from connection_restapi_client_poc.models.geometry2_d_point2_d_idea_rs_open_model import Geometry2DPoint2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry2_d_poly_line2_d_idea_rs_open_model import Geometry2DPolyLine2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry2_d_region2_d_idea_rs_open_model import Geometry2DRegion2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry2_d_segment2_d_idea_rs_open_model import Geometry2DSegment2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_arc_segment3_d_idea_rs_open_model import Geometry3DArcSegment3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_line_segment3_d_idea_rs_open_model import Geometry3DLineSegment3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model import Geometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_point_on_line3_d_idea_rs_open_model import Geometry3DPointOnLine3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_poly_line3_d_idea_rs_open_model import Geometry3DPolyLine3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_region3_d_idea_rs_open_model import Geometry3DRegion3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_vector3_d_idea_rs_open_model import Geometry3DVector3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_common_parameters_parameter_data_ci_basic_types import IdeaRSCommonParametersParameterDataCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_common_parameters_validation_type_ci_basic_types import IdeaRSCommonParametersValidationTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_american_subcode_ci_basic_types import IdeaRSWsLibCssServiceAmericanSubcodeCIBasicTypes
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_code_type_ci_basic_types import IdeaRSWsLibCssServiceCodeTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_material_type_ci_basic_types import IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_base_template_conversion_idea_stati_ca_api import IdeaStatiCaApiConnectionModelBaseTemplateConversionIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_analysis_type_enum_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConAnalysisTypeEnumIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_member_load_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_position_enum_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectPositionEnumIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_section_load_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectSectionLoadIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_loading_options_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadingOptionsIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_member_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_missing_weld_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_operation_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_production_cost_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_data_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_result_summary_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_idea_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_idea_parameter_update_idea_stati_ca_api import IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_pin_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_selected_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelSelectedElementIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_table_container_type_idea_stati_ca_api import IdeaStatiCaApiConnectionModelTableContainerTypeIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_template_conversions_idea_stati_ca_api import IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi
from connection_restapi_client_poc.models.load_effect_data_idea_stati_ca_connection_checks import LoadEffectDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.loading_combi_input_idea_rs_open_model import LoadingCombiInputIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_load_case_idea_rs_open_model import LoadingLoadCaseIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_load_group_idea_rs_open_model import LoadingLoadGroupIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_load_in_point_idea_rs_open_model import LoadingLoadInPointIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_load_on_line_idea_rs_open_model import LoadingLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_load_on_surface_idea_rs_open_model import LoadingLoadOnSurfaceIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_point_load_on_line_idea_rs_open_model import LoadingPointLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_result_class_idea_rs_open_model import LoadingResultClassIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_settlement_idea_rs_open_model import LoadingSettlementIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_strain_load_on_line_idea_rs_open_model import LoadingStrainLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.loading_temperature_load_on_line_idea_rs_open_model import LoadingTemperatureLoadOnLineIdeaRSOpenModel
from connection_restapi_client_poc.models.material_mat_concrete_idea_rs_open_model import MaterialMatConcreteIdeaRSOpenModel
from connection_restapi_client_poc.models.material_mat_prestress_steel_idea_rs_open_model import MaterialMatPrestressSteelIdeaRSOpenModel
from connection_restapi_client_poc.models.material_mat_reinforcement_idea_rs_open_model import MaterialMatReinforcementIdeaRSOpenModel
from connection_restapi_client_poc.models.material_mat_steel_idea_rs_open_model import MaterialMatSteelIdeaRSOpenModel
from connection_restapi_client_poc.models.material_mat_welding_idea_rs_open_model import MaterialMatWeldingIdeaRSOpenModel
from connection_restapi_client_poc.models.message_message_number_idea_rs_open_model import MessageMessageNumberIdeaRSOpenModel
from connection_restapi_client_poc.models.message_open_message_idea_rs_open_model import MessageOpenMessageIdeaRSOpenModel
from connection_restapi_client_poc.models.message_open_messages_idea_rs_open_model import MessageOpenMessagesIdeaRSOpenModel
from connection_restapi_client_poc.models.microsoft_asp_net_core_mvc_ok_object_result_microsoft_asp_net_core_mvc_core import MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore
from connection_restapi_client_poc.models.model_check_member_idea_rs_open_model import ModelCheckMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.model_design_member_idea_rs_open_model import ModelDesignMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.model_element1_d_idea_rs_open_model import ModelElement1DIdeaRSOpenModel
from connection_restapi_client_poc.models.model_element2_d_idea_rs_open_model import ModelElement2DIdeaRSOpenModel
from connection_restapi_client_poc.models.model_hinge_element1_d_idea_rs_open_model import ModelHingeElement1DIdeaRSOpenModel
from connection_restapi_client_poc.models.model_initial_imperfection_of_point_idea_rs_open_model import ModelInitialImperfectionOfPointIdeaRSOpenModel
from connection_restapi_client_poc.models.model_line_support_segment_idea_rs_open_model import ModelLineSupportSegmentIdeaRSOpenModel
from connection_restapi_client_poc.models.model_member1_d_idea_rs_open_model import ModelMember1DIdeaRSOpenModel
from connection_restapi_client_poc.models.model_member2_d_idea_rs_open_model import ModelMember2DIdeaRSOpenModel
from connection_restapi_client_poc.models.model_point_support_node_idea_rs_open_model import ModelPointSupportNodeIdeaRSOpenModel
from connection_restapi_client_poc.models.model_rebar_general_idea_rs_open_model import ModelRebarGeneralIdeaRSOpenModel
from connection_restapi_client_poc.models.model_rebar_shape_idea_rs_open_model import ModelRebarShapeIdeaRSOpenModel
from connection_restapi_client_poc.models.model_rebar_single_idea_rs_open_model import ModelRebarSingleIdeaRSOpenModel
from connection_restapi_client_poc.models.model_rebar_stirrups_idea_rs_open_model import ModelRebarStirrupsIdeaRSOpenModel
from connection_restapi_client_poc.models.model_rigid_link_idea_rs_open_model import ModelRigidLinkIdeaRSOpenModel
from connection_restapi_client_poc.models.model_span_idea_rs_open_model import ModelSpanIdeaRSOpenModel
from connection_restapi_client_poc.models.model_sub_structure_idea_rs_open_model import ModelSubStructureIdeaRSOpenModel
from connection_restapi_client_poc.models.model_taper_idea_rs_open_model import ModelTaperIdeaRSOpenModel
from connection_restapi_client_poc.models.model_tendon_idea_rs_open_model import ModelTendonIdeaRSOpenModel
from connection_restapi_client_poc.models.open_element_id_idea_rs_open_model import OpenElementIdIdeaRSOpenModel
from connection_restapi_client_poc.models.open_model_container_idea_rs_open_model import OpenModelContainerIdeaRSOpenModel
from connection_restapi_client_poc.models.open_model_idea_rs_open_model import OpenModelIdeaRSOpenModel
from connection_restapi_client_poc.models.parameters_anchor_type_idea_rs_open_model import ParametersAnchorTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.parameters_bolt_shear_type_idea_rs_open_model import ParametersBoltShearTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.pin_check_res_data_idea_stati_ca_connection_checks import PinCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_local_deformation_idea_stati_ca_connection_checks import PlateCheckLocalDeformationIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_res_data_idea_stati_ca_connection_checks import PlateCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_res_data_info_idea_stati_ca_connection_checks import PlateCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.project_check_res_data_idea_stati_ca_connection_checks import ProjectCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.reference_element_idea_rs_open_model import ReferenceElementIdeaRSOpenModel
from connection_restapi_client_poc.models.result_loading_idea_rs_open_model import ResultLoadingIdeaRSOpenModel
from connection_restapi_client_poc.models.result_loading_type_idea_rs_open_model import ResultLoadingTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.result_member_idea_rs_open_model import ResultMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.result_member_type_idea_rs_open_model import ResultMemberTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.result_open_model_result_idea_rs_open_model import ResultOpenModelResultIdeaRSOpenModel
from connection_restapi_client_poc.models.result_result_local_system_type_idea_rs_open_model import ResultResultLocalSystemTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.result_result_on_member_idea_rs_open_model import ResultResultOnMemberIdeaRSOpenModel
from connection_restapi_client_poc.models.result_result_on_members_idea_rs_open_model import ResultResultOnMembersIdeaRSOpenModel
from connection_restapi_client_poc.models.result_result_type_idea_rs_open_model import ResultResultTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.stiffness_chek_data_idea_stati_ca_connection_checks import StiffnessChekDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.stiffness_chek_data_load_component_idea_stati_ca_connection_checks import StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.summary_check_res_data_context_idea_stati_ca_connection_checks import SummaryCheckResDataContextIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.summary_check_res_data_idea_stati_ca_connection_checks import SummaryCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.summary_check_res_data_message_context_idea_stati_ca_connection_checks import SummaryCheckResDataMessageContextIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
from connection_restapi_client_poc.models.weld_check_res_data_idea_stati_ca_connection_checks import WeldCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_check_res_data_info_idea_stati_ca_connection_checks import WeldCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_data_load_level_idea_stati_ca_connection_checks import WeldDataLoadLevelIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_evaluation_idea_rs_open_model import WeldEvaluationIdeaRSOpenModel
