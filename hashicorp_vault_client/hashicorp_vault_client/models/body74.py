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


class Body74(object):
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
        'args': 'list[str]',
        'command': 'str',
        'env': 'list[str]',
        'sha256': 'str',
        'sha_256': 'str'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'env': 'env',
        'sha256': 'sha256',
        'sha_256': 'sha_256'
    }

    def __init__(self, args=None, command=None, env=None, sha256=None, sha_256=None):  # noqa: E501
        """Body74 - a model defined in Swagger"""  # noqa: E501
        self._args = None
        self._command = None
        self._env = None
        self._sha256 = None
        self._sha_256 = None
        self.discriminator = None
        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if sha256 is not None:
            self.sha256 = sha256
        if sha_256 is not None:
            self.sha_256 = sha_256

    @property
    def args(self):
        """Gets the args of this Body74.  # noqa: E501

        The args passed to plugin command.  # noqa: E501

        :return: The args of this Body74.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Body74.

        The args passed to plugin command.  # noqa: E501

        :param args: The args of this Body74.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this Body74.  # noqa: E501

        The command used to start the plugin. The executable defined in this command must exist in vault's plugin directory.  # noqa: E501

        :return: The command of this Body74.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Body74.

        The command used to start the plugin. The executable defined in this command must exist in vault's plugin directory.  # noqa: E501

        :param command: The command of this Body74.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this Body74.  # noqa: E501

        The environment variables passed to plugin command. Each entry is of the form \"key=value\".  # noqa: E501

        :return: The env of this Body74.  # noqa: E501
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this Body74.

        The environment variables passed to plugin command. Each entry is of the form \"key=value\".  # noqa: E501

        :param env: The env of this Body74.  # noqa: E501
        :type: list[str]
        """

        self._env = env

    @property
    def sha256(self):
        """Gets the sha256 of this Body74.  # noqa: E501

        The SHA256 sum of the executable used in the command field. This should be HEX encoded.  # noqa: E501

        :return: The sha256 of this Body74.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this Body74.

        The SHA256 sum of the executable used in the command field. This should be HEX encoded.  # noqa: E501

        :param sha256: The sha256 of this Body74.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def sha_256(self):
        """Gets the sha_256 of this Body74.  # noqa: E501

        The SHA256 sum of the executable used in the command field. This should be HEX encoded.  # noqa: E501

        :return: The sha_256 of this Body74.  # noqa: E501
        :rtype: str
        """
        return self._sha_256

    @sha_256.setter
    def sha_256(self, sha_256):
        """Sets the sha_256 of this Body74.

        The SHA256 sum of the executable used in the command field. This should be HEX encoded.  # noqa: E501

        :param sha_256: The sha_256 of this Body74.  # noqa: E501
        :type: str
        """

        self._sha_256 = sha_256

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
        if issubclass(Body74, dict):
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
        if not isinstance(other, Body74):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
