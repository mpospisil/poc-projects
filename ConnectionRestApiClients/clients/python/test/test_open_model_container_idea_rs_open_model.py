# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.open_model_container_idea_rs_open_model import OpenModelContainerIdeaRSOpenModel

class TestOpenModelContainerIdeaRSOpenModel(unittest.TestCase):
    """OpenModelContainerIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenModelContainerIdeaRSOpenModel:
        """Test OpenModelContainerIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenModelContainerIdeaRSOpenModel`
        """
        model = OpenModelContainerIdeaRSOpenModel()
        if include_optional:
            return OpenModelContainerIdeaRSOpenModel(
                open_model = connection_restapi_client_poc.models.open_model_idea_rs_open_model.OpenModel-IdeaRS_OpenModel(
                    version = 56, 
                    origin_settings = connection_restapi_client_poc.models.origin_settings.originSettings(), 
                    point3_d = [
                        connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model.Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, )
                        ], 
                    line_segment3_d = [
                        connection_restapi_client_poc.models.geometry3_d_line_segment3_d_idea_rs_open_model.Geometry3D_LineSegment3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    arc_segment3_d = [
                        connection_restapi_client_poc.models.geometry3_d_arc_segment3_d_idea_rs_open_model.Geometry3D_ArcSegment3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    poly_line3_d = [
                        connection_restapi_client_poc.models.geometry3_d_poly_line3_d_idea_rs_open_model.Geometry3D_PolyLine3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    region3_d = [
                        connection_restapi_client_poc.models.geometry3_d_region3_d_idea_rs_open_model.Geometry3D_Region3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    mat_concrete = [
                        connection_restapi_client_poc.models.material_mat_concrete_idea_rs_open_model.Material_MatConcrete-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    mat_reinforcement = [
                        connection_restapi_client_poc.models.material_mat_reinforcement_idea_rs_open_model.Material_MatReinforcement-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    mat_steel = [
                        connection_restapi_client_poc.models.material_mat_steel_idea_rs_open_model.Material_MatSteel-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    mat_prestress_steel = [
                        connection_restapi_client_poc.models.material_mat_prestress_steel_idea_rs_open_model.Material_MatPrestressSteel-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    mat_welding = [
                        connection_restapi_client_poc.models.material_mat_welding_idea_rs_open_model.Material_MatWelding-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    cross_section = [
                        connection_restapi_client_poc.models.cross_section_cross_section_idea_rs_open_model.CrossSection_CrossSection-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    reinforced_cross_section = [
                        connection_restapi_client_poc.models.cross_section_reinforced_cross_section_idea_rs_open_model.CrossSection_ReinforcedCrossSection-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    hinge_element1_d = [
                        connection_restapi_client_poc.models.model_hinge_element1_d_idea_rs_open_model.Model_HingeElement1D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    opening = [
                        connection_restapi_client_poc.models.detail_opening_idea_rs_open_model.Detail_Opening-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    dapped_end = [
                        connection_restapi_client_poc.models.detail_dapped_end_idea_rs_open_model.Detail_DappedEnd-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    patch_device = [
                        connection_restapi_client_poc.models.detail_patch_device_idea_rs_open_model.Detail_PatchDevice-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    element1_d = [
                        connection_restapi_client_poc.models.model_element1_d_idea_rs_open_model.Model_Element1D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    beam = [
                        connection_restapi_client_poc.models.detail_beam_idea_rs_open_model.Detail_Beam-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    member1_d = [
                        connection_restapi_client_poc.models.model_member1_d_idea_rs_open_model.Model_Member1D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    element2_d = [
                        connection_restapi_client_poc.models.model_element2_d_idea_rs_open_model.Model_Element2D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    wall = [
                        connection_restapi_client_poc.models.detail_wall_idea_rs_open_model.Detail_Wall-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    member2_d = [
                        connection_restapi_client_poc.models.model_member2_d_idea_rs_open_model.Model_Member2D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    rigid_link = [
                        connection_restapi_client_poc.models.model_rigid_link_idea_rs_open_model.Model_RigidLink-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    point_on_line3_d = [
                        connection_restapi_client_poc.models.geometry3_d_point_on_line3_d_idea_rs_open_model.Geometry3D_PointOnLine3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    point_support_node = [
                        connection_restapi_client_poc.models.model_point_support_node_idea_rs_open_model.Model_PointSupportNode-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    line_support_segment = [
                        connection_restapi_client_poc.models.model_line_support_segment_idea_rs_open_model.Model_LineSupportSegment-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    loads_in_point = [
                        connection_restapi_client_poc.models.loading_load_in_point_idea_rs_open_model.Loading_LoadInPoint-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    loads_on_line = [
                        connection_restapi_client_poc.models.loading_load_on_line_idea_rs_open_model.Loading_LoadOnLine-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    strain_loads_on_line = [
                        connection_restapi_client_poc.models.loading_strain_load_on_line_idea_rs_open_model.Loading_StrainLoadOnLine-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    point_loads_on_line = [
                        connection_restapi_client_poc.models.loading_point_load_on_line_idea_rs_open_model.Loading_PointLoadOnLine-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    loads_on_surface = [
                        connection_restapi_client_poc.models.loading_load_on_surface_idea_rs_open_model.Loading_LoadOnSurface-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    settlements = [
                        connection_restapi_client_poc.models.loading_settlement_idea_rs_open_model.Loading_Settlement-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    temperature_loads_on_line = [
                        connection_restapi_client_poc.models.loading_temperature_load_on_line_idea_rs_open_model.Loading_TemperatureLoadOnLine-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    load_group = [
                        connection_restapi_client_poc.models.loading_load_group_idea_rs_open_model.Loading_LoadGroup-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    load_case = [
                        connection_restapi_client_poc.models.loading_load_case_idea_rs_open_model.Loading_LoadCase-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    combi_input = [
                        connection_restapi_client_poc.models.loading_combi_input_idea_rs_open_model.Loading_CombiInput-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    attribute = [
                        connection_restapi_client_poc.models.open_attribute_idea_rs_open_model.OpenAttribute-IdeaRS_OpenModel()
                        ], 
                    connection_point = [
                        connection_restapi_client_poc.models.connection_connection_point_idea_rs_open_model.Connection_ConnectionPoint-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    connections = [
                        connection_restapi_client_poc.models.connection_connection_data_idea_rs_open_model.Connection_ConnectionData-IdeaRS_OpenModel(
                            conenction_point_id = 56, 
                            beams = [
                                connection_restapi_client_poc.models.connection_beam_data_idea_rs_open_model.Connection_BeamData-IdeaRS_OpenModel(
                                    name = '', 
                                    plates = [
                                        connection_restapi_client_poc.models.connection_plate_data_idea_rs_open_model.Connection_PlateData-IdeaRS_OpenModel(
                                            name = '', 
                                            thickness = 1.337, 
                                            material = '', 
                                            outline_points = [
                                                connection_restapi_client_poc.models.geometry2_d_point2_d_idea_rs_open_model.Geometry2D_Point2D-IdeaRS_OpenModel(
                                                    x = 1.337, 
                                                    y = 1.337, )
                                                ], 
                                            origin = connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model.Geometry3D_Point3D-IdeaRS_OpenModel(
                                                x = 1.337, 
                                                y = 1.337, 
                                                z = 1.337, 
                                                id = 56, ), 
                                            axis_x = connection_restapi_client_poc.models.geometry3_d_vector3_d_idea_rs_open_model.Geometry3D_Vector3D-IdeaRS_OpenModel(
                                                x = 1.337, 
                                                y = 1.337, 
                                                z = 1.337, ), 
                                            axis_y = connection_restapi_client_poc.models.geometry3_d_vector3_d_idea_rs_open_model.Geometry3D_Vector3D-IdeaRS_OpenModel(
                                                x = 1.337, 
                                                y = 1.337, 
                                                z = 1.337, ), 
                                            axis_z = , 
                                            region = '', 
                                            geometry = connection_restapi_client_poc.models.geometry2_d_region2_d_idea_rs_open_model.Geometry2D_Region2D-IdeaRS_OpenModel(
                                                outline = connection_restapi_client_poc.models.geometry2_d_poly_line2_d_idea_rs_open_model.Geometry2D_PolyLine2D-IdeaRS_OpenModel(
                                                    start_point = connection_restapi_client_poc.models.geometry2_d_point2_d_idea_rs_open_model.Geometry2D_Point2D-IdeaRS_OpenModel(
                                                        x = 1.337, 
                                                        y = 1.337, ), 
                                                    segments = [
                                                        connection_restapi_client_poc.models.geometry2_d_segment2_d_idea_rs_open_model.Geometry2D_Segment2D-IdeaRS_OpenModel(
                                                            end_point = , )
                                                        ], ), 
                                                openings = [
                                                    connection_restapi_client_poc.models.geometry2_d_poly_line2_d_idea_rs_open_model.Geometry2D_PolyLine2D-IdeaRS_OpenModel()
                                                    ], ), 
                                            original_model_id = '', 
                                            is_negative_object = True, 
                                            id = 56, )
                                        ], 
                                    cross_section_type = '', 
                                    mprl_name = '', 
                                    original_model_id = '', 
                                    cuts = [
                                        connection_restapi_client_poc.models.connection_cut_data_idea_rs_open_model.Connection_CutData-IdeaRS_OpenModel(
                                            plane_point = , 
                                            normal_vector = , 
                                            direction = 'default', 
                                            offset = 1.337, )
                                        ], 
                                    is_added = True, 
                                    added_member_length = 1.337, 
                                    is_negative_object = True, 
                                    added_member = connection_restapi_client_poc.models.reference_element_idea_rs_open_model.ReferenceElement-IdeaRS_OpenModel(
                                        type_name = '', 
                                        id = 56, 
                                        element = connection_restapi_client_poc.models.open_element_id_idea_rs_open_model.OpenElementId-IdeaRS_OpenModel(
                                            id = 56, ), ), 
                                    mirror_y = True, 
                                    ref_line_in_center_of_gravity = True, 
                                    is_bearing_member = True, 
                                    auto_add_cut_by_workplane = True, 
                                    id = 56, )
                                ], 
                            plates = [
                                connection_restapi_client_poc.models.connection_plate_data_idea_rs_open_model.Connection_PlateData-IdeaRS_OpenModel(
                                    name = '', 
                                    thickness = 1.337, 
                                    material = '', 
                                    region = '', 
                                    original_model_id = '', 
                                    is_negative_object = True, 
                                    id = 56, )
                                ], 
                            folded_plates = [
                                connection_restapi_client_poc.models.connection_folded_plate_data_idea_rs_open_model.Connection_FoldedPlateData-IdeaRS_OpenModel(
                                    bends = [
                                        connection_restapi_client_poc.models.connection_bend_data_idea_rs_open_model.Connection_BendData-IdeaRS_OpenModel(
                                            plate1_id = 56, 
                                            plate2_id = 56, 
                                            radius = 1.337, 
                                            point1_of_side_boundary1 = , 
                                            point2_of_side_boundary1 = , 
                                            end_face_normal1 = , 
                                            point1_of_side_boundary2 = , 
                                            point2_of_side_boundary2 = , )
                                        ], )
                                ], 
                            bolt_grids = [
                                connection_restapi_client_poc.models.connection_bolt_grid_idea_rs_open_model.Connection_BoltGrid-IdeaRS_OpenModel(
                                    bolt_assembly_ref = '', 
                                    id = 56, 
                                    is_anchor = True, 
                                    anchor_len = 1.337, 
                                    hole_diameter = 1.337, 
                                    diameter = 1.337, 
                                    head_diameter = 1.337, 
                                    diagonal_head_diameter = 1.337, 
                                    head_height = 1.337, 
                                    bore_hole = 1.337, 
                                    tensile_stress_area = 1.337, 
                                    nut_thickness = 1.337, 
                                    bolt_assembly_name = '', 
                                    standard = '', 
                                    material = '', 
                                    positions = [
                                        
                                        ], 
                                    connected_plates = [
                                        56
                                        ], 
                                    connected_part_ids = [
                                        ''
                                        ], 
                                    shear_in_thread = True, 
                                    bolt_interaction = 'bearing', )
                                ], 
                            anchor_grids = [
                                connection_restapi_client_poc.models.connection_anchor_grid_idea_rs_open_model.Connection_AnchorGrid-IdeaRS_OpenModel(
                                    concrete_block = connection_restapi_client_poc.models.connection_concrete_block_idea_rs_open_model.Connection_ConcreteBlock-IdeaRS_OpenModel(
                                        lenght = 1.337, 
                                        width = 1.337, 
                                        height = 1.337, 
                                        material = '', ), 
                                    anchor_type = 'straight', 
                                    washer_size = 1.337, 
                                    bolt_assembly_ref = '', 
                                    id = 56, 
                                    is_anchor = True, 
                                    anchor_len = 1.337, 
                                    hole_diameter = 1.337, 
                                    diameter = 1.337, 
                                    head_diameter = 1.337, 
                                    diagonal_head_diameter = 1.337, 
                                    head_height = 1.337, 
                                    bore_hole = 1.337, 
                                    tensile_stress_area = 1.337, 
                                    nut_thickness = 1.337, 
                                    bolt_assembly_name = '', 
                                    standard = '', 
                                    material = '', 
                                    shear_in_thread = True, )
                                ], 
                            welds = [
                                connection_restapi_client_poc.models.connection_weld_data_idea_rs_open_model.Connection_WeldData-IdeaRS_OpenModel(
                                    id = 56, 
                                    name = '', 
                                    thickness = 1.337, 
                                    material = '', 
                                    weld_material = connection_restapi_client_poc.models.reference_element_idea_rs_open_model.ReferenceElement-IdeaRS_OpenModel(
                                        type_name = '', 
                                        id = 56, ), 
                                    weld_type = 'notSpecified', 
                                    start = , 
                                    end = , )
                                ], 
                            concrete_blocks = [
                                connection_restapi_client_poc.models.connection_concrete_block_data_idea_rs_open_model.Connection_ConcreteBlockData-IdeaRS_OpenModel(
                                    id = 56, 
                                    name = '', 
                                    depth = 1.337, 
                                    material = '', 
                                    center = , 
                                    region = '', 
                                    original_model_id = '', )
                                ], 
                            cut_beam_by_beams = [
                                connection_restapi_client_poc.models.connection_cut_beam_by_beam_data_idea_rs_open_model.Connection_CutBeamByBeamData-IdeaRS_OpenModel(
                                    modified_object = , 
                                    cutting_object = , 
                                    is_weld = True, 
                                    weld_thickness = 1.337, 
                                    offset = 1.337, 
                                    method = 'boundingBox', 
                                    orientation = 'default', 
                                    plane_on_cutting_object = 'closer', 
                                    cut_part = 'begin', )
                                ], )
                        ], 
                    reinforcement = [
                        connection_restapi_client_poc.models.detail_reinforcement_idea_rs_open_model.Detail_Reinforcement-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    isd_model = [
                        connection_restapi_client_poc.models.detail_isd_model_idea_rs_open_model.Detail_ISDModel-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    initial_imperfection_of_point = [
                        connection_restapi_client_poc.models.model_initial_imperfection_of_point_idea_rs_open_model.Model_InitialImperfectionOfPoint-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    tendon = [
                        connection_restapi_client_poc.models.model_tendon_idea_rs_open_model.Model_Tendon-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    result_class = [
                        connection_restapi_client_poc.models.loading_result_class_idea_rs_open_model.Loading_ResultClass-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    design_member = [
                        connection_restapi_client_poc.models.model_design_member_idea_rs_open_model.Model_DesignMember-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    sub_structure = [
                        connection_restapi_client_poc.models.model_sub_structure_idea_rs_open_model.Model_SubStructure-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    connection_setup = connection_restapi_client_poc.models.connection_setup_idea_rs_open_model.ConnectionSetup-IdeaRS_OpenModel(
                        steel_setup = connection_restapi_client_poc.models.steel_setup.steelSetup(), 
                        concrete_setup = connection_restapi_client_poc.models.concrete_concrete_setup_idea_rs_open_model.Concrete_ConcreteSetup-IdeaRS_OpenModel(
                            id = 56, ), 
                        stop_at_limit_strain = True, 
                        weld_evaluation_data = 'maxForceElement', 
                        check_detailing = True, 
                        apply_cone_breakout_check = 'both', 
                        pretension_force_fpc = 1.337, 
                        gamma_inst = 1.337, 
                        gamma_c = 1.337, 
                        gamma_m3 = 1.337, 
                        anchor_length_for_stiffness = 56, 
                        joint_beta_factor = 1.337, 
                        effective_area_stress_coeff = 1.337, 
                        effective_area_stress_coeff_aisc = 1.337, 
                        friction_coefficient = 1.337, 
                        limit_plastic_strain = 1.337, 
                        limit_deformation = 1.337, 
                        limit_deformation_check = True, 
                        analysis_gnl = True, 
                        analysis_all_gnl = True, 
                        warn_plastic_strain = 1.337, 
                        warn_check_level = 1.337, 
                        optimal_check_level = 1.337, 
                        distance_between_bolts = 1.337, 
                        distance_diameter_between_bp = 1.337, 
                        distance_between_bolts_edge = 1.337, 
                        bearing_angle = 1.337, 
                        decreasing_ftrd = 1.337, 
                        braced_system = True, 
                        bearing_check = True, 
                        apply_betap_influence = True, 
                        member_length_ratio = 1.337, 
                        division_of_surface_of_chs = 56, 
                        division_of_arcs_of_rhs = 56, 
                        num_element = 56, 
                        number_iterations = 56, 
                        mdiv = 56, 
                        min_size = 1.337, 
                        max_size = 1.337, 
                        num_element_rhs = 56, 
                        num_element_plate = 56, 
                        rigid_bp = True, 
                        alpha_cc = 1.337, 
                        cracked_concrete = True, 
                        developed_fillers = True, 
                        deformation_bolt_hole = True, 
                        extension_length_ration_open_sections = 1.337, 
                        extension_length_ration_close_sections = 1.337, 
                        factor_preload_bolt = 1.337, 
                        base_metal_capacity = True, 
                        apply_bearing_check = True, 
                        friction_coefficient_pbolt = 1.337, 
                        crt_comp_check_is = 'iS800_Cl_7_4', 
                        bolt_max_grip_length_coeff = 1.337, 
                        fatigue_section_offset = 1.337, 
                        condensed_element_length_factor = 1.337, 
                        gamma_mu = 1.337, 
                        hss_limit_plastic_strain = 1.337, ), 
                    project_data = connection_restapi_client_poc.models.project_data.projectData(), 
                    check_member = [
                        connection_restapi_client_poc.models.model_check_member_idea_rs_open_model.Model_CheckMember-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    concrete_check_section = [
                        connection_restapi_client_poc.models.concrete_check_section_idea_rs_open_model.Concrete_CheckSection-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    concrete_setup = connection_restapi_client_poc.models.concrete_concrete_setup_idea_rs_open_model.Concrete_ConcreteSetup-IdeaRS_OpenModel(
                        id = 56, ), 
                    project_data_concrete = connection_restapi_client_poc.models.project_data_concrete.projectDataConcrete(), 
                    rebar_shape = [
                        connection_restapi_client_poc.models.model_rebar_shape_idea_rs_open_model.Model_RebarShape-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    rebar_general = [
                        connection_restapi_client_poc.models.model_rebar_general_idea_rs_open_model.Model_RebarGeneral-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    rebar_single = [
                        connection_restapi_client_poc.models.model_rebar_single_idea_rs_open_model.Model_RebarSingle-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    rebar_stirrups = [
                        connection_restapi_client_poc.models.model_rebar_stirrups_idea_rs_open_model.Model_RebarStirrups-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    taper = [
                        connection_restapi_client_poc.models.model_taper_idea_rs_open_model.Model_Taper-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    span = [
                        connection_restapi_client_poc.models.model_span_idea_rs_open_model.Model_Span-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    solid_blocks3_d = [
                        connection_restapi_client_poc.models.detail_solid_block3_d_idea_rs_open_model.Detail_SolidBlock3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    surface_supports3_d = [
                        connection_restapi_client_poc.models.detail_surface_support3_d_idea_rs_open_model.Detail_SurfaceSupport3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    base_plates3_d = [
                        connection_restapi_client_poc.models.detail_base_plate3_d_idea_rs_open_model.Detail_BasePlate3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    anchors3_d = [
                        connection_restapi_client_poc.models.detail_anchor3_d_idea_rs_open_model.Detail_Anchor3D-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    detail_load_case = [
                        connection_restapi_client_poc.models.detail_loading_detail_load_case_idea_rs_open_model.Detail_Loading_DetailLoadCase-IdeaRS_OpenModel(
                            id = 56, )
                        ], 
                    detail_combination = [
                        connection_restapi_client_poc.models.detail_loading_detail_combination_idea_rs_open_model.Detail_Loading_DetailCombination-IdeaRS_OpenModel(
                            id = 56, )
                        ], ),
                open_model_result = connection_restapi_client_poc.models.result_open_model_result_idea_rs_open_model.Result_OpenModelResult-IdeaRS_OpenModel(
                    result_on_members = [
                        connection_restapi_client_poc.models.result_result_on_members_idea_rs_open_model.Result_ResultOnMembers-IdeaRS_OpenModel(
                            loading = connection_restapi_client_poc.models.result_loading_idea_rs_open_model.Result_Loading-IdeaRS_OpenModel(
                                loading_type = 'loadCase', 
                                id = 56, ), 
                            members = [
                                connection_restapi_client_poc.models.result_result_on_member_idea_rs_open_model.Result_ResultOnMember-IdeaRS_OpenModel(
                                    member = connection_restapi_client_poc.models.result_member_idea_rs_open_model.Result_Member-IdeaRS_OpenModel(
                                        member_type = 'member1D', 
                                        id = 56, ), 
                                    result_type = 'internalForces', 
                                    local_system_type = 'local', 
                                    results = [
                                        connection_restapi_client_poc.models.result_result_base_idea_rs_open_model.Result_ResultBase-IdeaRS_OpenModel()
                                        ], )
                                ], )
                        ], )
            )
        else:
            return OpenModelContainerIdeaRSOpenModel(
        )
        """

    def testOpenModelContainerIdeaRSOpenModel(self):
        """Test OpenModelContainerIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
