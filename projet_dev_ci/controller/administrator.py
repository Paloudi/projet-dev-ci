#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import string
from projet_dev_ci.model.group import Group
from projet_dev_ci.model.user import User
from typing import List


"""
Controller of the administrator route.
"""

from datetime import datetime
from projet_dev_ci.view import administrator as v


def home(request):
    """
    Handles request of the administrator route.
    """
    now = datetime.now()
    return v.home(now)

def group_gestion(self, group : Group):
    if group.get_last_param == "LAST_MIN":
        

