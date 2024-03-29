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


class Body96(object):
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
        'mode': 'str',
        'paths': 'list[str]'
    }

    attribute_map = {
        'mode': 'mode',
        'paths': 'paths'
    }

    def __init__(self, mode='whitelist', paths=None):  # noqa: E501
        """Body96 - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._paths = None
        self.discriminator = None
        if mode is not None:
            self.mode = mode
        if paths is not None:
            self.paths = paths

    @property
    def mode(self):
        """Gets the mode of this Body96.  # noqa: E501

        The filter mode for the mount paths (whitelist or blacklist). Defaults to whitelist.  # noqa: E501

        :return: The mode of this Body96.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Body96.

        The filter mode for the mount paths (whitelist or blacklist). Defaults to whitelist.  # noqa: E501

        :param mode: The mode of this Body96.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def paths(self):
        """Gets the paths of this Body96.  # noqa: E501

        The paths to the mount to filter in replication.  # noqa: E501

        :return: The paths of this Body96.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this Body96.

        The paths to the mount to filter in replication.  # noqa: E501

        :param paths: The paths of this Body96.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

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
        if issubclass(Body96, dict):
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
        if not isinstance(other, Body96):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
