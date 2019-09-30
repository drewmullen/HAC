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


class Body79(object):
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
        'policy': 'str',
        'rules': 'str'
    }

    attribute_map = {
        'policy': 'policy',
        'rules': 'rules'
    }

    def __init__(self, policy=None, rules=None):  # noqa: E501
        """Body79 - a model defined in Swagger"""  # noqa: E501
        self._policy = None
        self._rules = None
        self.discriminator = None
        if policy is not None:
            self.policy = policy
        if rules is not None:
            self.rules = rules

    @property
    def policy(self):
        """Gets the policy of this Body79.  # noqa: E501

        The rules of the policy.  # noqa: E501

        :return: The policy of this Body79.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Body79.

        The rules of the policy.  # noqa: E501

        :param policy: The policy of this Body79.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def rules(self):
        """Gets the rules of this Body79.  # noqa: E501

        The rules of the policy.  # noqa: E501

        :return: The rules of this Body79.  # noqa: E501
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Body79.

        The rules of the policy.  # noqa: E501

        :param rules: The rules of this Body79.  # noqa: E501
        :type: str
        """

        self._rules = rules

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
        if issubclass(Body79, dict):
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
        if not isinstance(other, Body79):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
