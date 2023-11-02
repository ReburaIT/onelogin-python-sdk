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


class ResponseUser(object):
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
        'id': 'int',
        'firstname': 'str',
        'lastname': 'str',
        'username': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'username': 'username',
        'email': 'email'
    }

    def __init__(self, id=None, firstname=None, lastname=None, username=None, email=None, _configuration=None):  # noqa: E501
        """ResponseUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._firstname = None
        self._lastname = None
        self._username = None
        self._email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this ResponseUser.  # noqa: E501


        :return: The id of this ResponseUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseUser.


        :param id: The id of this ResponseUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firstname(self):
        """Gets the firstname of this ResponseUser.  # noqa: E501


        :return: The firstname of this ResponseUser.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ResponseUser.


        :param firstname: The firstname of this ResponseUser.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ResponseUser.  # noqa: E501


        :return: The lastname of this ResponseUser.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ResponseUser.


        :param lastname: The lastname of this ResponseUser.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def username(self):
        """Gets the username of this ResponseUser.  # noqa: E501


        :return: The username of this ResponseUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ResponseUser.


        :param username: The username of this ResponseUser.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this ResponseUser.  # noqa: E501


        :return: The email of this ResponseUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResponseUser.


        :param email: The email of this ResponseUser.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(ResponseUser, dict):
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
        if not isinstance(other, ResponseUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseUser):
            return True

        return self.to_dict() != other.to_dict()
