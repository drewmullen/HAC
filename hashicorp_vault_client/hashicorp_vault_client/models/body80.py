# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body80(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'backup': 'bool',
        'pgp_keys': 'list[str]',
        'require_verification': 'bool',
        'secret_shares': 'int',
        'secret_threshold': 'int'
    }

    attribute_map = {
        'backup': 'backup',
        'pgp_keys': 'pgp_keys',
        'require_verification': 'require_verification',
        'secret_shares': 'secret_shares',
        'secret_threshold': 'secret_threshold'
    }

    def __init__(self, backup=None, pgp_keys=None, require_verification=None, secret_shares=None, secret_threshold=None):  # noqa: E501
        """Body80 - a model defined in Swagger"""  # noqa: E501
        self._backup = None
        self._pgp_keys = None
        self._require_verification = None
        self._secret_shares = None
        self._secret_threshold = None
        self.discriminator = None
        if backup is not None:
            self.backup = backup
        if pgp_keys is not None:
            self.pgp_keys = pgp_keys
        if require_verification is not None:
            self.require_verification = require_verification
        if secret_shares is not None:
            self.secret_shares = secret_shares
        if secret_threshold is not None:
            self.secret_threshold = secret_threshold

    @property
    def backup(self):
        """Gets the backup of this Body80.  # noqa: E501

        Specifies if using PGP-encrypted keys, whether Vault should also store a plaintext backup of the PGP-encrypted keys.  # noqa: E501

        :return: The backup of this Body80.  # noqa: E501
        :rtype: bool
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this Body80.

        Specifies if using PGP-encrypted keys, whether Vault should also store a plaintext backup of the PGP-encrypted keys.  # noqa: E501

        :param backup: The backup of this Body80.  # noqa: E501
        :type: bool
        """

        self._backup = backup

    @property
    def pgp_keys(self):
        """Gets the pgp_keys of this Body80.  # noqa: E501

        Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as secret_shares.  # noqa: E501

        :return: The pgp_keys of this Body80.  # noqa: E501
        :rtype: list[str]
        """
        return self._pgp_keys

    @pgp_keys.setter
    def pgp_keys(self, pgp_keys):
        """Sets the pgp_keys of this Body80.

        Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as secret_shares.  # noqa: E501

        :param pgp_keys: The pgp_keys of this Body80.  # noqa: E501
        :type: list[str]
        """

        self._pgp_keys = pgp_keys

    @property
    def require_verification(self):
        """Gets the require_verification of this Body80.  # noqa: E501

        Turns on verification functionality  # noqa: E501

        :return: The require_verification of this Body80.  # noqa: E501
        :rtype: bool
        """
        return self._require_verification

    @require_verification.setter
    def require_verification(self, require_verification):
        """Sets the require_verification of this Body80.

        Turns on verification functionality  # noqa: E501

        :param require_verification: The require_verification of this Body80.  # noqa: E501
        :type: bool
        """

        self._require_verification = require_verification

    @property
    def secret_shares(self):
        """Gets the secret_shares of this Body80.  # noqa: E501

        Specifies the number of shares to split the master key into.  # noqa: E501

        :return: The secret_shares of this Body80.  # noqa: E501
        :rtype: int
        """
        return self._secret_shares

    @secret_shares.setter
    def secret_shares(self, secret_shares):
        """Sets the secret_shares of this Body80.

        Specifies the number of shares to split the master key into.  # noqa: E501

        :param secret_shares: The secret_shares of this Body80.  # noqa: E501
        :type: int
        """

        self._secret_shares = secret_shares

    @property
    def secret_threshold(self):
        """Gets the secret_threshold of this Body80.  # noqa: E501

        Specifies the number of shares required to reconstruct the master key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as secret_shares.  # noqa: E501

        :return: The secret_threshold of this Body80.  # noqa: E501
        :rtype: int
        """
        return self._secret_threshold

    @secret_threshold.setter
    def secret_threshold(self, secret_threshold):
        """Sets the secret_threshold of this Body80.

        Specifies the number of shares required to reconstruct the master key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as secret_shares.  # noqa: E501

        :param secret_threshold: The secret_threshold of this Body80.  # noqa: E501
        :type: int
        """

        self._secret_threshold = secret_threshold

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body80, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body80):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
