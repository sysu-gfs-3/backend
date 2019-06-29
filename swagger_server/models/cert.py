# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Cert(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, user_id: str = None, files: List[str] = None, remarks: str = None
    ):  # noqa: E501
        """Cert - a model defined in Swagger

        :param user_id: The user_id of this Cert.  # noqa: E501
        :type user_id: str
        :param files: The files of this Cert.  # noqa: E501
        :type files: List[str]
        :param remarks: The remarks of this Cert.  # noqa: E501
        :type remarks: str
        """
        self.swagger_types = {"user_id": str, "files": List[str], "remarks": str}

        self.attribute_map = {
            "user_id": "userId",
            "files": "files",
            "remarks": "remarks",
        }

        self._user_id = user_id
        self._files = files
        self._remarks = remarks

    @classmethod
    def from_dict(cls, dikt) -> "Cert":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cert of this Cert.  # noqa: E501
        :rtype: Cert
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Cert.


        :return: The user_id of this Cert.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Cert.


        :param user_id: The user_id of this Cert.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def files(self) -> List[str]:
        """Gets the files of this Cert.


        :return: The files of this Cert.
        :rtype: List[str]
        """
        return self._files

    @files.setter
    def files(self, files: List[str]):
        """Sets the files of this Cert.


        :param files: The files of this Cert.
        :type files: List[str]
        """

        self._files = files

    @property
    def remarks(self) -> str:
        """Gets the remarks of this Cert.


        :return: The remarks of this Cert.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks: str):
        """Sets the remarks of this Cert.


        :param remarks: The remarks of this Cert.
        :type remarks: str
        """

        self._remarks = remarks
