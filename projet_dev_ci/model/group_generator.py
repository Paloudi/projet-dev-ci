#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module generating groups
"""

import string
from projet_dev_ci.model.group import Group
from projet_dev_ci.model.user import User
from typing import List

class group_generator:

    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """
    # region Constructors

    def __init__(self, users_number : int, groups_number : int, last_param : string) -> None:
        """
        Creates a new Group_generator object with a given number of users and number of groups
        :param users_number: The amount of users
        :param groups_number: The amount of groups
        :param last_param: The way of handling last group size
        :type users_number: int
        :type groups_number: int
        :type last_param: string
        """
        super().__init__()
        if users_number and isinstance(users_number, int) and users_number > 0 and \
            groups_number and isinstance(groups_number, int) and groups_number > 0 and \
            last_param and isinstance(last_param, string) and (last_param == "LAST_MIN" or last_param == "LAST_MAX"):

            self.__users_number = users_number
            self.__groups_number = groups_number
            self.__last_param = last_param
        else:
            raise ValueError("Parameters are invalid")

    # endregion

    # region getters

    def get_last_param(self) -> string:
            """
            Returns the last param of the group
            :return: last param of the group
            :rtype: string
            """
            return self.__last_param

    # endregion

    # region setters

    def set_last_param(self, last_param: string):
        """
        set the last param of the group
        """
        self.__last_param = last_param

    # endregion

    # region methods

    def last_group_gestion(self, users_number : int, groups_number : int):
        if users_number % groups_number != 0:
            return
        if group.get_last_param == "LAST_MIN":
            print("blabla")
        if group.get_last_param == "LAST_MAX":
            print("blabla")

    #endrehion