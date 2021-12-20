#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controller of the home route.
"""

from datetime import datetime
from projet_dev_ci.view import home as v


def home(request):
    """
    Handles request of the home and default route.
    """
    now = datetime.now()
    return v.home(now)
