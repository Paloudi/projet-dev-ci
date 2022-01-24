#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the group models
"""

from typing import List
from projet_dev_ci.models.user import User
from django.db import models


class Group(models.Model):
    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """

    max_size = models.PositiveIntegerField()
    current_size = models.PositiveIntegerField()
    users = models.TextField(null=True)

    class Meta:
        """
        Class used to modify this models table information in the database
        """
        db_table = "groups"
        app_label = "projet_dev_ci"


    # region Methods

    def add_user(self, new_user: User) -> None:
        """
        Add a new user to this group
        :param new_user: an user to add to this group
        :type new_user: User
        """
        if new_user and isinstance(new_user, User):
            if self.max_size > self.current_size:
                self.list_users.append(new_user)
                self.current_size += 1

    def remove_user(self, user_to_remove: User) -> None:
        """
        Remove a user to this group
        :param user_to_remove : an user to remove from this group
        :type user_to_remove: User
        """
        if user_to_remove and isinstance(user_to_remove, User):
            user_to_remove.set_has_a_group(False)
            self.__users.remove(user_to_remove)
            self.__current_size -= 1

    def print_list_users(self) -> None:
        """
        Print every user from the Group
        """
        for element in self.__users:
            print(element.get_name())

    # endregion

    # region Getters

    def get_users(self) -> List[User]:
        """
        Returns the list of the users of this group
        :return: This group users list
        :rtype: List[User]
        """
        return self.list_users

    # endregion

    # region setters

    def set_max_size(self, new_max_size: int):
        """
        set the max size of the group
        """
        self.__max_size = new_max_size

    def set_current_size(self, new_current_size: int):
        """
        set the current size of the group
        """
        self.__current_size = new_current_size

    def set_users(self, new_users_list: int):
        """
        set the list of group's users
        """
        self.__users = new_users_list

    # endregion
