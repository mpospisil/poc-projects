# coding: utf-8

"""
    ConDesignProposer API 9.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from idea_cdp_client_poc.models.cdi_design_item_v9 import CdiDesignItemV9

class TestCdiDesignItemV9(unittest.TestCase):
    """CdiDesignItemV9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CdiDesignItemV9:
        """Test CdiDesignItemV9
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CdiDesignItemV9`
        """
        model = CdiDesignItemV9()
        if include_optional:
            return CdiDesignItemV9(
                con_design_item = idea_cdp_client_poc.models.con_design_item.ConDesignItem(
                    picture_id = '', 
                    version = '', 
                    name = '0', 
                    owner_id = '', 
                    design_code = '', 
                    con_design_set_id = '', 
                    con_design_item_id = '', 
                    design_data = idea_cdp_client_poc.models.con_design_data.ConDesignData(
                        typology = idea_cdp_client_poc.models.con_typology.ConTypology(
                            bearing_member = idea_cdp_client_poc.models.bearing_member_data.BearingMemberData(
                                operation_id = 56, 
                                order = 56, 
                                inclination = 1.337, 
                                continuity_type = 0, 
                                css_meta_data = idea_cdp_client_poc.models.css_data.CssData(
                                    arc_segment_count = 56, 
                                    css_class = 0, 
                                    css_size = idea_cdp_client_poc.models.css_size.CssSize(
                                        width = 1.337, 
                                        height = 1.337, ), 
                                    integrality_type = 0, 
                                    label = '', 
                                    main_segment_count = 56, 
                                    shape = 0, 
                                    type = '', 
                                    form_code = 0, ), 
                                rigidity = 0, 
                                static_behaviour = 56, ), 
                            connected_members = [
                                idea_cdp_client_poc.models.connected_member_data.ConnectedMemberData(
                                    operation_id = 56, 
                                    typological_sector_code = 56, 
                                    order = 56, 
                                    lcs_rotatiton = 1.337, 
                                    dir_related_to_bearing = 0, 
                                    static_behaviour = 56, )
                                ], 
                            typology_code = '', ), 
                        manufacture = idea_cdp_client_poc.models.con_manufacture.ConManufacture(
                            manufacturing_type = 0, 
                            connection_template = '', 
                            con_parts = [
                                idea_cdp_client_poc.models.con_part.ConPart(
                                    stiffness = 0, 
                                    category = 0, )
                                ], 
                            operations_info = idea_cdp_client_poc.models.operations_info.OperationsInfo(
                                end_plate = idea_cdp_client_poc.models.end_plate.EndPlate(
                                    count = 56, ), 
                                shifted_end_plate = idea_cdp_client_poc.models.shifted_end_plate.ShiftedEndPlate(
                                    count = 56, ), 
                                stub = idea_cdp_client_poc.models.stub.Stub(
                                    count = 56, ), 
                                plate_to_plate = idea_cdp_client_poc.models.plate_to_plate.PlateToPlate(
                                    count = 56, ), 
                                splice_plate = idea_cdp_client_poc.models.splice_plate.SplicePlate(
                                    count = 56, ), 
                                gusset_plate = idea_cdp_client_poc.models.gusset_plate.GussetPlate(
                                    count = 56, 
                                    gusset_plate_type = 0, ), 
                                connecting_plate = idea_cdp_client_poc.models.connecting_plate.ConnectingPlate(
                                    count = 56, 
                                    connecting_plate_type = 0, ), 
                                fin_plate = idea_cdp_client_poc.models.fin_plate.FinPlate(
                                    count = 56, ), 
                                cleat = idea_cdp_client_poc.models.cleat.Cleat(
                                    count = 56, ), 
                                anchoring = idea_cdp_client_poc.models.anchoring.Anchoring(
                                    count = 56, 
                                    anchoring_type = 0, ), 
                                opening = idea_cdp_client_poc.models.opening.Opening(
                                    count = 56, ), 
                                general_plate = idea_cdp_client_poc.models.general_plate.GeneralPlate(
                                    count = 56, 
                                    general_plate_type = 0, ), 
                                stiffener = idea_cdp_client_poc.models.stiffener.Stiffener(
                                    count = 56, ), 
                                bolt_grid = idea_cdp_client_poc.models.bolt_grid.BoltGrid(
                                    count = 56, ), 
                                pin_grid = idea_cdp_client_poc.models.pin_grid.PinGrid(
                                    count = 56, ), ), 
                            typology_code = '', ), ), 
                    company_name = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    load_transfer_type = 0, 
                    author_name = '', 
                    activity = True, 
                    priority = True, 
                    imported = True, 
                    is_parametric = True, ),
                picture_url = '',
                project_url = '',
                scene3d_url = ''
            )
        else:
            return CdiDesignItemV9(
        )
        """

    def testCdiDesignItemV9(self):
        """Test CdiDesignItemV9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
