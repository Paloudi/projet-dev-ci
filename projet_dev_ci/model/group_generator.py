#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module generating groups
"""

import string
from projet_dev_ci.model import user
from projet_dev_ci.model.group import Group
from projet_dev_ci.model.user import User
from typing import List

class group_generator:

    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """
    # region Constructors

    def __init__(self, users_list : List[User], groups_number : int, last_param : string) -> None:
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
        if users_list and isinstance(users_list, List[User]) and len(users_list) > 0 and \
            groups_number and isinstance(groups_number, int) and groups_number > 0 and \
            last_param and isinstance(last_param, string) and (last_param == "LAST_MIN" or last_param == "LAST_MAX"):

            self.__users_list = users_list
            self.__users_number = len(self.__users_list)
            self.__groups_list = List[Group]
            self.__groups_number = len(self.__list_groups)
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

    def get_users_list(self) -> List[User]:
            """
            Returns the list of the users
            :return: the list of the users
            :rtype: List[User]
            """
            return self.__users_list

    def get_users_number(self) -> int:
            """
            Returns the number of users
            :return: the number of users
            :rtype: int
            """
            return self.__users_number

    def get_groups_list(self) -> List[Group]:
            """
            Returns the list of the groups
            :return: the list of the groups
            :rtype: List[Group]
            """
            return self.__groups_list

    def get_groups_number(self) -> int:
            """
            Returns the number of groups
            :return: the number of groups
            :rtype: int
            """
            return self.__users_groups

    # endregion

    # region setters

    def set_last_param(self, last_param: string):
        """
        set the last param of the group
        """
        self.__last_param = last_param

    def set_users_list(self, users_list: List[User]):
        """
        set the list of Users
        """
        self.__users_list = users_list

    def set_users_number(self, users_number: int):
        """
        set the number of users
        """
        self.__users_number = users_number

    def set_groups_list(self, groups_list: List[Group]):
        """
        set the list of Groups
        """
        self.__groups_list = groups_list

    def set_groups_number(self, groups_number: int):
        """
        set the number of groups
        """
        self.__groups_number = groups_number

    # endregion

    # region Methods

    def last_group_gestion(self):
        """
        Group gestion 
        TODO : A modifier
        """
        if self.__users_number % self.__groups_number == 0:
            return
        if self.get_last_param == "LAST_MIN":
            print("blabla")
        if self.get_last_param == "LAST_MAX":
            print("blabla")

    def add_to_group(self, new_user: User, group: Group)  -> None:
        """
        Add a user to an existing group
        :param new_user: user to add in the existing group
        :param group: group which the user will be added to 
        :type new_user: User
        :type group: Group
        """
        group.add_user(new_user)


    #endrehion