# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_connection_data_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel(
                conenction_point_id = 56,
                beams = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_beam_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_BeamData-IdeaRS_OpenModel(
                        name = '', 
                        plates = [
                            connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_PlateData-IdeaRS_OpenModel(
                                name = '', 
                                thickness = 1.337, 
                                material = '', 
                                outline_points = [
                                    connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                        x = 1.337, 
                                        y = 1.337, )
                                    ], 
                                origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, 
                                    id = 56, ), 
                                axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, ), 
                                axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, ), 
                                axis_z = , 
                                region = '', 
                                geometry = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Region2D-IdeaRS_OpenModel(
                                    outline = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel(
                                        start_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                            x = 1.337, 
                                            y = 1.337, ), 
                                        segments = [
                                            connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Segment2D-IdeaRS_OpenModel(
                                                end_point = , )
                                            ], ), 
                                    openings = [
                                        connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel()
                                        ], ), 
                                original_model_id = '', 
                                is_negative_object = True, 
                                id = 56, )
                            ], 
                        cross_section_type = '', 
                        mprl_name = '', 
                        original_model_id = '', 
                        cuts = [
                            connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_CutData-IdeaRS_OpenModel(
                                plane_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, 
                                    id = 56, ), 
                                normal_vector = , 
                                direction = 'default', 
                                offset = 1.337, )
                            ], 
                        is_added = True, 
                        added_member_length = 1.337, 
                        is_negative_object = True, 
                        added_member = connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model.IdeaRS_OpenModel_ReferenceElement-IdeaRS_OpenModel(
                            type_name = '', 
                            id = 56, 
                            element = connection_restapi_client_poc.models.idea_rs_open_model_open_element_id_idea_rs_open_model.IdeaRS_OpenModel_OpenElementId-IdeaRS_OpenModel(
                                id = 56, ), ), 
                        mirror_y = True, 
                        ref_line_in_center_of_gravity = True, 
                        is_bearing_member = True, 
                        auto_add_cut_by_workplane = True, 
                        id = 56, )
                    ],
                plates = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_PlateData-IdeaRS_OpenModel(
                        name = '', 
                        thickness = 1.337, 
                        material = '', 
                        outline_points = [
                            connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                x = 1.337, 
                                y = 1.337, )
                            ], 
                        origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_z = , 
                        region = '', 
                        geometry = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Region2D-IdeaRS_OpenModel(
                            outline = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel(
                                start_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, ), 
                                segments = [
                                    connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Segment2D-IdeaRS_OpenModel(
                                        end_point = , )
                                    ], ), 
                            openings = [
                                connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel()
                                ], ), 
                        original_model_id = '', 
                        is_negative_object = True, 
                        id = 56, )
                    ],
                folded_plates = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_folded_plate_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_FoldedPlateData-IdeaRS_OpenModel(
                        plates = [
                            connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_PlateData-IdeaRS_OpenModel(
                                name = '', 
                                thickness = 1.337, 
                                material = '', 
                                outline_points = [
                                    connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                        x = 1.337, 
                                        y = 1.337, )
                                    ], 
                                origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, 
                                    id = 56, ), 
                                axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, ), 
                                axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, ), 
                                axis_z = , 
                                region = '', 
                                geometry = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Region2D-IdeaRS_OpenModel(
                                    outline = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel(
                                        start_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                            x = 1.337, 
                                            y = 1.337, ), 
                                        segments = [
                                            connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Segment2D-IdeaRS_OpenModel(
                                                end_point = , )
                                            ], ), 
                                    openings = [
                                        connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel()
                                        ], ), 
                                original_model_id = '', 
                                is_negative_object = True, 
                                id = 56, )
                            ], 
                        bends = [
                            connection_restapi_client_poc.models.idea_rs_open_model_connection_bend_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_BendData-IdeaRS_OpenModel(
                                plate1_id = 56, 
                                plate2_id = 56, 
                                radius = 1.337, 
                                point1_of_side_boundary1 = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, 
                                    z = 1.337, 
                                    id = 56, ), 
                                point2_of_side_boundary1 = , 
                                end_face_normal1 = , 
                                point1_of_side_boundary2 = , 
                                point2_of_side_boundary2 = , )
                            ], )
                    ],
                bolt_grids = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_bolt_grid_idea_rs_open_model.IdeaRS_OpenModel_Connection_BoltGrid-IdeaRS_OpenModel(
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
                        origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_z = , 
                        positions = [
                            connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                x = 1.337, 
                                y = 1.337, 
                                z = 1.337, 
                                id = 56, )
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
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_anchor_grid_idea_rs_open_model.IdeaRS_OpenModel_Connection_AnchorGrid-IdeaRS_OpenModel(
                        concrete_block = connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_idea_rs_open_model.IdeaRS_OpenModel_Connection_ConcreteBlock-IdeaRS_OpenModel(
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
                        origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_z = , 
                        positions = [
                            connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                                x = 1.337, 
                                y = 1.337, 
                                z = 1.337, 
                                id = 56, )
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
                welds = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_weld_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_WeldData-IdeaRS_OpenModel(
                        id = 56, 
                        name = '', 
                        thickness = 1.337, 
                        material = '', 
                        weld_material = connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model.IdeaRS_OpenModel_ReferenceElement-IdeaRS_OpenModel(
                            type_name = '', 
                            id = 56, 
                            element = connection_restapi_client_poc.models.idea_rs_open_model_open_element_id_idea_rs_open_model.IdeaRS_OpenModel_OpenElementId-IdeaRS_OpenModel(
                                id = 56, ), ), 
                        weld_type = 'notSpecified', 
                        connected_part_ids = [
                            ''
                            ], 
                        start = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        end = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), )
                    ],
                concrete_blocks = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_ConcreteBlockData-IdeaRS_OpenModel(
                        id = 56, 
                        name = '', 
                        depth = 1.337, 
                        material = '', 
                        center = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        outline_points = [
                            connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                x = 1.337, 
                                y = 1.337, )
                            ], 
                        origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, 
                            id = 56, ), 
                        axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, 
                            z = 1.337, ), 
                        axis_z = , 
                        region = '', 
                        original_model_id = '', )
                    ],
                cut_beam_by_beams = [
                    connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_beam_by_beam_data_idea_rs_open_model.IdeaRS_OpenModel_Connection_CutBeamByBeamData-IdeaRS_OpenModel(
                        modified_object = connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model.IdeaRS_OpenModel_ReferenceElement-IdeaRS_OpenModel(
                            type_name = '', 
                            id = 56, 
                            element = connection_restapi_client_poc.models.idea_rs_open_model_open_element_id_idea_rs_open_model.IdeaRS_OpenModel_OpenElementId-IdeaRS_OpenModel(
                                id = 56, ), ), 
                        cutting_object = connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model.IdeaRS_OpenModel_ReferenceElement-IdeaRS_OpenModel(
                            type_name = '', 
                            id = 56, ), 
                        is_weld = True, 
                        weld_thickness = 1.337, 
                        weld_type = 'notSpecified', 
                        offset = 1.337, 
                        method = 'boundingBox', 
                        orientation = 'default', 
                        plane_on_cutting_object = 'closer', 
                        cut_part = 'begin', )
                    ]
            )
        else:
            return IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
