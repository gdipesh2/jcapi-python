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


class SystemInsightsDiskEncryption(object):
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
        'name': 'str',
        'uuid': 'str',
        'encrypted': 'int',
        'type': 'str',
        'uid': 'str',
        'user_uuid': 'str',
        'encryption_status': 'str',
        'jc_collection_time': 'str',
        'jc_system_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'encrypted': 'encrypted',
        'type': 'type',
        'uid': 'uid',
        'user_uuid': 'user_uuid',
        'encryption_status': 'encryption_status',
        'jc_collection_time': 'jc_collection_time',
        'jc_system_id': 'jc_system_id'
    }

    def __init__(self, name=None, uuid=None, encrypted=None, type=None, uid=None, user_uuid=None, encryption_status=None, jc_collection_time=None, jc_system_id=None):  # noqa: E501
        """SystemInsightsDiskEncryption - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._encrypted = None
        self._type = None
        self._uid = None
        self._user_uuid = None
        self._encryption_status = None
        self._jc_collection_time = None
        self._jc_system_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if encrypted is not None:
            self.encrypted = encrypted
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if encryption_status is not None:
            self.encryption_status = encryption_status
        if jc_collection_time is not None:
            self.jc_collection_time = jc_collection_time
        if jc_system_id is not None:
            self.jc_system_id = jc_system_id

    @property
    def name(self):
        """Gets the name of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The name of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsDiskEncryption.


        :param name: The name of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The uuid of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SystemInsightsDiskEncryption.


        :param uuid: The uuid of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def encrypted(self):
        """Gets the encrypted of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The encrypted of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: int
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this SystemInsightsDiskEncryption.


        :param encrypted: The encrypted of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: int
        """

        self._encrypted = encrypted

    @property
    def type(self):
        """Gets the type of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The type of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsDiskEncryption.


        :param type: The type of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The uid of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SystemInsightsDiskEncryption.


        :param uid: The uid of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The user_uuid of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SystemInsightsDiskEncryption.


        :param user_uuid: The user_uuid of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def encryption_status(self):
        """Gets the encryption_status of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The encryption_status of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._encryption_status

    @encryption_status.setter
    def encryption_status(self, encryption_status):
        """Sets the encryption_status of this SystemInsightsDiskEncryption.


        :param encryption_status: The encryption_status of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._encryption_status = encryption_status

    @property
    def jc_collection_time(self):
        """Gets the jc_collection_time of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The jc_collection_time of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._jc_collection_time

    @jc_collection_time.setter
    def jc_collection_time(self, jc_collection_time):
        """Sets the jc_collection_time of this SystemInsightsDiskEncryption.


        :param jc_collection_time: The jc_collection_time of this SystemInsightsDiskEncryption.  # noqa: E501
        :type: str
        """

        self._jc_collection_time = jc_collection_time

    @property
    def jc_system_id(self):
        """Gets the jc_system_id of this SystemInsightsDiskEncryption.  # noqa: E501


        :return: The jc_system_id of this SystemInsightsDiskEncryption.  # noqa: E501
        :rtype: str
        """
        return self._jc_system_id

    @jc_system_id.setter
    def jc_system_id(self, jc_system_id):
        """Sets the jc_system_id of this SystemInsightsDiskEncryption.


        :param jc_system_id: The jc_system_id of this SystemInsightsDiskEncryption.  # noqa: E501
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
        if issubclass(SystemInsightsDiskEncryption, dict):
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
        if not isinstance(other, SystemInsightsDiskEncryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
