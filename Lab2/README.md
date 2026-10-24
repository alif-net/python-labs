# Lab 2: The Multi-Cluster IP Audit Tool

**File:** `cluster_audit.py`

A small audit tool that reads a cluster's configuration, counts its active nodes with a loop, and reports how much of the cluster's capacity is in use.

## How it works

1. **Data:** the cluster is described in a nested dictionary (`cluster_config`): its name, the total number of node slots, and a list of active node IP addresses
2. **Count:** `calculate_capacity()` loops over the `active_nodes` list, prints each IP and counts it
3. **Calculate:** utilization = (active nodes / total max slots) x 100
4. **Report:** prints a summary with f-strings

## Run it

```bash
python3 cluster_audit.py
```

## Example output

```
Found node: 10.0.1.15
Found node: 10.0.1.16
Found node: 10.0.1.17
Found node: 10.0.1.18
Found node: 10.0.1.19

Cluster:      dhaka-prod-east
Active nodes: 5 of 8 slots
Utilization:  62.5%
```

## Concepts practised

- Lists and dictionaries, including a list nested inside a dictionary
- Reading values from a dictionary by key
- A `for` loop with a counter
- Division and percentages
- Defining and calling a function
- f-strings for formatted output

## Tested cases

| Active nodes | Total slots | Utilization |
|---|---|---|
| 5 | 8 | 62.5% |
| 4 | 8 | 50.0% |
| 5 | 10 | 50.0% |
