import os

from resource_management import *
from subprocess import *
from utils import check_rc


def kibana(action=None):
    if action == 'start' or action == 'stop' or action == 'status':
        cmd = Popen(['service', 'kibana4', action], stdout=PIPE, stderr=PIPE)
        out, err = cmd.communicate()
        Logger.info('Kibana4 action: %s.\nSTDOUT=%s\nSTDERR=%s' % (action, out, err))
        if action == 'start' or action == 'status':
            check_rc(cmd.returncode, stdout=out, stderr=err)

    if action == 'config':
        import params
        Directory('/var/log/kibana',
                  owner='kibana',
                  group='kibana',
                  mode=0550
                  )
