#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the user model
"""


class User:
    """
    A user represent... a user.
    A user has a name
    """

    __id = 0

    def __init__(self, name: str) -> None:
        """
        Creates a new User object with a given name
        :param name: The name of this user
        :type name: str
        """
        super().__init__()
        if name and isinstance(name, str):
            self.__name = name
        self.__current_id = User.__id
        self.__has_a_group = True
        User.__id += 1

    def get_name(self) -> str:
        """
        Returns the name of this user
        :return: this user name
        :rtype: str
        """
        return self.__name

    def get_id(self) -> int:
        """
        Return the ID of this user
        :return: this user ID
        :rtype: int
        """
        return self.__current_id

    def get_has_a_group(self) -> bool:
        """
        Return a boolean which indicates if the user is in a group or not
        :return: this boolean "has_a_group"
        :rtype: bool
        """
        return self.__has_a_group

    @staticmethod
    def get_static_id() -> int:
        """
        Return the static id of the class
        :return: The id of the next user
        :rtype: int
        """
        return User.__id

    def set_name(self, new_name: str) -> None:
        """
        Sets the name of the user
        :param new_name: New name of the user
        :Type: Str
        """
        self.__name = new_name

    def set_has_a_group(self, has_a_group: bool) -> None:
        """
        Sets the boolean which indicates if the user has a group or not
        :param has_a_group: Information indicating if the user is in a group or not
        """
        self.__has_a_group = has_a_group
