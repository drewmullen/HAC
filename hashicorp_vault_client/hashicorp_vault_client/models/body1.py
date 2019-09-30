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


class Body1(object):
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
        'jwt': 'str',
        'role': 'str'
    }

    attribute_map = {
        'jwt': 'jwt',
        'role': 'role'
    }

    def __init__(self, jwt=None, role=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._jwt = None
        self._role = None
        self.discriminator = None
        if jwt is not None:
            self.jwt = jwt
        if role is not None:
            self.role = role

    @property
    def jwt(self):
        """Gets the jwt of this Body1.  # noqa: E501

        The signed JWT to validate.  # noqa: E501

        :return: The jwt of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this Body1.

        The signed JWT to validate.  # noqa: E501

        :param jwt: The jwt of this Body1.  # noqa: E501
        :type: str
        """

        self._jwt = jwt

    @property
    def role(self):
        """Gets the role of this Body1.  # noqa: E501

        The role to log in against.  # noqa: E501

        :return: The role of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Body1.

        The role to log in against.  # noqa: E501

        :param role: The role of this Body1.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
