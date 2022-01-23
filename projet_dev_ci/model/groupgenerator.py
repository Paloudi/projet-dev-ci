#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module generating groups
"""

import string
from typing import List
from projet_dev_ci.model.group import Group
from projet_dev_ci.model.user import User


class GroupGenerator:
    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """

    # region Constructors

    def __init__(self, users_list: List[User], groups_size: int, last_param: string) -> None:
        """
        Creates a new Group_generator object with a given number of users and number of groups
        :param users_list: List of users
        :param groups_size: Desired size of the groups
        :param last_param: The way of handling last group size
        :type users_list: List[User]
        :type groups_size: int
        :type last_param: string
        """
        super().__init__()
        if users_list and isinstance(users_list, List) and len(users_list) > 0 and \
                groups_size and isinstance(groups_size, int) and groups_size > 0 and \
                last_param and isinstance(last_param, str) and \
                last_param in ('LAST_MIN', 'LAST_MAX'):

            self.__users_list = users_list
            self.__users_number = len(self.__users_list)
            self.__last_param = last_param
            self.__groups_list: List[Group] = []
            self.__number_of_groups = 0
            self.__last_group_size = 0
            self.__groups_size = groups_size

            self.number_of_groups_calculator(self.__users_number, self.__groups_size, self.__last_param)
            self.create_groups(self.__groups_list)
            self.set_size_of_groups(self.__groups_list)

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

    def get_number_of_groups(self) -> int:
        """
        Returns the number of groups
        :return: the number of groups
        :rtype: int
        """
        return self.__number_of_groups

    def get_last_group(self) -> Group:
        """
        Returns the number of groups
        :return: the number of groups
        :rtype: int
        """
        last_group = self.get_groups_list()

        return last_group[-1]

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

    def set_last_element_groups_list(self, groups_list: List[Group]):
        """
        set the last element of the list of Groups
        """
        self.__groups_list = groups_list

    def set_number_of_groups(self, groups_number: int):
        """
        set the number of groups
        """
        self.__number_of_groups = groups_number

    # endregion

    # region Methods

    def number_of_groups_calculator(self, users_number: int, groups_size: int, last_param):
        """
        Calculation of group dimensions
        :param users_number: Number of users
        :param groups_size: Desired size of the groups
        :param last_param: The way of handling last group size
        :type users_number: int
        :type groups_size: int
        :type last_param: string
        """
        groups_number = 0
        list_of_number_of_groups = []
        list_of_size_of_groups = []
        if users_number % int((users_number / groups_size)) == 0:
            self.__number_of_groups = (users_number / groups_size)
            self.__groups_size = groups_size
            self.__last_group_size = self.__groups_size
            print("Taille des groupes : ", self.__groups_size, " Nombre de groupes : ", self.__number_of_groups, "Taille du dernier groupe : ", self.__last_group_size)
            return
        if last_param == "LAST_MAX":
            for number_of_groups_loop in range(users_number):
                for groups_size_loop in range(users_number):
                    if (number_of_groups_loop * groups_size_loop) == users_number:
                        print("C'est gagné ! -> X : ", number_of_groups_loop, " Y : ", groups_size_loop)
                        list_of_number_of_groups.append(number_of_groups_loop)
                        list_of_size_of_groups.append(groups_size_loop)
                    if (number_of_groups_loop * groups_size_loop) == (users_number - 1):
                        print("C'est gagné ! -> X : ", number_of_groups_loop, " Y : ", groups_size_loop)
                        list_of_number_of_groups.append(number_of_groups_loop)
                        list_of_size_of_groups.append(groups_size_loop)
                if groups_number != 0:
                    break

        if last_param == "LAST_MIN":
            for number_of_groups_loop in range(users_number):
                for groups_size_loop in range(users_number):
                    # print("X = ", number_of_groups_loop, "Y = " , groups_size_loop , "X*Y = ", number_of_groups_loop*groups_size_loop)
                    if (number_of_groups_loop * groups_size_loop) == users_number:
                        print("C'est gagné ! -> X : ", number_of_groups_loop, " Y : ", groups_size_loop)
                        list_of_number_of_groups.append(number_of_groups_loop)
                        list_of_size_of_groups.append(groups_size_loop)
                    if (number_of_groups_loop * groups_size_loop) == (users_number + 1):
                        print("C'est gagné ! -> X : ", number_of_groups_loop, " Y : ", groups_size_loop)
                        list_of_number_of_groups.append(number_of_groups_loop)
                        list_of_size_of_groups.append(groups_size_loop)
                if groups_number != 0:
                    break
        if last_param not in ('LAST_MIN', 'LAST_MAX'):
            print("IMPOSSIBLE")
            return

        result = min(list_of_size_of_groups,
                     key=lambda z: abs(z - groups_size))  # Find closest number to the specified one from the list
        self.__groups_size = list_of_size_of_groups[list_of_number_of_groups.index(result)]
        self.__number_of_groups = result
        self.__users_number = users_number

        if users_number % self.__number_of_groups != 0:
            if last_param == "LAST_MIN":
                self.__last_group_size = self.__groups_size - 1
            if last_param == "LAST_MAX":
                self.__last_group_size = self.__groups_size + 1
        else:
            self.__last_group_size = self.__groups_size

        print("Number of users : ", self.__users_number," Groups size : ", self.__groups_size, " Number of groups : ", self.__number_of_groups,
              " Size of the last group : ", self.__last_group_size, "| Calculation : ", self.__groups_size, " * ", (self.__number_of_groups - 1), " + ", self.__last_group_size,  " = ", (self.__groups_size * (self.__number_of_groups - 1) + self.__last_group_size))

    def create_groups(self, groups_list: List[Group]) -> None:
        for i in range(self.__number_of_groups):
            groups_list.append(Group(self.__groups_size))
        self.set_groups_list(groups_list)

    def set_size_of_groups(self, groups_list: List[Group]):
        """
        Set max size of groups
        :param groups_list: List of the groups
        :type groups_list: List[Group]
        """
        for group in groups_list:
            group.set_max_size(self.__groups_size)
        if self.__last_group_size != groups_list[-1].get_max_size():
            groups_list[-1].set_max_size(self.__last_group_size)
        for group in groups_list:
            print(group.get_max_size())

    def fill_groups(self, list_users: List[User]) -> None:
        users_list = list_users
        groups_list = self.get_groups_list
        filled_groups = 0
        # Fill groups with users
        for i in range(len(users_list)):
            if groups_list[filled_groups].get_current_size() < groups_list:
                groups_list[filled_groups].add_user(users_list[i])
            else:
                filled_groups += 1
                groups_list[filled_groups].add_user(users_list[i])
        self.set_groups_list(groups_list)

    @classmethod
    def add_to_group(cls, new_user: User, group: Group) -> None:
        """
        Add a user to an existing group
        :param new_user: user to add in the existing group
        :param group: group which the user will be added to
        :type new_user: User
        :type group: Group
        """
        group.add_user(new_user)

    # endregion
