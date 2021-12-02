import os

from resource_management import *
import re
from subprocess import *


def check_rc(rc, stdout=None, stderr=None):
    if rc == 2:
        Logger.error("Code 2: Invalid argument\n%s" % stderr)
        raise InvalidArgument(stderr)
    if rc == 3:
        Logger.error("Code 3: Component is Not Running\n%s" % stderr)
        raise ComponentIsNotRunning(stderr)
    if rc > 0:
        Logger.error("Code %d: Undefined error\n%s" % (rc, stderr))
        raise Fail(stderr)


def os_mkdir(directories, owner=None, group=None, mode=0755):
    failed = []
    for path in directories.split(','):
        status = __mkdir(path, mode)
        status = __chown(path, owner, group) if status else status
        if not status:
            failed.append(path)
    return failed


def __mkdir(path, mode):
    exists = False
    try:
        os.makedirs(path, mode)
        exists = True
    except:
        # If raised exception and path exists, it is fine
        exists = os.path.exists(path)
    return exists


def __chown(path, owner, group):
    uid, gid = -1, -1

    if owner:
        from pwd import getpwnam
        try:
            uid = getpwnam(owner).pw_uid
        except:
            return False

    if group:
        from grp import getgrnam
        try:
            gid = getgrnam(group).gr_gid
        except:
            return False

    try:
        os.chown(path, uid, gid)
        return True
    except:
        return False


def __chmod(path, mode):
    try:
        os.chmod(path, mode)
        return True
    except:
        return False


def __owner_group(owner, group):
    chown = owner
    if chown:
        chown = chown + ":" + group if group else chown
    else:
        chown = ":" + group
    return chown