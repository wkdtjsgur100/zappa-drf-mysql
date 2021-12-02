from resource_management import *
from kazoo.client import KazooClient

config = Script.get_config()
zookeeper_server_hosts = str(default("/configurations/kafka-server-properties/zookeeper.connect",None))
kafka_broker_hosts = default("/clusterHostInfo/kafka_broker_hosts",[])
log_dirs = default("/configurations/kafka-server-properties/log.dirs","")

ganglia_server_hosts = default('/clusterHostInfo/ganglia_server_host', [])
kafka_conf = default("/configurations/kafka-server-properties",[])

has_ganglia_server = not len(ganglia_server_hosts) == 0
if has_ganglia_server:
  gmondServer = ganglia_server_hosts[0]
  jmxPort = default("/configurations/kafka-env/jmxPort","9999")
  gmondPort = default("/configurations/kafka-broker/kafka.ganglia.metrics.port", 8671)


hostname = None
if config.has_key('hostname'):
  hostname = str(config['hostname'])

znode_kafka_path=str(default("/configurations/kafka-env/znode_path","/ambari/kafka"))
kafka_id=None

zk = KazooClient(hosts=zookeeper_server_hosts)
zk.start()

lock = zk.Lock("/kafka-lock", hostname)
lock.acquire(timeout=60)

if zk.exists(znode_kafka_path+'/brokers/'+hostname):
  kafka_id=int(zk.get(znode_kafka_path+'/brokers/'+hostname)[0])
else:
  kafka_id=int(zk.create(znode_kafka_path+'/ids/',sequence=True,value=hostname,makepath=True).rsplit('/',1)[1])
  zk.create(znode_kafka_path+'/brokers/'+hostname,value=str(kafka_id),makepath=True)
lock.release()
zk.stop()