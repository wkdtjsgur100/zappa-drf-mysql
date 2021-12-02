from resource_management import *
from kafka_handler import kafka
from subprocess import *


class Rebalance(Script):

    def rebalance(self, env):
        import params
        executed = Popen(["/usr/lib/kafka/bin/kafka-preferred-replica-election.sh", "--zookeeper",
                          params.zookeeper_server_hosts + '/kafka'], stdout=PIPE, stderr=PIPE)
        out, err = executed.communicate()
        Logger.info("Kafka rebalancing:")
        Logger.info(action)
        Logger.info(out)
        Logger.info(err)


if __name__ == "__main__":
    Rebalance().execute()