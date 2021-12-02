
from resource_management import *
import multiprocessing
cpu_count = multiprocessing.cpu_count()

config = Script.get_config()


cluster_name = config['clusterName']
hostname = config['hostname']
security_enabled = config['configurations']['cluster-env']['security_enabled']
realm = config['configurations']['cluster-env']['kerberos_domain']


cassandra_hosts = ",".join([str(elem) for elem in default('/clusterHostInfo/cassandra_hosts',[])])

tokens = default('/configurations/cassandra/tokens',256)
cassandra_data_path = list(str(config['configurations']['cassandra']['cassandra_data_path']).split(","))
cassandra_commit_log = config['configurations']['cassandra']['cassandra_commit_log']
storage_port = config['configurations']['cassandra']['storage_port']
native_transport_port = config['configurations']['cassandra']['native_transport_port']
rpc_port = config['configurations']['cassandra']['rpc_port']
rpc_max_threads = config['configurations']['cassandra']['rpc_max_threads']
endpoint_snitch = config['configurations']['cassandra']['endpoint_snitch']
rack = config['configurations']['cassandra']['rack']
datacenter = config['configurations']['cassandra']['datacenter']

cassandra_user = default('/configurations/cassandra-env/cassandra_user','cassandra')