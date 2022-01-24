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

    class Meta:
        db_table = "users"
