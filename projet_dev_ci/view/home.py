#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse


def home(time):
    html = "<html><body>C'est maintenant : %s.</body></html>" % time
    return HttpResponse(html)
