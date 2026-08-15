import statistics

networkx = {
    "Data loading": [0.042586, 0.038833, 0.039274],
    "Graph building": [0.207269, 0.209712, 0.180494],
    "Two-hop traversal": [0.000081, 0.000074, 0.000092],
    "Degree centrality": [0.022784, 0.021372, 0.018892],
    "PageRank": [0.330275, 0.295186, 0.262498],
}

neo4j = {
    "Node count": [0.005743, 0.002756, 0.003631],
    "Relationship count": [0.002569, 0.002110, 0.001830],
    "Degree query": [0.066693, 0.051311, 0.037030],
    "Outgoing relationship query": [0.038704, 0.058907, 0.036038],
    "Two-hop traversal": [0.022165, 0.027371, 0.027924],
}

output = []

output.append("POKEC GRAPH DATABASE BENCHMARK - FINAL COMPARISON")
output.append("=" * 55)
output.append("")
output.append("Dataset: soc-Pokec 120K")
output.append("Runs per system: 3")
output.append("")

output.append("NETWORKX AVERAGES")
output.append("-" * 20)

for name, values in networkx.items():
    output.append(
        f"{name}: {statistics.mean(values):.6f} seconds"
    )

output.append("")
output.append("NEO4J AVERAGES")
output.append("-" * 20)

for name, values in neo4j.items():
    output.append(
        f"{name}: {statistics.mean(values):.6f} seconds"
    )

output.append("")
output.append("INTERPRETATION")
output.append("-" * 20)
output.append(
    "NetworkX showed very fast in-memory two-hop traversal "
    "and graph-analysis operations."
)
output.append(
    "Neo4j showed fast database query performance for "
    "node, relationship, degree and outgoing relationship queries."
)
output.append(
    "The two systems serve different purposes: Neo4j provides "
    "persistent graph database storage and Cypher querying, "
    "while NetworkX provides in-memory graph analysis."
)

result_file = "benchmark/results/final_comparison.txt"

with open(result_file, "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("\n".join(output))
print(f"\nSaved to: {result_file}")