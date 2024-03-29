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


class Body92(object):
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
        'dr_operation_token': 'str',
        'force': 'bool',
        'primary_cluster_addr': 'str'
    }

    attribute_map = {
        'dr_operation_token': 'dr_operation_token',
        'force': 'force',
        'primary_cluster_addr': 'primary_cluster_addr'
    }

    def __init__(self, dr_operation_token=None, force=None, primary_cluster_addr=None):  # noqa: E501
        """Body92 - a model defined in Swagger"""  # noqa: E501
        self._dr_operation_token = None
        self._force = None
        self._primary_cluster_addr = None
        self.discriminator = None
        if dr_operation_token is not None:
            self.dr_operation_token = dr_operation_token
        if force is not None:
            self.force = force
        if primary_cluster_addr is not None:
            self.primary_cluster_addr = primary_cluster_addr

    @property
    def dr_operation_token(self):
        """Gets the dr_operation_token of this Body92.  # noqa: E501

        DR root token used to authorize this request.  # noqa: E501

        :return: The dr_operation_token of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._dr_operation_token

    @dr_operation_token.setter
    def dr_operation_token(self, dr_operation_token):
        """Sets the dr_operation_token of this Body92.

        DR root token used to authorize this request.  # noqa: E501

        :param dr_operation_token: The dr_operation_token of this Body92.  # noqa: E501
        :type: str
        """

        self._dr_operation_token = dr_operation_token

    @property
    def force(self):
        """Gets the force of this Body92.  # noqa: E501

        Set to true if the cluster should be promoted despite replication being in an error state. This could mean some data was not replicated to the secondary  # noqa: E501

        :return: The force of this Body92.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this Body92.

        Set to true if the cluster should be promoted despite replication being in an error state. This could mean some data was not replicated to the secondary  # noqa: E501

        :param force: The force of this Body92.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def primary_cluster_addr(self):
        """Gets the primary_cluster_addr of this Body92.  # noqa: E501

        The address the secondary cluster should connect to. Defaults to the primary's cluster address.  # noqa: E501

        :return: The primary_cluster_addr of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._primary_cluster_addr

    @primary_cluster_addr.setter
    def primary_cluster_addr(self, primary_cluster_addr):
        """Sets the primary_cluster_addr of this Body92.

        The address the secondary cluster should connect to. Defaults to the primary's cluster address.  # noqa: E501

        :param primary_cluster_addr: The primary_cluster_addr of this Body92.  # noqa: E501
        :type: str
        """

        self._primary_cluster_addr = primary_cluster_addr

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
        if issubclass(Body92, dict):
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
        if not isinstance(other, Body92):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
