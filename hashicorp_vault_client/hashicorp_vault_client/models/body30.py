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


class Body30(object):
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
        'algorithm': 'str',
        'allowed_client_ids': 'list[str]',
        'rotation_period': 'int',
        'verification_ttl': 'int'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'allowed_client_ids': 'allowed_client_ids',
        'rotation_period': 'rotation_period',
        'verification_ttl': 'verification_ttl'
    }

    def __init__(self, algorithm='RS256', allowed_client_ids=None, rotation_period=None, verification_ttl=None):  # noqa: E501
        """Body30 - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._allowed_client_ids = None
        self._rotation_period = None
        self._verification_ttl = None
        self.discriminator = None
        if algorithm is not None:
            self.algorithm = algorithm
        if allowed_client_ids is not None:
            self.allowed_client_ids = allowed_client_ids
        if rotation_period is not None:
            self.rotation_period = rotation_period
        if verification_ttl is not None:
            self.verification_ttl = verification_ttl

    @property
    def algorithm(self):
        """Gets the algorithm of this Body30.  # noqa: E501

        Signing algorithm to use. This will default to RS256.  # noqa: E501

        :return: The algorithm of this Body30.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this Body30.

        Signing algorithm to use. This will default to RS256.  # noqa: E501

        :param algorithm: The algorithm of this Body30.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def allowed_client_ids(self):
        """Gets the allowed_client_ids of this Body30.  # noqa: E501

        Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \"*\" all roles are allowed.  # noqa: E501

        :return: The allowed_client_ids of this Body30.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_client_ids

    @allowed_client_ids.setter
    def allowed_client_ids(self, allowed_client_ids):
        """Sets the allowed_client_ids of this Body30.

        Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \"*\" all roles are allowed.  # noqa: E501

        :param allowed_client_ids: The allowed_client_ids of this Body30.  # noqa: E501
        :type: list[str]
        """

        self._allowed_client_ids = allowed_client_ids

    @property
    def rotation_period(self):
        """Gets the rotation_period of this Body30.  # noqa: E501

        How often to generate a new keypair.  # noqa: E501

        :return: The rotation_period of this Body30.  # noqa: E501
        :rtype: int
        """
        return self._rotation_period

    @rotation_period.setter
    def rotation_period(self, rotation_period):
        """Sets the rotation_period of this Body30.

        How often to generate a new keypair.  # noqa: E501

        :param rotation_period: The rotation_period of this Body30.  # noqa: E501
        :type: int
        """

        self._rotation_period = rotation_period

    @property
    def verification_ttl(self):
        """Gets the verification_ttl of this Body30.  # noqa: E501

        Controls how long the public portion of a key will be available for verification after being rotated.  # noqa: E501

        :return: The verification_ttl of this Body30.  # noqa: E501
        :rtype: int
        """
        return self._verification_ttl

    @verification_ttl.setter
    def verification_ttl(self, verification_ttl):
        """Sets the verification_ttl of this Body30.

        Controls how long the public portion of a key will be available for verification after being rotated.  # noqa: E501

        :param verification_ttl: The verification_ttl of this Body30.  # noqa: E501
        :type: int
        """

        self._verification_ttl = verification_ttl

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
        if issubclass(Body30, dict):
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
        if not isinstance(other, Body30):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
