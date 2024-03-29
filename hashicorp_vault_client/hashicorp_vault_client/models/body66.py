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


class Body66(object):
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
        'api_token': 'str',
        'base_url': 'str',
        'mount_accessor': 'str',
        'org_name': 'str',
        'primary_email': 'bool',
        'production': 'bool',
        'username_format': 'str'
    }

    attribute_map = {
        'api_token': 'api_token',
        'base_url': 'base_url',
        'mount_accessor': 'mount_accessor',
        'org_name': 'org_name',
        'primary_email': 'primary_email',
        'production': 'production',
        'username_format': 'username_format'
    }

    def __init__(self, api_token=None, base_url=None, mount_accessor=None, org_name=None, primary_email=None, production=None, username_format=None):  # noqa: E501
        """Body66 - a model defined in Swagger"""  # noqa: E501
        self._api_token = None
        self._base_url = None
        self._mount_accessor = None
        self._org_name = None
        self._primary_email = None
        self._production = None
        self._username_format = None
        self.discriminator = None
        if api_token is not None:
            self.api_token = api_token
        if base_url is not None:
            self.base_url = base_url
        if mount_accessor is not None:
            self.mount_accessor = mount_accessor
        if org_name is not None:
            self.org_name = org_name
        if primary_email is not None:
            self.primary_email = primary_email
        if production is not None:
            self.production = production
        if username_format is not None:
            self.username_format = username_format

    @property
    def api_token(self):
        """Gets the api_token of this Body66.  # noqa: E501

        Okta API key.  # noqa: E501

        :return: The api_token of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this Body66.

        Okta API key.  # noqa: E501

        :param api_token: The api_token of this Body66.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def base_url(self):
        """Gets the base_url of this Body66.  # noqa: E501

        The base domain to use for the Okta API. When not specified in the configuration, \"okta.com\" is used.  # noqa: E501

        :return: The base_url of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Body66.

        The base domain to use for the Okta API. When not specified in the configuration, \"okta.com\" is used.  # noqa: E501

        :param base_url: The base_url of this Body66.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def mount_accessor(self):
        """Gets the mount_accessor of this Body66.  # noqa: E501

        The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping.  # noqa: E501

        :return: The mount_accessor of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._mount_accessor

    @mount_accessor.setter
    def mount_accessor(self, mount_accessor):
        """Sets the mount_accessor of this Body66.

        The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping.  # noqa: E501

        :param mount_accessor: The mount_accessor of this Body66.  # noqa: E501
        :type: str
        """

        self._mount_accessor = mount_accessor

    @property
    def org_name(self):
        """Gets the org_name of this Body66.  # noqa: E501

        Name of the organization to be used in the Okta API.  # noqa: E501

        :return: The org_name of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this Body66.

        Name of the organization to be used in the Okta API.  # noqa: E501

        :param org_name: The org_name of this Body66.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def primary_email(self):
        """Gets the primary_email of this Body66.  # noqa: E501

        If true, the username will only match the primary email for the account. Defaults to false.  # noqa: E501

        :return: The primary_email of this Body66.  # noqa: E501
        :rtype: bool
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """Sets the primary_email of this Body66.

        If true, the username will only match the primary email for the account. Defaults to false.  # noqa: E501

        :param primary_email: The primary_email of this Body66.  # noqa: E501
        :type: bool
        """

        self._primary_email = primary_email

    @property
    def production(self):
        """Gets the production of this Body66.  # noqa: E501

        (DEPRECATED) Use base_url instead.  # noqa: E501

        :return: The production of this Body66.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Body66.

        (DEPRECATED) Use base_url instead.  # noqa: E501

        :param production: The production of this Body66.  # noqa: E501
        :type: bool
        """

        self._production = production

    @property
    def username_format(self):
        """Gets the username_format of this Body66.  # noqa: E501

        A format string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \"{{alias.name}}@example.com\". Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias's name field will be used as-is.  # noqa: E501

        :return: The username_format of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._username_format

    @username_format.setter
    def username_format(self, username_format):
        """Sets the username_format of this Body66.

        A format string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \"{{alias.name}}@example.com\". Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias's name field will be used as-is.  # noqa: E501

        :param username_format: The username_format of this Body66.  # noqa: E501
        :type: str
        """

        self._username_format = username_format

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
        if issubclass(Body66, dict):
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
        if not isinstance(other, Body66):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
