#!/usr/bin/python3
""""script that generate a .tgz archive from the contents of the web_static"""
from fabric.api import local
import time


def do_pack():
    """generate the archive"""
    date = time.strftime('%Y%m%d%H%M%S')
    arc = 'versions/web_static_' + date + '.tgz'

    local('mkdir -p versions/')
    res = local('tar -cvzf {} web_static/'.format(arc))

    try:
        return arc
    except Exception:
        return None
