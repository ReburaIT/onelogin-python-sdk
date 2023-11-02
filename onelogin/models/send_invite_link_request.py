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


class SendInviteLinkRequest(object):
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
        'email': 'str',
        'personal_email': 'str'
    }

    attribute_map = {
        'email': 'email',
        'personal_email': 'personal_email'
    }

    def __init__(self, email=None, personal_email=None, _configuration=None):  # noqa: E501
        """SendInviteLinkRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._personal_email = None
        self.discriminator = None

        self.email = email
        if personal_email is not None:
            self.personal_email = personal_email

    @property
    def email(self):
        """Gets the email of this SendInviteLinkRequest.  # noqa: E501

        Set to the user email address to generate an invite link.  # noqa: E501

        :return: The email of this SendInviteLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SendInviteLinkRequest.

        Set to the user email address to generate an invite link.  # noqa: E501

        :param email: The email of this SendInviteLinkRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def personal_email(self):
        """Gets the personal_email of this SendInviteLinkRequest.  # noqa: E501

        To send an invite email to a different address than the one provided in email, provide it here. The invite link is sent to this address instead.  # noqa: E501

        :return: The personal_email of this SendInviteLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """Sets the personal_email of this SendInviteLinkRequest.

        To send an invite email to a different address than the one provided in email, provide it here. The invite link is sent to this address instead.  # noqa: E501

        :param personal_email: The personal_email of this SendInviteLinkRequest.  # noqa: E501
        :type: str
        """

        self._personal_email = personal_email

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
        if issubclass(SendInviteLinkRequest, dict):
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
        if not isinstance(other, SendInviteLinkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendInviteLinkRequest):
            return True

        return self.to_dict() != other.to_dict()
