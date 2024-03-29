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
from api.secrets_api import SecretsApi  # noqa: E501
from hashicorp_vault_client.rest import ApiException


class TestSecretsApi(unittest.TestCase):
    """SecretsApi unit test stubs"""

    def setUp(self):
        self.api = api.secrets_api.SecretsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_cubbyhole_path(self):
        """Test case for delete_cubbyhole_path

        Deletes the secret at the specified location.  # noqa: E501
        """
        pass

    def test_delete_kv_data_path(self):
        """Test case for delete_kv_data_path

        Write, Read, and Delete data in the Key-Value Store.  # noqa: E501
        """
        pass

    def test_delete_kv_metadata_path(self):
        """Test case for delete_kv_metadata_path

        Configures settings for the KV store  # noqa: E501
        """
        pass

    def test_get_cubbyhole_path(self):
        """Test case for get_cubbyhole_path

        Retrieve the secret at the specified location.  # noqa: E501
        """
        pass

    def test_get_kv_config(self):
        """Test case for get_kv_config

        Read the backend level settings.  # noqa: E501
        """
        pass

    def test_get_kv_data_path(self):
        """Test case for get_kv_data_path

        Write, Read, and Delete data in the Key-Value Store.  # noqa: E501
        """
        pass

    def test_get_kv_metadata_path(self):
        """Test case for get_kv_metadata_path

        Configures settings for the KV store  # noqa: E501
        """
        pass

    def test_post_cubbyhole_path(self):
        """Test case for post_cubbyhole_path

        Store a secret at the specified location.  # noqa: E501
        """
        pass

    def test_post_kv_config(self):
        """Test case for post_kv_config

        Configure backend level settings that are applied to every key in the key-value store.  # noqa: E501
        """
        pass

    def test_post_kv_data_path(self):
        """Test case for post_kv_data_path

        Write, Read, and Delete data in the Key-Value Store.  # noqa: E501
        """
        pass

    def test_post_kv_delete_path(self):
        """Test case for post_kv_delete_path

        Marks one or more versions as deleted in the KV store.  # noqa: E501
        """
        pass

    def test_post_kv_destroy_path(self):
        """Test case for post_kv_destroy_path

        Permanently removes one or more versions in the KV store  # noqa: E501
        """
        pass

    def test_post_kv_metadata_path(self):
        """Test case for post_kv_metadata_path

        Configures settings for the KV store  # noqa: E501
        """
        pass

    def test_post_kv_undelete_path(self):
        """Test case for post_kv_undelete_path

        Undeletes one or more versions from the KV store.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
