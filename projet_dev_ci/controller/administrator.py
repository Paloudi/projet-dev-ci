#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from projet_dev_ci.view import administrator as v


def home(request):
    now = datetime.now()
    return v.home(now)
