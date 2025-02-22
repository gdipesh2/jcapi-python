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


class SystemInsightsMounts(object):
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
        'device': 'str',
        'device_alias': 'str',
        'path': 'str',
        'type': 'str',
        'blocks_size': 'str',
        'blocks': 'str',
        'blocks_free': 'str',
        'blocks_available': 'str',
        'inodes': 'str',
        'inodes_free': 'str',
        'flags': 'str',
        'jc_collection_time': 'str',
        'jc_system_id': 'str'
    }

    attribute_map = {
        'device': 'device',
        'device_alias': 'device_alias',
        'path': 'path',
        'type': 'type',
        'blocks_size': 'blocks_size',
        'blocks': 'blocks',
        'blocks_free': 'blocks_free',
        'blocks_available': 'blocks_available',
        'inodes': 'inodes',
        'inodes_free': 'inodes_free',
        'flags': 'flags',
        'jc_collection_time': 'jc_collection_time',
        'jc_system_id': 'jc_system_id'
    }

    def __init__(self, device=None, device_alias=None, path=None, type=None, blocks_size=None, blocks=None, blocks_free=None, blocks_available=None, inodes=None, inodes_free=None, flags=None, jc_collection_time=None, jc_system_id=None):  # noqa: E501
        """SystemInsightsMounts - a model defined in Swagger"""  # noqa: E501

        self._device = None
        self._device_alias = None
        self._path = None
        self._type = None
        self._blocks_size = None
        self._blocks = None
        self._blocks_free = None
        self._blocks_available = None
        self._inodes = None
        self._inodes_free = None
        self._flags = None
        self._jc_collection_time = None
        self._jc_system_id = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if device_alias is not None:
            self.device_alias = device_alias
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type
        if blocks_size is not None:
            self.blocks_size = blocks_size
        if blocks is not None:
            self.blocks = blocks
        if blocks_free is not None:
            self.blocks_free = blocks_free
        if blocks_available is not None:
            self.blocks_available = blocks_available
        if inodes is not None:
            self.inodes = inodes
        if inodes_free is not None:
            self.inodes_free = inodes_free
        if flags is not None:
            self.flags = flags
        if jc_collection_time is not None:
            self.jc_collection_time = jc_collection_time
        if jc_system_id is not None:
            self.jc_system_id = jc_system_id

    @property
    def device(self):
        """Gets the device of this SystemInsightsMounts.  # noqa: E501


        :return: The device of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this SystemInsightsMounts.


        :param device: The device of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def device_alias(self):
        """Gets the device_alias of this SystemInsightsMounts.  # noqa: E501


        :return: The device_alias of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._device_alias

    @device_alias.setter
    def device_alias(self, device_alias):
        """Sets the device_alias of this SystemInsightsMounts.


        :param device_alias: The device_alias of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._device_alias = device_alias

    @property
    def path(self):
        """Gets the path of this SystemInsightsMounts.  # noqa: E501


        :return: The path of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsMounts.


        :param path: The path of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this SystemInsightsMounts.  # noqa: E501


        :return: The type of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsMounts.


        :param type: The type of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def blocks_size(self):
        """Gets the blocks_size of this SystemInsightsMounts.  # noqa: E501


        :return: The blocks_size of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._blocks_size

    @blocks_size.setter
    def blocks_size(self, blocks_size):
        """Sets the blocks_size of this SystemInsightsMounts.


        :param blocks_size: The blocks_size of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._blocks_size = blocks_size

    @property
    def blocks(self):
        """Gets the blocks of this SystemInsightsMounts.  # noqa: E501


        :return: The blocks of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this SystemInsightsMounts.


        :param blocks: The blocks of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._blocks = blocks

    @property
    def blocks_free(self):
        """Gets the blocks_free of this SystemInsightsMounts.  # noqa: E501


        :return: The blocks_free of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._blocks_free

    @blocks_free.setter
    def blocks_free(self, blocks_free):
        """Sets the blocks_free of this SystemInsightsMounts.


        :param blocks_free: The blocks_free of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._blocks_free = blocks_free

    @property
    def blocks_available(self):
        """Gets the blocks_available of this SystemInsightsMounts.  # noqa: E501


        :return: The blocks_available of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._blocks_available

    @blocks_available.setter
    def blocks_available(self, blocks_available):
        """Sets the blocks_available of this SystemInsightsMounts.


        :param blocks_available: The blocks_available of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._blocks_available = blocks_available

    @property
    def inodes(self):
        """Gets the inodes of this SystemInsightsMounts.  # noqa: E501


        :return: The inodes of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._inodes

    @inodes.setter
    def inodes(self, inodes):
        """Sets the inodes of this SystemInsightsMounts.


        :param inodes: The inodes of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._inodes = inodes

    @property
    def inodes_free(self):
        """Gets the inodes_free of this SystemInsightsMounts.  # noqa: E501


        :return: The inodes_free of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._inodes_free

    @inodes_free.setter
    def inodes_free(self, inodes_free):
        """Sets the inodes_free of this SystemInsightsMounts.


        :param inodes_free: The inodes_free of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._inodes_free = inodes_free

    @property
    def flags(self):
        """Gets the flags of this SystemInsightsMounts.  # noqa: E501


        :return: The flags of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this SystemInsightsMounts.


        :param flags: The flags of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._flags = flags

    @property
    def jc_collection_time(self):
        """Gets the jc_collection_time of this SystemInsightsMounts.  # noqa: E501


        :return: The jc_collection_time of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._jc_collection_time

    @jc_collection_time.setter
    def jc_collection_time(self, jc_collection_time):
        """Sets the jc_collection_time of this SystemInsightsMounts.


        :param jc_collection_time: The jc_collection_time of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._jc_collection_time = jc_collection_time

    @property
    def jc_system_id(self):
        """Gets the jc_system_id of this SystemInsightsMounts.  # noqa: E501


        :return: The jc_system_id of this SystemInsightsMounts.  # noqa: E501
        :rtype: str
        """
        return self._jc_system_id

    @jc_system_id.setter
    def jc_system_id(self, jc_system_id):
        """Sets the jc_system_id of this SystemInsightsMounts.


        :param jc_system_id: The jc_system_id of this SystemInsightsMounts.  # noqa: E501
        :type: str
        """

        self._jc_system_id = jc_system_id

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
        if issubclass(SystemInsightsMounts, dict):
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
        if not isinstance(other, SystemInsightsMounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
