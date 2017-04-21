import untangle

def system_info(path_to_file):
    obj = untangle.parse(path_to_file)
    timestamp = obj.diskStatsColl['timestamp']
    cluster_id = obj.diskStatsColl['cluster_id']
    return (timestamp, cluster_id)


def Nn_parser(path_to_file, upload_id):
    port_stats_list = []
    cpu_stats_list = []
    node_stats_list = []
    obj = untangle.parse(path_to_file)
    timestamp, cluster_id = system_info(path_to_file)
    #Parsing node port statistics:
    node_port_stats = obj.diskStatsColl.port
    for element in node_port_stats:
        if element['type'] == "FC":
            port_perf = {
            'timestamp': timestamp,
            'upload_id': upload_id,
            'cluster_id': cluster_id
            }
            port_perf_counters = ['id', 'type', 'wwpn', 'cbr', 'cbt', 'cer', 'cet', 
            'hbr', 'hbt', 'her', 'het', 'lnbt', 'lnbr', 'lnet', 'lner', 'lf', 'lsy',
            'lsi', 'pspe', 'itw', 'icrc', 'bbcz']
            for counter in port_perf_counters:
                if counter == 'type' or counter =='wwpn':
                    port_perf[counter] = element[counter]
                else:
                    port_perf[counter] = int(element[counter])
        port_stats_list.append(port_perf)    
    #Parsing node CPU statistics:
    node_cpu_stats = obj.diskStatsColl.cpu_core
    for element in node_cpu_stats:
        cpu_perf = {
            'timestamp': timestamp,
            'upload_id': upload_id,
            'cluster_id': cluster_id
            }
        cpu_perf_counters = ['id', 'system', 'comp']
        for counter in cpu_perf_counters:
            cpu_perf[counter] = element[counter]
        cpu_stats_list.append(cpu_perf)
    #Parsing node statistics:
    node_stats = obj.diskStatsColl.node
    for element in node_stats:
        node_perf = {
            'timestamp': timestamp,
            'upload_id': upload_id,
            'cluster_id': cluster_id
            }
        
        node_perf_counters = ['id', 'ro', 'wo', 'rb', 'wb', 're', 'we', 'rq', 'wq']
        for counter in node_perf_counters:
            if counter == 'id':
                node_perf[counter] = element[counter]
            else:
                node_perf[counter] = int(element[counter])
        node_stats_list.append(node_perf)
    return (port_stats_list, cpu_stats_list, node_stats_list)


def Nd_parser(path_to_file, upload_id):
    disk_stats_list = []
    obj = untangle.parse(path_to_file)
    timestamp, cluster_id = system_info(path_to_file)
    disk_stats = obj.diskStatsColl.mdsk
    for element in disk_stats:
        disk_perf = {
        'timestamp': timestamp,
        'upload_id': upload_id,
        'cluster_id': cluster_id
        }
        disk_perf_counters = ['idx', 'ro', 'rb', 'wo', 're', 'we', 'rq', 'wq', 'ure',
         'uwe', 'urq', 'uwq', 'pre', 'pwe', 'pro', 'pwo']
        for counter in disk_perf_counters:
            disk_perf[counter] = int(element[counter])
        disk_stats_list.append(disk_perf)
    return disk_stats_list


def Nm_parser(path_to_file, upload_id):
    mdisk_stats_list = []
    obj = untangle.parse(path_to_file)
    timestamp, cluster_id = system_info(path_to_file)
    mdisk_stats = obj.diskStatsColl.mdsk
    for element in mdisk_stats:
        mdisk_perf = {
        'timestamp': timestamp,
        'upload_id': upload_id,
        'cluster_id': cluster_id
        }
        mdisk_perf_counters = ['idx', 'idd', 'ro', 'wo', 'rb', 'wb', 're', 'we', 'rq',
        'wq', 'ure', 'uwe', 'urq', 'uwq', 'pre', 'pwe', 'pro', 'pwo']
        for counter in mdisk_perf_counters:
            mdisk_perf[counter] = element[counter]
        mdisk_stats_list.append(mdisk_perf)
    return mdisk_stats_list

def Nv_parser(path_to_file, upload_id):
    vdisk_stats_list = []
    obj = untangle.parse(path_to_file)
    timestamp, cluster_id = system_info(path_to_file)
    vdisk_stats = obj.diskStatsColl.vdsk
    for element in vdisk_stats:
        vdisk_perf = {
        'timestamp': timestamp,
        'upload_id': upload_id,
        'cluster_id': cluster_id
        }
        vdisk_perf_counters = ['idx', 'ctps', 'ctrhs', 'ctrhps', 'ctds', 'ctwfts', 
        'ctwwts', 'ctwfws', 'ctwhs', 'cv', 'cm', 'ctws', 'ctrs', 'ctr', 'ctw', 'ctp',
        'ctrh', 'ctrhp', 'ctd', 'ctwft', 'ctwwt', 'ctwfw', 'ctwfwsh', 'ctwfwshs',
        'ctwh', 'gwot', 'gwo', 'gws', 'gwl', 'id', 'ro', 'wo', 'wou', 'rb', 'wb', 'rl',
        'wl', 'rlw', 'wlw', 'xl']
        for counter in vdisk_perf_counters:
            if counter == 'id':
                vdisk_perf[counter] = element[counter]
            else:
                vdisk_perf[counter] = int(element[counter])
        vdisk_stats_list.append(vdisk_perf)
    return vdisk_stats_list