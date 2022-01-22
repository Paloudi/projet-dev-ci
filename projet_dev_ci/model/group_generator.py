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


class Group_generator:
    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """

    # region Constructors

    def __init__(self, users_list: List[User], groups_size: int, last_param: string) -> None:
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
        if users_list and isinstance(users_list, List) and len(users_list) > 0 and \
                groups_size and isinstance(groups_size, int) and groups_size > 0 and \
                last_param and isinstance(last_param, str) and \
                (last_param == "LAST_MIN" or last_param == "LAST_MAX"):

            self.__users_list = users_list
            self.__users_number = len(self.__users_list)
            self.__last_param = last_param
            self.__groups_list: List[Group] = []
            self.__number_of_groups = 0
            self.__last_group_size = 0
            self.__groups_size = groups_size

            self.number_of_groups_calculator(self.__users_number, self.__groups_size, self.__last_param)

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
        return self.__groups_number

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

    def set_groups_number(self, groups_number: int):
        """
        set the number of groups
        """
        self.__groups_number = groups_number

    # endregion

    # region Methods

    def number_of_groups_calculator(self, users_number: int, groups_size: int, last_param):
        groups_number = 0
        last_group_size = groups_number
        list_of_number_of_groups = []
        list_of_size_of_groups = []
        # print("Nombre d'utilisateurs : ", users_number," Nombre de groupes : ", groups_number - 1, " Taille des groupes : ", groups_size, " Taille du dernier groupe : ", last_group_size, " Calcul : ", ((groups_number - 1) * groups_size) + last_group_size)
        if users_number % (users_number // groups_size) == 0:
            print("Taille des groupes : ", groups_size, " Nombre de groupes : ", (users_number // groups_size))
            groups_number = (users_number // groups_size)
            return
        if last_param == "LAST_MAX":
            for x in range(users_number):
                for y in range(users_number):
                    # print("X = ", x, "Y = " , y , "X*Y = ", x*y)
                    if (x * y) == users_number:
                        print("C'est gagné ! -> X : ", x, " Y : ", y)
                        list_of_number_of_groups.append(x)
                        list_of_size_of_groups.append(y)
                    if (x * y) == (users_number - 1):
                        print("C'est gagné ! -> X : ", x, " Y : ", y)
                        list_of_number_of_groups.append(x)
                        list_of_size_of_groups.append(y)
                if groups_number != 0:
                    break

        if last_param == "LAST_MIN":
            for x in range(users_number):
                for y in range(users_number):
                    # print("X = ", x, "Y = " , y , "X*Y = ", x*y)
                    if (x * y) == users_number:
                        print("C'est gagné ! -> X : ", x, " Y : ", y)
                        list_of_number_of_groups.append(x)
                        list_of_size_of_groups.append(y)
                    if (x * y) == (users_number + 1):
                        print("C'est gagné ! -> X : ", x, " Y : ", y)
                        list_of_number_of_groups.append(x)
                        list_of_size_of_groups.append(y)
                if groups_number != 0:
                    break
        if last_param != "LAST_MIN" and last_param != "LAST_MAX":
            print("IMPOSSIBLE")
            return
        # print("Liste des éléments : ")
        # for element in list_of_size_of_groups:
        #     print(element)
        result = min(list_of_size_of_groups, key=lambda z: abs(z - groups_size))  # Find closest number to the specified one from the list
        self.__groups_size = list_of_size_of_groups[list_of_number_of_groups.index(result)]
        self.__number_of_groups = result
        self.__users_number = users_number
        print("Le résultat le plus proche", "de", self.__groups_size, "est : ", result)

        if users_number % self.__number_of_groups != 0:
            if last_param == "LAST_MIN":
                self.__last_group_size = self.__groups_size - 1
            if last_param == "LAST_MAX":
                self.__last_group_size = self.__groups_size + 1
        else:
            self.__last_group_size = self.__groups_size

        print("Taille des groupes : ", self.__groups_size, " Nombre de groupes : ", self.__number_of_groups, " Taille dernier groupe : ",
              self.__last_group_size)

    # Todo : à faire
    # def fill_groups(self, list_users: List[User]) -> None:
    #     users_list = self.__users_list
    #     groups_list = self.get_groups_list
    #     filled_groups = 0
    #     # Fill groups with users
    #     for i in range(len(users_list)):
    #         if groups_list[filled_group].get_current_size() < group_size:
    #             groups_list[filled_group].add_user(users_list[i])
    #         else:
    #             filled_group += 1
    #             groups_list[filled_group].add_user(users_list[i])
    #     self.set_groups_list(groups_list)

    def add_to_group(self, new_user: User, group: Group) -> None:
        """
        Add a user to an existing group
        :param new_user: user to add in the existing group
        :param group: group which the user will be added to 
        :type new_user: User
        :type group: Group
        """
        group.add_user(new_user)

    # endregion
