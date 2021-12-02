import sys
from resource_management import *

from cassandra import cassandra


class CassandraHandler(Script):
    def install(self, env):
        self.install_packages(env)

    def configure(self, env):
        import params
        env.set_params(params)
        cassandra(action='config')

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        cassandra(action='start')

    def stop(self, env):
        import params
        cassandra(action='stop')

    def status(self, env):
        cassandra(action='status')


if __name__ == "__main__":
    CassandraHandler().execute()