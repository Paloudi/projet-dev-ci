#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the user model
"""


class User:
    """
    An user represent... an user.
    An user has a name
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
