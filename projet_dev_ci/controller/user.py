#! /usr/bin/env python3
# -*- coding: utf-8== -*-
"""
Controller of the administrator route.
"""

from datetime import datetime
from projet_dev_ci.view import user as v


def home():
    """
    Handles request of the user route.
    """
    now = datetime.now()
    return v.home(now)
