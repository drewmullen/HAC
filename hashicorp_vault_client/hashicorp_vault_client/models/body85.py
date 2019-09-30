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


class Body85(object):
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
        'increment': 'int',
        'lease_id': 'str'
    }

    attribute_map = {
        'increment': 'increment',
        'lease_id': 'lease_id'
    }

    def __init__(self, increment=None, lease_id=None):  # noqa: E501
        """Body85 - a model defined in Swagger"""  # noqa: E501
        self._increment = None
        self._lease_id = None
        self.discriminator = None
        if increment is not None:
            self.increment = increment
        if lease_id is not None:
            self.lease_id = lease_id

    @property
    def increment(self):
        """Gets the increment of this Body85.  # noqa: E501

        The desired increment in seconds to the lease  # noqa: E501

        :return: The increment of this Body85.  # noqa: E501
        :rtype: int
        """
        return self._increment

    @increment.setter
    def increment(self, increment):
        """Sets the increment of this Body85.

        The desired increment in seconds to the lease  # noqa: E501

        :param increment: The increment of this Body85.  # noqa: E501
        :type: int
        """

        self._increment = increment

    @property
    def lease_id(self):
        """Gets the lease_id of this Body85.  # noqa: E501

        The lease identifier to renew. This is included with a lease.  # noqa: E501

        :return: The lease_id of this Body85.  # noqa: E501
        :rtype: str
        """
        return self._lease_id

    @lease_id.setter
    def lease_id(self, lease_id):
        """Sets the lease_id of this Body85.

        The lease identifier to renew. This is included with a lease.  # noqa: E501

        :param lease_id: The lease_id of this Body85.  # noqa: E501
        :type: str
        """

        self._lease_id = lease_id

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
        if issubclass(Body85, dict):
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
        if not isinstance(other, Body85):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
