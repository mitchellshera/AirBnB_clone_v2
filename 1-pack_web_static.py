#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime
import os


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


if __name__ == "__main__":
    archive = do_pack()
    if archive is not None:
        print("web_static packed: {}".format(archive))
    else:
        print("Packaging failed")
