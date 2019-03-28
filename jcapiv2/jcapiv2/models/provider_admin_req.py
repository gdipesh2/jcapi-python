# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProviderAdminReq(object):
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
        'enable_multi_factor': 'bool',
        'firstname': 'str',
        'lastname': 'str'
    }

    attribute_map = {
        'email': 'email',
        'enable_multi_factor': 'enableMultiFactor',
        'firstname': 'firstname',
        'lastname': 'lastname'
    }

    def __init__(self, email=None, enable_multi_factor=None, firstname=None, lastname=None):  # noqa: E501
        """ProviderAdminReq - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._enable_multi_factor = None
        self._firstname = None
        self._lastname = None
        self.discriminator = None

        self.email = email
        if enable_multi_factor is not None:
            self.enable_multi_factor = enable_multi_factor
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname

    @property
    def email(self):
        """Gets the email of this ProviderAdminReq.  # noqa: E501


        :return: The email of this ProviderAdminReq.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProviderAdminReq.


        :param email: The email of this ProviderAdminReq.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def enable_multi_factor(self):
        """Gets the enable_multi_factor of this ProviderAdminReq.  # noqa: E501


        :return: The enable_multi_factor of this ProviderAdminReq.  # noqa: E501
        :rtype: bool
        """
        return self._enable_multi_factor

    @enable_multi_factor.setter
    def enable_multi_factor(self, enable_multi_factor):
        """Sets the enable_multi_factor of this ProviderAdminReq.


        :param enable_multi_factor: The enable_multi_factor of this ProviderAdminReq.  # noqa: E501
        :type: bool
        """

        self._enable_multi_factor = enable_multi_factor

    @property
    def firstname(self):
        """Gets the firstname of this ProviderAdminReq.  # noqa: E501


        :return: The firstname of this ProviderAdminReq.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ProviderAdminReq.


        :param firstname: The firstname of this ProviderAdminReq.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ProviderAdminReq.  # noqa: E501


        :return: The lastname of this ProviderAdminReq.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ProviderAdminReq.


        :param lastname: The lastname of this ProviderAdminReq.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

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
        if issubclass(ProviderAdminReq, dict):
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
        if not isinstance(other, ProviderAdminReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
