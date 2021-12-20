#! /usr/bin/env python3
# -*- coding: utf-8 -*-
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
