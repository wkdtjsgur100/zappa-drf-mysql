from resource_management import *
from kafka_handler import kafka
from subprocess import *


class Kafka(Script):
    def install(self, env):
        self.install_packages(env)


    def start(self, env):
        import params
        env.set_params(params)

        self.configure(env)
        kafka(action='start')

    def stop(self, env):
        import params
        env.set_params(params)

        kafka(action='stop')

    def configure(self, env):
        import params
        env.set_params(params)

        kafka(action='config')

    def status(self, env):
        kafka(action='status')

    def rebalance(self, env):
        import params
        executed = Popen(
            ["/usr/lib/kafka/bin/kafka-preferred-replica-election.sh", "--zookeeper", params.zookeeper_server_hosts],
            stdout=PIPE, stderr=PIPE)
        out, err = executed.communicate()
        Logger.info("Kafka rebalancing:")
        Logger.info(out)
        Logger.info(err)

    def repartition(self, env):
        Logger.info("Kafka rebalancing: Not yet implemented")



if __name__ == "__main__":
    Kafka().execute()