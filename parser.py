#import xmltodict as xd 
#from lxml import etree
import untangle
from datetime import datetime

#with open('Nn_stats_78N1K98-2_170401_112309', 'r', encoding = 'utf8') as svc_file:
#    xml_output = xd.parse(svc_file)

#print(xml_output)


#tree = etree.parse('Nn_stats_78N1K98-2_170401_112309')

#print(tree)
#diskStatsColl = tree.root()
#print(diskStatsColl)

def Nn_parser(path_to_file, upload_id):
    port_stats_list = []
    cpu_stats_list = []
    node_stats_list = []
    #system_serial = path_to_file.split('_')[3][:-2]
    obj = untangle.parse(path_to_file)
    timestamp = obj.diskStatsColl['timestamp']
    cluster_id = obj.diskStatsColl['cluster_id']
    node_port_stats = obj.diskStatsColl.port
    for element in node_port_stats:
        if element['type'] == "FC":
            port_perf = {}
            port_perf['timestamp'] = timestamp
            port_perf['upload_id'] = upload_id
            port_perf['cluster_id'] = cluster_id
            port_perf['id'] = int(element['id'])
            port_perf['type'] = element['type']
            port_perf['wwpn'] = element['wwpn']
            port_perf['cbr'] = int(element['cbr'])
            port_perf['cbt'] = int(element['cbt'])
            port_perf['cer'] = int(element['cer'])
            port_perf['cet'] = int(element['cet'])
            port_perf['hbr'] = int(element['hbr'])
            port_perf['hbt'] = int(element['hbt'])
            port_perf['her'] = int(element['her'])
            port_perf['het'] = int(element['het'])
            port_perf['lnbt'] = int(element['lnbt'])
            port_perf['lnbr'] = int(element['lnbr'])
            port_perf['lnet'] = int(element['lnet'])
            port_perf['lner'] = int(element['lner'])
            port_perf['lf'] = int(element['lf'])
            port_perf['lsy'] = int(element['lsy'])
            port_perf['lsi'] = int(element['lsi'])
            port_perf['pspe'] = int(element['pspe'])
            port_perf['ltw'] = int(element['lf'])
            port_perf['icrc'] = int(element['lsy'])
            port_perf['bbcz'] = int(element['lsi'])
            port_stats_list.append(port_perf)
    node_cpu_stats = obj.diskStatsColl.cpu_core
    for element in node_cpu_stats:
        cpu_perf = {}
        cpu_perf['timestamp'] = timestamp
        cpu_perf['upload_id'] = upload_id
        cpu_perf['cluster_id'] = cluster_id
        cpu_perf['id'] = int(element['id'])
        cpu_perf['system'] = int(element['system'])
        cpu_perf['comp'] = int(element['comp'])
        cpu_stats_list.append(cpu_perf)
    node_stats = obj.diskStatsColl.node
    for element in node_stats:
        node_perf = {}
        node_perf['timestamp'] = timestamp
        node_perf['upload_id'] = upload_id
        node_perf['cluster_id'] = cluster_id
        node_perf['id'] = element['id']
        node_perf['ro'] = int(element['ro'])
        node_perf['wo'] = int(element['wo'])
        node_perf['rb'] = int(element['rb'])
        node_perf['wb'] = int(element['wb'])
        node_perf['re'] = int(element['re'])
        node_perf['we'] = int(element['we'])
        node_perf['rq'] = int(element['rq'])
        node_perf['wq'] = int(element['wq'])
        #node_stats_list.append
    print(port_stats_list)
    print(cpu_stats_list)
    print
    return 

Nn_parser('/home/ivan/projects/xml_parser/examples/stats/v7k1/Nn_stats_78N1K98-2_170401_112309', 123456)
