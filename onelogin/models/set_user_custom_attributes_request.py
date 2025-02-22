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


class SetUserCustomAttributesRequest(object):
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
        'custom_attributes': 'dict(str, str)'
    }

    attribute_map = {
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, custom_attributes=None, _configuration=None):  # noqa: E501
        """SetUserCustomAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_attributes = None
        self.discriminator = None

        self.custom_attributes = custom_attributes

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this SetUserCustomAttributesRequest.  # noqa: E501

        The attributes to set  # noqa: E501

        :return: The custom_attributes of this SetUserCustomAttributesRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this SetUserCustomAttributesRequest.

        The attributes to set  # noqa: E501

        :param custom_attributes: The custom_attributes of this SetUserCustomAttributesRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if self._configuration.client_side_validation and custom_attributes is None:
            raise ValueError("Invalid value for `custom_attributes`, must not be `None`")  # noqa: E501

        self._custom_attributes = custom_attributes

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
        if issubclass(SetUserCustomAttributesRequest, dict):
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
        if not isinstance(other, SetUserCustomAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetUserCustomAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
