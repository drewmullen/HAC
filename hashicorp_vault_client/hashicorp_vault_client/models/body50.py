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


class Body50(object):
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
        'allowed_headers': 'list[str]',
        'allowed_origins': 'list[str]',
        'enable': 'bool'
    }

    attribute_map = {
        'allowed_headers': 'allowed_headers',
        'allowed_origins': 'allowed_origins',
        'enable': 'enable'
    }

    def __init__(self, allowed_headers=None, allowed_origins=None, enable=None):  # noqa: E501
        """Body50 - a model defined in Swagger"""  # noqa: E501
        self._allowed_headers = None
        self._allowed_origins = None
        self._enable = None
        self.discriminator = None
        if allowed_headers is not None:
            self.allowed_headers = allowed_headers
        if allowed_origins is not None:
            self.allowed_origins = allowed_origins
        if enable is not None:
            self.enable = enable

    @property
    def allowed_headers(self):
        """Gets the allowed_headers of this Body50.  # noqa: E501

        A comma-separated string or array of strings indicating headers that are allowed on cross-origin requests.  # noqa: E501

        :return: The allowed_headers of this Body50.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_headers

    @allowed_headers.setter
    def allowed_headers(self, allowed_headers):
        """Sets the allowed_headers of this Body50.

        A comma-separated string or array of strings indicating headers that are allowed on cross-origin requests.  # noqa: E501

        :param allowed_headers: The allowed_headers of this Body50.  # noqa: E501
        :type: list[str]
        """

        self._allowed_headers = allowed_headers

    @property
    def allowed_origins(self):
        """Gets the allowed_origins of this Body50.  # noqa: E501

        A comma-separated string or array of strings indicating origins that may make cross-origin requests.  # noqa: E501

        :return: The allowed_origins of this Body50.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_origins

    @allowed_origins.setter
    def allowed_origins(self, allowed_origins):
        """Sets the allowed_origins of this Body50.

        A comma-separated string or array of strings indicating origins that may make cross-origin requests.  # noqa: E501

        :param allowed_origins: The allowed_origins of this Body50.  # noqa: E501
        :type: list[str]
        """

        self._allowed_origins = allowed_origins

    @property
    def enable(self):
        """Gets the enable of this Body50.  # noqa: E501

        Enables or disables CORS headers on requests.  # noqa: E501

        :return: The enable of this Body50.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this Body50.

        Enables or disables CORS headers on requests.  # noqa: E501

        :param enable: The enable of this Body50.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if issubclass(Body50, dict):
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
        if not isinstance(other, Body50):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other