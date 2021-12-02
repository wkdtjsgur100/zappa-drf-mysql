import os
from resource_management import *

def check_rc(rc,stdout=None,stderr=None):
  if rc == 2:
    Logger.error("Code 2: Invalid argument\n%s" % stderr)
    raise InvalidArgument(stderr)
  if rc == 3:
    Logger.error("Code 3: Component is Not Running\n%s" % stderr)
    raise ComponentIsNotRunning(stderr)
  if rc > 0:
    Logger.error("Code %d: Undefined error\n%s" % (rc,stderr))
    raise Fail(stderr)