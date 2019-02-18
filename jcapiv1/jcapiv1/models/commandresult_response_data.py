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


class CommandresultResponseData(object):
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
        'output': 'str',
        'exit_code': 'int'
    }

    attribute_map = {
        'output': 'output',
        'exit_code': 'exitCode'
    }

    def __init__(self, output=None, exit_code=None):  # noqa: E501
        """CommandresultResponseData - a model defined in Swagger"""  # noqa: E501

        self._output = None
        self._exit_code = None
        self.discriminator = None

        if output is not None:
            self.output = output
        if exit_code is not None:
            self.exit_code = exit_code

    @property
    def output(self):
        """Gets the output of this CommandresultResponseData.  # noqa: E501

        The output of the command that was executed.  # noqa: E501

        :return: The output of this CommandresultResponseData.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CommandresultResponseData.

        The output of the command that was executed.  # noqa: E501

        :param output: The output of this CommandresultResponseData.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def exit_code(self):
        """Gets the exit_code of this CommandresultResponseData.  # noqa: E501

        The stderr output from the command that ran.  # noqa: E501

        :return: The exit_code of this CommandresultResponseData.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this CommandresultResponseData.

        The stderr output from the command that ran.  # noqa: E501

        :param exit_code: The exit_code of this CommandresultResponseData.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

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
        if issubclass(CommandresultResponseData, dict):
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
        if not isinstance(other, CommandresultResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
