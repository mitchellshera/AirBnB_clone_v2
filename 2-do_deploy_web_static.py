#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers.
"""
from fabric.api import env, run, put, local
import os

env.hosts = ['54.237.9.28', '3.85.196.6']
env.user = 'ubuntu'
env.key_filename = '/home/shera/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the target directory for the new version
        release_folder = "/data/web_static/releases/{}".format(
            os.path.splitext(os.path.basename(archive_path))[0])
        run("mkdir -p {}".format(release_folder))

        # Uncompress the archive to the target directory
        run("tar -xzf /tmp/{} -C {}".format(
            os.path.basename(archive_path), release_folder))

        # Remove the archive from the web server
        run("rm /tmp/{}".format(os.path.basename(archive_path)))

        # Move the contents of the new version to the appropriate location
        run("mv {}/web_static/* {}/".format(release_folder, release_folder))

        # Remove the now-empty web_static folder
        run("rm -rf {}/web_static".format(release_folder))

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
