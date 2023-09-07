#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using the function do_deploy.
"""
from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime
import os


env.hosts = ['54.175.198.8', '52.86.56.129']

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns: Archive path or None on failure.
    """
    try:
        current_time = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            current_time.year,
            str(current_time.month).zfill(2),
            str(current_time.day).zfill(2),
            str(current_time.hour).zfill(2),
            str(current_time.minute).zfill(2),
            str(current_time.second).zfill(2)
        )
        archive_path = "versions/{}".format(archive_name)

        if not os.path.exists("versions"):
            os.mkdir("versions")

        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(
            archive_name.split(".")[0])

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}/".format(archive_name, folder_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_name))
        return True
    except Exception:
        return False
