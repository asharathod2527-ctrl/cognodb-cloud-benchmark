import matplotlib.pyplot as plt

networkx = {
    "Data Loading": 0.040231,
    "Graph Building": 0.199158,
    "Two-hop": 0.000082,
    "Degree Centrality": 0.021016,
    "PageRank": 0.295986,
}

neo4j = {
    "Node Count": 0.004043,
    "Relationship Count": 0.002170,
    "Degree Query": 0.051678,
    "Outgoing Query": 0.044550,
    "Two-hop": 0.025820,
}

# NetworkX graph-analysis timings
plt.figure(figsize=(10, 6))
plt.bar(networkx.keys(), networkx.values())
plt.ylabel("Time (seconds)")
plt.xlabel("Benchmark Operation")
plt.title("NetworkX Performance - soc-Pokec 120K")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("benchmark/results/networkx_performance.png", dpi=300)
plt.close()

# Neo4j query timings
plt.figure(figsize=(10, 6))
plt.bar(neo4j.keys(), neo4j.values())
plt.ylabel("Time (seconds)")
plt.xlabel("Benchmark Operation")
plt.title("Neo4j Performance - soc-Pokec 120K")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("benchmark/results/neo4j_performance.png", dpi=300)
plt.close()

print("Graphs created successfully.")