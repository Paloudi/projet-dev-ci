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

    # region Constructors

    def __init__(self, size: int) -> None:
        """
        Creates a new Group object with a given size
        :param size: The max size of this group
        :type size: int
        """
        super().__init__()
        if size and isinstance(size, int) and size > 0:
            self.max_size = size
            self.current_size = 0
            self.users: List[User] = []
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
            if self.max_size > self.current_size:
                self.users.append(new_user)
                self.current_size += 1

    def remove_user(self, user_to_remove: User) -> None:
        """
        Remove a user to this group
        :param user_to_remove : an user to remove from this group
        :type user_to_remove: User
        """
        if user_to_remove and isinstance(user_to_remove, User):
            user_to_remove.set_has_a_group(False)
            self.users.remove(user_to_remove)
            self.current_size -= 1

    def print_list_users(self) -> None:
        """
        Print every user from the Group
        """
        for element in self.users:
            print(element.get_name())

    # endregion

    # region Getters

    def get_users(self) -> List[User]:
        """
        Returns the list of the users of this group
        :return: This group users list
        :rtype: List[User]
        """
        return self.users

    def get_current_size(self) -> int:
        """
        Returns the current size of this group
        :return: This group current size
        :rtype: int
        """
        return self.current_size

    def get_max_size(self) -> int:
        """
        Returns the max size of this group
        :return: This group max size
        :rtype: int
        """
        return self.max_size

    # endregion

    # region setters

    def set_max_size(self, new_max_size: int):
        """
        set the max size of the group
        """
        self.max_size = new_max_size

    def set_current_size(self, new_current_size: int):
        """
        set the current size of the group
        """
        self.current_size = new_current_size

    def set_users(self, new_users_list: int):
        """
        set the list of group's users
        """
        self.users = new_users_list

    # endregion
