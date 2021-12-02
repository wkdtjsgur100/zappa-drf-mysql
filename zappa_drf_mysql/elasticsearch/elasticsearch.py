import os

from resource_management import *
from subprocess import *
from utils import check_rc


def elasticsearch(action=None):
    if action == 'start' or action == 'stop' or action == 'status':
        cmd = Popen(['service', 'elasticsearch', action], stdout=PIPE, stderr=PIPE)
        out, err = cmd.communicate()
        Logger.info('Elasticsearch action: %s.\nSTDOUT=%s\nSTDERR=%s' % (action, out, err))
        if action == 'start' or action == 'status':
            check_rc(cmd.returncode, stdout=out, stderr=err)

    if action == 'config':
        File('/etc/elasticsearch/elasticsearch.yml',
             content=Template('elasticsearch.j2'),
             owner="elasticsearch",
             group="elasticsearch",
             mode=0644)