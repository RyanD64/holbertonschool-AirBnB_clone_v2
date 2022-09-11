#!/usr/bin/python3
""""script that distributes an archive to the web servers"""
import os
import time
from fabric.api import put, run, get, local

env.hosts = ['18.215.148.114', '54.204.89.250']

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


def do_deploy(archive_path):
    """"""
    if not os.path.exists(archive_path):
        return False
    
    try:
        run()
        put(archive_path, '/tmp')
        get('tar -xf /data/web_static/releases/arc')
        get('tar -xvzf /data/web_static/releases/arc')
        run('ln -sf /data/web_static/current')
        return True
    except Exception:
        return False
