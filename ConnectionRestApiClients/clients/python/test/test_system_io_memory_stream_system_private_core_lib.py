# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib

class TestSystemIOMemoryStreamSystemPrivateCoreLib(unittest.TestCase):
    """SystemIOMemoryStreamSystemPrivateCoreLib unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemIOMemoryStreamSystemPrivateCoreLib:
        """Test SystemIOMemoryStreamSystemPrivateCoreLib
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemIOMemoryStreamSystemPrivateCoreLib`
        """
        model = SystemIOMemoryStreamSystemPrivateCoreLib()
        if include_optional:
            return SystemIOMemoryStreamSystemPrivateCoreLib(
                can_read = True,
                can_seek = True,
                can_write = True,
                capacity = 56,
                length = 56,
                position = 56,
                can_timeout = True,
                read_timeout = 56,
                write_timeout = 56
            )
        else:
            return SystemIOMemoryStreamSystemPrivateCoreLib(
        )
        """

    def testSystemIOMemoryStreamSystemPrivateCoreLib(self):
        """Test SystemIOMemoryStreamSystemPrivateCoreLib"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
