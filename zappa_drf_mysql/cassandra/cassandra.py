import os

from resource_management import *
from subprocess import *
from utils import check_rc


def cassandra(action=None):
    if action == 'start' or action == 'stop' or action == 'status':
        cmd = Popen(['service', 'cassandra', action], stdout=PIPE, stderr=PIPE)
        out, err = cmd.communicate()
        Logger.info('Cassandra action: %s.\nSTDOUT=%s\nSTDERR=%s' % (action, out, err))
        if action == 'start' or action == 'status':
            check_rc(cmd.returncode, stdout=out, stderr=err)

    if action == 'config':
        import params
        File('/etc/cassandra/conf/cassandra.yaml',
             content=Template('cassandra.j2'),
             owner='cassandra',
             group='cassandra'
             )
        File('/etc/cassandra/conf/cassandra-rackdc.properties',
             content=Template('cassandra-rackdc.properties.j2'),
             owner='cassandra',
             group='cassandra'
             )