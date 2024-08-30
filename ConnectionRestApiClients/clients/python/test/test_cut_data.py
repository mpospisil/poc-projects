# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.cut_data import CutData

class TestCutData(unittest.TestCase):
    """CutData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CutData:
        """Test CutData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CutData`
        """
        model = CutData()
        if include_optional:
            return CutData(
                plane_point = connection_restapi_client_poc.models.point3_d.Point3D(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, ),
                normal_vector = connection_restapi_client_poc.models.vector3_d.Vector3D(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                direction = 'default',
                offset = 1.337
            )
        else:
            return CutData(
        )
        """

    def testCutData(self):
        """Test CutData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
