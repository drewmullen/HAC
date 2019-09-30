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


class Body34(object):
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
        'entity_id': 'str',
        'metadata': 'object',
        'mount_accessor': 'str',
        'name': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'metadata': 'metadata',
        'mount_accessor': 'mount_accessor',
        'name': 'name'
    }

    def __init__(self, entity_id=None, metadata=None, mount_accessor=None, name=None):  # noqa: E501
        """Body34 - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._metadata = None
        self._mount_accessor = None
        self._name = None
        self.discriminator = None
        if entity_id is not None:
            self.entity_id = entity_id
        if metadata is not None:
            self.metadata = metadata
        if mount_accessor is not None:
            self.mount_accessor = mount_accessor
        if name is not None:
            self.name = name

    @property
    def entity_id(self):
        """Gets the entity_id of this Body34.  # noqa: E501

        Entity ID to which this persona should be tied to  # noqa: E501

        :return: The entity_id of this Body34.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Body34.

        Entity ID to which this persona should be tied to  # noqa: E501

        :param entity_id: The entity_id of this Body34.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def metadata(self):
        """Gets the metadata of this Body34.  # noqa: E501

        Metadata to be associated with the persona. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault <command> <path> metadata=key1=value1 metadata=key2=value2  # noqa: E501

        :return: The metadata of this Body34.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Body34.

        Metadata to be associated with the persona. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault <command> <path> metadata=key1=value1 metadata=key2=value2  # noqa: E501

        :param metadata: The metadata of this Body34.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def mount_accessor(self):
        """Gets the mount_accessor of this Body34.  # noqa: E501

        Mount accessor to which this persona belongs to  # noqa: E501

        :return: The mount_accessor of this Body34.  # noqa: E501
        :rtype: str
        """
        return self._mount_accessor

    @mount_accessor.setter
    def mount_accessor(self, mount_accessor):
        """Sets the mount_accessor of this Body34.

        Mount accessor to which this persona belongs to  # noqa: E501

        :param mount_accessor: The mount_accessor of this Body34.  # noqa: E501
        :type: str
        """

        self._mount_accessor = mount_accessor

    @property
    def name(self):
        """Gets the name of this Body34.  # noqa: E501

        Name of the persona  # noqa: E501

        :return: The name of this Body34.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body34.

        Name of the persona  # noqa: E501

        :param name: The name of this Body34.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(Body34, dict):
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
        if not isinstance(other, Body34):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
