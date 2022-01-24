#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module storing the user model
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
        Class used to modify this model table information in the database
        """
        db_table = "users"
