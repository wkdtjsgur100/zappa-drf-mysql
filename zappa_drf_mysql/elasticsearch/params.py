from resource_management import *

config = Script.get_config()

cluster_name = config['clusterName']
es_port = default('/configurations/elasticsearch/service_port',9200)
es_master_hosts = [ str(elem) for elem in config['clusterHostInfo']['elasticsearch_hosts']]
es_indexer_hosts = [ str(elem) for elem in default('/clusterHostInfo/elasticsearch_indexer_hosts',[]) ]

kibana_port = config['configurations']['kibana4']['kibana_port']
kibana_index = config['configurations']['kibana4']['kibana_index']
hostname = config['hostname']

is_es_master = hostname in es_master_hosts
is_es_master_str = str(hostname in es_master_hosts).lower()
is_es_indexer = hostname in es_indexer_hosts
is_es_indexer_str = str(hostname in es_indexer_hosts).lower()