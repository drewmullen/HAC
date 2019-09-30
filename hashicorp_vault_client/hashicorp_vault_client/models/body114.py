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


class Body114(object):
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
        'bytes': 'int',
        'format': 'str',
        'urlbytes': 'str'
    }

    attribute_map = {
        'bytes': 'bytes',
        'format': 'format',
        'urlbytes': 'urlbytes'
    }

    def __init__(self, bytes=32, format='base64', urlbytes=None):  # noqa: E501
        """Body114 - a model defined in Swagger"""  # noqa: E501
        self._bytes = None
        self._format = None
        self._urlbytes = None
        self.discriminator = None
        if bytes is not None:
            self.bytes = bytes
        if format is not None:
            self.format = format
        if urlbytes is not None:
            self.urlbytes = urlbytes

    @property
    def bytes(self):
        """Gets the bytes of this Body114.  # noqa: E501

        The number of bytes to generate (POST body parameter). Defaults to 32 (256 bits).  # noqa: E501

        :return: The bytes of this Body114.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this Body114.

        The number of bytes to generate (POST body parameter). Defaults to 32 (256 bits).  # noqa: E501

        :param bytes: The bytes of this Body114.  # noqa: E501
        :type: int
        """

        self._bytes = bytes

    @property
    def format(self):
        """Gets the format of this Body114.  # noqa: E501

        Encoding format to use. Can be \"hex\" or \"base64\". Defaults to \"base64\".  # noqa: E501

        :return: The format of this Body114.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Body114.

        Encoding format to use. Can be \"hex\" or \"base64\". Defaults to \"base64\".  # noqa: E501

        :param format: The format of this Body114.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def urlbytes(self):
        """Gets the urlbytes of this Body114.  # noqa: E501

        The number of bytes to generate (POST URL parameter)  # noqa: E501

        :return: The urlbytes of this Body114.  # noqa: E501
        :rtype: str
        """
        return self._urlbytes

    @urlbytes.setter
    def urlbytes(self, urlbytes):
        """Sets the urlbytes of this Body114.

        The number of bytes to generate (POST URL parameter)  # noqa: E501

        :param urlbytes: The urlbytes of this Body114.  # noqa: E501
        :type: str
        """

        self._urlbytes = urlbytes

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
        if issubclass(Body114, dict):
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
        if not isinstance(other, Body114):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
