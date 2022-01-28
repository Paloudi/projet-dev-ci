#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Controller of the administrator route.
"""

from datetime import datetime
from projet_dev_ci.view import administrator as v
from projet_dev_ci.models import Group


def home(request):
    """
    Handles request of the administrator route.
    """
    request
    now = datetime.now()
    grp = Group(5)
    grp.save()
    return v.home(now)

