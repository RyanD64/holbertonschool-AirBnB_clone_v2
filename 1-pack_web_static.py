#!/usr/bin/python3
"""

"""
from fabric.api import local
import time


def do_pack():
    """"""
    date = time.strftime('%Y%m%d%H%M%S')
    arc = 'versions/web_static_' + date + '.tgz'

    local('mkdir -p versions/')
    res = local('tar -cvzf {} web_static/'.format(arc))

    try:
        return arc
    except Exception:
        return None
