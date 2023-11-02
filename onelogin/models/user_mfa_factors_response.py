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


class UserMfaFactorsResponse(object):
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
        'status': 'Status',
        'data': 'UserMfaFactorsResponseData'
    }

    attribute_map = {
        'status': 'status',
        'data': 'data'
    }

    def __init__(self, status=None, data=None, _configuration=None):  # noqa: E501
        """UserMfaFactorsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._data = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if data is not None:
            self.data = data

    @property
    def status(self):
        """Gets the status of this UserMfaFactorsResponse.  # noqa: E501


        :return: The status of this UserMfaFactorsResponse.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserMfaFactorsResponse.


        :param status: The status of this UserMfaFactorsResponse.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def data(self):
        """Gets the data of this UserMfaFactorsResponse.  # noqa: E501


        :return: The data of this UserMfaFactorsResponse.  # noqa: E501
        :rtype: UserMfaFactorsResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserMfaFactorsResponse.


        :param data: The data of this UserMfaFactorsResponse.  # noqa: E501
        :type: UserMfaFactorsResponseData
        """

        self._data = data

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
        if issubclass(UserMfaFactorsResponse, dict):
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
        if not isinstance(other, UserMfaFactorsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMfaFactorsResponse):
            return True

        return self.to_dict() != other.to_dict()
