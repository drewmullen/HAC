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


class Body5(object):
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
        'accessor': 'str'
    }

    attribute_map = {
        'accessor': 'accessor'
    }

    def __init__(self, accessor=None):  # noqa: E501
        """Body5 - a model defined in Swagger"""  # noqa: E501
        self._accessor = None
        self.discriminator = None
        if accessor is not None:
            self.accessor = accessor

    @property
    def accessor(self):
        """Gets the accessor of this Body5.  # noqa: E501

        Accessor of the token to look up (request body)  # noqa: E501

        :return: The accessor of this Body5.  # noqa: E501
        :rtype: str
        """
        return self._accessor

    @accessor.setter
    def accessor(self, accessor):
        """Sets the accessor of this Body5.

        Accessor of the token to look up (request body)  # noqa: E501

        :param accessor: The accessor of this Body5.  # noqa: E501
        :type: str
        """

        self._accessor = accessor

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
        if issubclass(Body5, dict):
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
        if not isinstance(other, Body5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
