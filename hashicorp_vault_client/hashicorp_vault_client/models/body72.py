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


class Body72(object):
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
        'allowed_response_headers': 'list[str]',
        'audit_non_hmac_request_keys': 'list[str]',
        'audit_non_hmac_response_keys': 'list[str]',
        'default_lease_ttl': 'str',
        'description': 'str',
        'listing_visibility': 'str',
        'max_lease_ttl': 'str',
        'options': 'object',
        'passthrough_request_headers': 'list[str]',
        'token_type': 'str'
    }

    attribute_map = {
        'allowed_response_headers': 'allowed_response_headers',
        'audit_non_hmac_request_keys': 'audit_non_hmac_request_keys',
        'audit_non_hmac_response_keys': 'audit_non_hmac_response_keys',
        'default_lease_ttl': 'default_lease_ttl',
        'description': 'description',
        'listing_visibility': 'listing_visibility',
        'max_lease_ttl': 'max_lease_ttl',
        'options': 'options',
        'passthrough_request_headers': 'passthrough_request_headers',
        'token_type': 'token_type'
    }

    def __init__(self, allowed_response_headers=None, audit_non_hmac_request_keys=None, audit_non_hmac_response_keys=None, default_lease_ttl=None, description=None, listing_visibility=None, max_lease_ttl=None, options=None, passthrough_request_headers=None, token_type=None):  # noqa: E501
        """Body72 - a model defined in Swagger"""  # noqa: E501
        self._allowed_response_headers = None
        self._audit_non_hmac_request_keys = None
        self._audit_non_hmac_response_keys = None
        self._default_lease_ttl = None
        self._description = None
        self._listing_visibility = None
        self._max_lease_ttl = None
        self._options = None
        self._passthrough_request_headers = None
        self._token_type = None
        self.discriminator = None
        if allowed_response_headers is not None:
            self.allowed_response_headers = allowed_response_headers
        if audit_non_hmac_request_keys is not None:
            self.audit_non_hmac_request_keys = audit_non_hmac_request_keys
        if audit_non_hmac_response_keys is not None:
            self.audit_non_hmac_response_keys = audit_non_hmac_response_keys
        if default_lease_ttl is not None:
            self.default_lease_ttl = default_lease_ttl
        if description is not None:
            self.description = description
        if listing_visibility is not None:
            self.listing_visibility = listing_visibility
        if max_lease_ttl is not None:
            self.max_lease_ttl = max_lease_ttl
        if options is not None:
            self.options = options
        if passthrough_request_headers is not None:
            self.passthrough_request_headers = passthrough_request_headers
        if token_type is not None:
            self.token_type = token_type

    @property
    def allowed_response_headers(self):
        """Gets the allowed_response_headers of this Body72.  # noqa: E501

        A list of headers to whitelist and allow a plugin to set on responses.  # noqa: E501

        :return: The allowed_response_headers of this Body72.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_response_headers

    @allowed_response_headers.setter
    def allowed_response_headers(self, allowed_response_headers):
        """Sets the allowed_response_headers of this Body72.

        A list of headers to whitelist and allow a plugin to set on responses.  # noqa: E501

        :param allowed_response_headers: The allowed_response_headers of this Body72.  # noqa: E501
        :type: list[str]
        """

        self._allowed_response_headers = allowed_response_headers

    @property
    def audit_non_hmac_request_keys(self):
        """Gets the audit_non_hmac_request_keys of this Body72.  # noqa: E501

        The list of keys in the request data object that will not be HMAC'ed by audit devices.  # noqa: E501

        :return: The audit_non_hmac_request_keys of this Body72.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_non_hmac_request_keys

    @audit_non_hmac_request_keys.setter
    def audit_non_hmac_request_keys(self, audit_non_hmac_request_keys):
        """Sets the audit_non_hmac_request_keys of this Body72.

        The list of keys in the request data object that will not be HMAC'ed by audit devices.  # noqa: E501

        :param audit_non_hmac_request_keys: The audit_non_hmac_request_keys of this Body72.  # noqa: E501
        :type: list[str]
        """

        self._audit_non_hmac_request_keys = audit_non_hmac_request_keys

    @property
    def audit_non_hmac_response_keys(self):
        """Gets the audit_non_hmac_response_keys of this Body72.  # noqa: E501

        The list of keys in the response data object that will not be HMAC'ed by audit devices.  # noqa: E501

        :return: The audit_non_hmac_response_keys of this Body72.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_non_hmac_response_keys

    @audit_non_hmac_response_keys.setter
    def audit_non_hmac_response_keys(self, audit_non_hmac_response_keys):
        """Sets the audit_non_hmac_response_keys of this Body72.

        The list of keys in the response data object that will not be HMAC'ed by audit devices.  # noqa: E501

        :param audit_non_hmac_response_keys: The audit_non_hmac_response_keys of this Body72.  # noqa: E501
        :type: list[str]
        """

        self._audit_non_hmac_response_keys = audit_non_hmac_response_keys

    @property
    def default_lease_ttl(self):
        """Gets the default_lease_ttl of this Body72.  # noqa: E501

        The default lease TTL for this mount.  # noqa: E501

        :return: The default_lease_ttl of this Body72.  # noqa: E501
        :rtype: str
        """
        return self._default_lease_ttl

    @default_lease_ttl.setter
    def default_lease_ttl(self, default_lease_ttl):
        """Sets the default_lease_ttl of this Body72.

        The default lease TTL for this mount.  # noqa: E501

        :param default_lease_ttl: The default_lease_ttl of this Body72.  # noqa: E501
        :type: str
        """

        self._default_lease_ttl = default_lease_ttl

    @property
    def description(self):
        """Gets the description of this Body72.  # noqa: E501

        User-friendly description for this credential backend.  # noqa: E501

        :return: The description of this Body72.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body72.

        User-friendly description for this credential backend.  # noqa: E501

        :param description: The description of this Body72.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def listing_visibility(self):
        """Gets the listing_visibility of this Body72.  # noqa: E501

        Determines the visibility of the mount in the UI-specific listing endpoint. Accepted value are 'unauth' and ''.  # noqa: E501

        :return: The listing_visibility of this Body72.  # noqa: E501
        :rtype: str
        """
        return self._listing_visibility

    @listing_visibility.setter
    def listing_visibility(self, listing_visibility):
        """Sets the listing_visibility of this Body72.

        Determines the visibility of the mount in the UI-specific listing endpoint. Accepted value are 'unauth' and ''.  # noqa: E501

        :param listing_visibility: The listing_visibility of this Body72.  # noqa: E501
        :type: str
        """

        self._listing_visibility = listing_visibility

    @property
    def max_lease_ttl(self):
        """Gets the max_lease_ttl of this Body72.  # noqa: E501

        The max lease TTL for this mount.  # noqa: E501

        :return: The max_lease_ttl of this Body72.  # noqa: E501
        :rtype: str
        """
        return self._max_lease_ttl

    @max_lease_ttl.setter
    def max_lease_ttl(self, max_lease_ttl):
        """Sets the max_lease_ttl of this Body72.

        The max lease TTL for this mount.  # noqa: E501

        :param max_lease_ttl: The max_lease_ttl of this Body72.  # noqa: E501
        :type: str
        """

        self._max_lease_ttl = max_lease_ttl

    @property
    def options(self):
        """Gets the options of this Body72.  # noqa: E501

        The options to pass into the backend. Should be a json object with string keys and values.  # noqa: E501

        :return: The options of this Body72.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Body72.

        The options to pass into the backend. Should be a json object with string keys and values.  # noqa: E501

        :param options: The options of this Body72.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def passthrough_request_headers(self):
        """Gets the passthrough_request_headers of this Body72.  # noqa: E501

        A list of headers to whitelist and pass from the request to the plugin.  # noqa: E501

        :return: The passthrough_request_headers of this Body72.  # noqa: E501
        :rtype: list[str]
        """
        return self._passthrough_request_headers

    @passthrough_request_headers.setter
    def passthrough_request_headers(self, passthrough_request_headers):
        """Sets the passthrough_request_headers of this Body72.

        A list of headers to whitelist and pass from the request to the plugin.  # noqa: E501

        :param passthrough_request_headers: The passthrough_request_headers of this Body72.  # noqa: E501
        :type: list[str]
        """

        self._passthrough_request_headers = passthrough_request_headers

    @property
    def token_type(self):
        """Gets the token_type of this Body72.  # noqa: E501

        The type of token to issue (service or batch).  # noqa: E501

        :return: The token_type of this Body72.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Body72.

        The type of token to issue (service or batch).  # noqa: E501

        :param token_type: The token_type of this Body72.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

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
        if issubclass(Body72, dict):
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
        if not isinstance(other, Body72):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
