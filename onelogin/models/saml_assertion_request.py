# coding: utf-8

"""
    OneLogin API

    This is an administrative API for OneLogin customers  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from onelogin.configuration import Configuration


class SamlAssertionRequest(object):
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
        'username_or_email': 'str',
        'password': 'str',
        'subdomain': 'str',
        'app_id': 'int',
        'ip_address': 'str'
    }

    attribute_map = {
        'username_or_email': 'username_or_email',
        'password': 'password',
        'subdomain': 'subdomain',
        'app_id': 'app_id',
        'ip_address': 'ip_address'
    }

    def __init__(self, username_or_email=None, password=None, subdomain=None, app_id=None, ip_address=None, _configuration=None):  # noqa: E501
        """SamlAssertionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username_or_email = None
        self._password = None
        self._subdomain = None
        self._app_id = None
        self._ip_address = None
        self.discriminator = None

        self.username_or_email = username_or_email
        self.password = password
        self.subdomain = subdomain
        self.app_id = app_id
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def username_or_email(self):
        """Gets the username_or_email of this SamlAssertionRequest.  # noqa: E501

        Set to the username or email of the user that you want to log in.  # noqa: E501

        :return: The username_or_email of this SamlAssertionRequest.  # noqa: E501
        :rtype: str
        """
        return self._username_or_email

    @username_or_email.setter
    def username_or_email(self, username_or_email):
        """Sets the username_or_email of this SamlAssertionRequest.

        Set to the username or email of the user that you want to log in.  # noqa: E501

        :param username_or_email: The username_or_email of this SamlAssertionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username_or_email is None:
            raise ValueError("Invalid value for `username_or_email`, must not be `None`")  # noqa: E501

        self._username_or_email = username_or_email

    @property
    def password(self):
        """Gets the password of this SamlAssertionRequest.  # noqa: E501

        Set to the password of the user that you want to log in.  # noqa: E501

        :return: The password of this SamlAssertionRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SamlAssertionRequest.

        Set to the password of the user that you want to log in.  # noqa: E501

        :param password: The password of this SamlAssertionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def subdomain(self):
        """Gets the subdomain of this SamlAssertionRequest.  # noqa: E501

        Set to the subdomain of the user that you want to log in.  # noqa: E501

        :return: The subdomain of this SamlAssertionRequest.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this SamlAssertionRequest.

        Set to the subdomain of the user that you want to log in.  # noqa: E501

        :param subdomain: The subdomain of this SamlAssertionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subdomain is None:
            raise ValueError("Invalid value for `subdomain`, must not be `None`")  # noqa: E501

        self._subdomain = subdomain

    @property
    def app_id(self):
        """Gets the app_id of this SamlAssertionRequest.  # noqa: E501

        App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin.  # noqa: E501

        :return: The app_id of this SamlAssertionRequest.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SamlAssertionRequest.

        App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin.  # noqa: E501

        :param app_id: The app_id of this SamlAssertionRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def ip_address(self):
        """Gets the ip_address of this SamlAssertionRequest.  # noqa: E501

        If you are using this API in a scenario in which MFA is required and you’ll need to be able to honor IP address whitelisting defined in MFA policies, provide this parameter and set its value to the whitelisted IP address that needs to be bypassed.  # noqa: E501

        :return: The ip_address of this SamlAssertionRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SamlAssertionRequest.

        If you are using this API in a scenario in which MFA is required and you’ll need to be able to honor IP address whitelisting defined in MFA policies, provide this parameter and set its value to the whitelisted IP address that needs to be bypassed.  # noqa: E501

        :param ip_address: The ip_address of this SamlAssertionRequest.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

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
        if issubclass(SamlAssertionRequest, dict):
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
        if not isinstance(other, SamlAssertionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SamlAssertionRequest):
            return True

        return self.to_dict() != other.to_dict()
