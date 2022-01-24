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
