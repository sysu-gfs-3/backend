# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.condition import Condition  # noqa: F401,E501
from swagger_server import util


class TaskDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, wjx_id: str=None, title: str=None, desc: str=None, money: float=None, sum: int=None, part_num: int=None, condition: Condition=None):  # noqa: E501
        """TaskDetail - a model defined in Swagger

        :param type: The type of this TaskDetail.  # noqa: E501
        :type type: str
        :param wjx_id: The wjx_id of this TaskDetail.  # noqa: E501
        :type wjx_id: str
        :param title: The title of this TaskDetail.  # noqa: E501
        :type title: str
        :param desc: The desc of this TaskDetail.  # noqa: E501
        :type desc: str
        :param money: The money of this TaskDetail.  # noqa: E501
        :type money: float
        :param sum: The sum of this TaskDetail.  # noqa: E501
        :type sum: int
        :param part_num: The part_num of this TaskDetail.  # noqa: E501
        :type part_num: int
        :param condition: The condition of this TaskDetail.  # noqa: E501
        :type condition: Condition
        """
        self.swagger_types = {
            'type': str,
            'wjx_id': str,
            'title': str,
            'desc': str,
            'money': float,
            'sum': int,
            'part_num': int,
            'condition': Condition
        }

        self.attribute_map = {
            'type': 'type',
            'wjx_id': 'wjxId',
            'title': 'title',
            'desc': 'desc',
            'money': 'money',
            'sum': 'sum',
            'part_num': 'partNum',
            'condition': 'condition'
        }

        self._type = type
        self._wjx_id = wjx_id
        self._title = title
        self._desc = desc
        self._money = money
        self._sum = sum
        self._part_num = part_num
        self._condition = condition

    @classmethod
    def from_dict(cls, dikt) -> 'TaskDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TaskDetail of this TaskDetail.  # noqa: E501
        :rtype: TaskDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this TaskDetail.


        :return: The type of this TaskDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this TaskDetail.


        :param type: The type of this TaskDetail.
        :type type: str
        """

        self._type = type

    @property
    def wjx_id(self) -> str:
        """Gets the wjx_id of this TaskDetail.

        if the type is '问卷星', return wjxId.  # noqa: E501

        :return: The wjx_id of this TaskDetail.
        :rtype: str
        """
        return self._wjx_id

    @wjx_id.setter
    def wjx_id(self, wjx_id: str):
        """Sets the wjx_id of this TaskDetail.

        if the type is '问卷星', return wjxId.  # noqa: E501

        :param wjx_id: The wjx_id of this TaskDetail.
        :type wjx_id: str
        """

        self._wjx_id = wjx_id

    @property
    def title(self) -> str:
        """Gets the title of this TaskDetail.


        :return: The title of this TaskDetail.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this TaskDetail.


        :param title: The title of this TaskDetail.
        :type title: str
        """

        self._title = title

    @property
    def desc(self) -> str:
        """Gets the desc of this TaskDetail.


        :return: The desc of this TaskDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        """Sets the desc of this TaskDetail.


        :param desc: The desc of this TaskDetail.
        :type desc: str
        """

        self._desc = desc

    @property
    def money(self) -> float:
        """Gets the money of this TaskDetail.


        :return: The money of this TaskDetail.
        :rtype: float
        """
        return self._money

    @money.setter
    def money(self, money: float):
        """Sets the money of this TaskDetail.


        :param money: The money of this TaskDetail.
        :type money: float
        """

        self._money = money

    @property
    def sum(self) -> int:
        """Gets the sum of this TaskDetail.

        the num of people who have got money.  # noqa: E501

        :return: The sum of this TaskDetail.
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum: int):
        """Sets the sum of this TaskDetail.

        the num of people who have got money.  # noqa: E501

        :param sum: The sum of this TaskDetail.
        :type sum: int
        """

        self._sum = sum

    @property
    def part_num(self) -> int:
        """Gets the part_num of this TaskDetail.

        the num of participants.  # noqa: E501

        :return: The part_num of this TaskDetail.
        :rtype: int
        """
        return self._part_num

    @part_num.setter
    def part_num(self, part_num: int):
        """Sets the part_num of this TaskDetail.

        the num of participants.  # noqa: E501

        :param part_num: The part_num of this TaskDetail.
        :type part_num: int
        """

        self._part_num = part_num

    @property
    def condition(self) -> Condition:
        """Gets the condition of this TaskDetail.


        :return: The condition of this TaskDetail.
        :rtype: Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition: Condition):
        """Sets the condition of this TaskDetail.


        :param condition: The condition of this TaskDetail.
        :type condition: Condition
        """

        self._condition = condition
