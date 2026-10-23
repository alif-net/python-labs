# Lab 2: The Multi-Cluster IP Audit Tool

cluster_config = {
    "cluster_name": "Germany-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18"]
}


def calculate_capacity(config):
    # TODO 1: Calculate how many items are in the active_nodes list
    active_count = 0
    for node in config["active_nodes"]:
        print(f"Found node: {node}")
        active_count = active_count + 1

    # TODO 2: Run the mathematical formula to find utilization percentage
    total_slots = config["total_max_slots"]
    utilization = (active_count / total_slots) * 100
    print(active_count, total_slots, utilization)

#Todo 3: print the status statement

    cluster_name = config["cluster_name"]

    print(f"Cluster: {cluster_name}")
    print(f"active nodes: {active_count} of {total_slots} slots")
    print(f"Utilization : {utilization}%")

calculate_capacity(cluster_config)
