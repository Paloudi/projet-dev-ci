#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the user models
"""
from django.db import models


class User(models.Model):
    """
    An user represent... an user.
    An user has a name
    """

    name = models.TextField()
    has_a_group = models.BooleanField()

    class Meta:
        """
        Class used to modify this models table information in the database
        """
        db_table = "users"
        app_label = "projet_dev_ci"

    def __init__(self, name: str) -> None:
        """
        Creates a new User object with a given name
        :param name: The name of this user
        :type name: str
        """
        super().__init__()
        if name and isinstance(name, str):
            self.__name = name
        self.__has_a_group = True

    def get_name(self) -> str:
        """
        Returns the name of this user
        :return: this user name
        :rtype: str
        """
        return self.__name

    def get_has_a_group(self) -> bool:
        """
        Return a boolean which indicates if the user is in a group or not
        :return: this boolean "has_a_group"
        :rtype: bool
        """
        return self.__has_a_group

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
