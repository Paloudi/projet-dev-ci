#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the group model
"""

from typing import List
from projet_dev_ci.model.user import User


class Group:
    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """

    # region Constructors

    def __init__(self, size: int) -> None:
        """
        Creates a new Group object with a given size
        :param size: The max size of this group
        :type size: int
        """
        super().__init__()
        if size and isinstance(size, int) and size > 0:
            self.__max_size = size
            self.__current_size = 0
            self.__users: List[User] = []
        else:
            raise ValueError("size parameter is invalid")

    # endregion

    # region Methods

    def add_user(self, new_user: User) -> None:
        """
        Add a new user to this group
        :param new_user: an user to add to this group
        :type new_user: User
        """
        if new_user and isinstance(new_user, User):
            if self.__max_size > self.__current_size:
                self.__users.append(new_user)
                self.__current_size += 1

    # endregion

    # region Getters

    def get_users(self) -> List[User]:
        """
        Returns the list of the users of this group
        :return: This group users list
        :rtype: List[User]
        """
        return self.__users

    def get_current_size(self) -> int:
        """
        Returns the current size of this group
        :return: This group current size
        :rtype: int
        """
        return self.__current_size

    def get_max_size(self) -> int:
        """
        Returns the max size of this group
        :return: This group max size
        :rtype: int
        """
        return self.__max_size

    # endregion
