


#Lab 2 : multi-cluster IP Audit Tool

cluster_config = {
         "cluster_name": "Germany-prod-east",
         "total_max_slot": 8,
         "active_nodes":["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18"] 
}

print(cluster_config["cluster_name"])
print(cluster_config["active_nodes"])
print(type(cluster_config["active_nodes"]))




