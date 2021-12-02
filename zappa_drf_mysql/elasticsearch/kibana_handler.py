import sys
from resource_management import *

from elasticsearch import elasticsearch
from kibana4 import kibana

import params


class KibanaHandler(Script):
    def install(self, env):
        self.install_packages(env)
        kibana(action="install")

    def configure(self, env):
        env.set_params(params)
        kibana(action='config')

    def start(self, env):
        env.set_params(params)
        if not params.is_es_master and not params.is_es_indexer:
            elasticsearch(action='config')
            elasticsearch(action='start')
        self.configure(env)
        kibana(action='start')

    def stop(self, env):
        if not params.is_es_master and not params.is_es_indexer:
            elasticsearch(action='stop')
        kibana(action='stop')

    def status(self, env):
        kibana(action='status')


if __name__ == "__main__":
    KibanaHandler().execute()