# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ExtraTaskInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: str=None, content: str=None):  # noqa: E501
        """ExtraTaskInfo - a model defined in Swagger

        :param user_id: The user_id of this ExtraTaskInfo.  # noqa: E501
        :type user_id: str
        :param content: The content of this ExtraTaskInfo.  # noqa: E501
        :type content: str
        """
        self.swagger_types = {
            'user_id': str,
            'content': str
        }

        self.attribute_map = {
            'user_id': 'userId',
            'content': 'content'
        }

        self._user_id = user_id
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'ExtraTaskInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExtraTaskInfo of this ExtraTaskInfo.  # noqa: E501
        :rtype: ExtraTaskInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this ExtraTaskInfo.


        :return: The user_id of this ExtraTaskInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this ExtraTaskInfo.


        :param user_id: The user_id of this ExtraTaskInfo.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def content(self) -> str:
        """Gets the content of this ExtraTaskInfo.


        :return: The content of this ExtraTaskInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this ExtraTaskInfo.


        :param content: The content of this ExtraTaskInfo.
        :type content: str
        """

        self._content = content