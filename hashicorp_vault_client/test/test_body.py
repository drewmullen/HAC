# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import hashicorp_vault_client
from models.body import Body  # noqa: E501
from hashicorp_vault_client.rest import ApiException


class TestBody(unittest.TestCase):
    """Body unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBody(self):
        """Test Body"""
        # FIXME: construct object with mandatory attributes with example values
        # model = hashicorp_vault_client.models.body.Body()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
