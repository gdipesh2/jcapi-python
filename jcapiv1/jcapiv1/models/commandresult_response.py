# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv1.models.commandresult_response_data import CommandresultResponseData  # noqa: F401,E501


class CommandresultResponse(object):
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
        'id': 'str',
        'error': 'str',
        'data': 'CommandresultResponseData'
    }

    attribute_map = {
        'id': 'id',
        'error': 'error',
        'data': 'data'
    }

    def __init__(self, id=None, error=None, data=None):  # noqa: E501
        """CommandresultResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._error = None
        self._data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if error is not None:
            self.error = error
        if data is not None:
            self.data = data

    @property
    def id(self):
        """Gets the id of this CommandresultResponse.  # noqa: E501

        ID of the response.  # noqa: E501

        :return: The id of this CommandresultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommandresultResponse.

        ID of the response.  # noqa: E501

        :param id: The id of this CommandresultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def error(self):
        """Gets the error of this CommandresultResponse.  # noqa: E501

        The stderr output from the command that ran.  # noqa: E501

        :return: The error of this CommandresultResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CommandresultResponse.

        The stderr output from the command that ran.  # noqa: E501

        :param error: The error of this CommandresultResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def data(self):
        """Gets the data of this CommandresultResponse.  # noqa: E501


        :return: The data of this CommandresultResponse.  # noqa: E501
        :rtype: CommandresultResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CommandresultResponse.


        :param data: The data of this CommandresultResponse.  # noqa: E501
        :type: CommandresultResponseData
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
        if issubclass(CommandresultResponse, dict):
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
        if not isinstance(other, CommandresultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
