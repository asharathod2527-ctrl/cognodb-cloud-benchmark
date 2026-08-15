from pathlib import Path

neo4j_file = Path("benchmark/results/neo4j_results.txt")
networkx_file = Path("benchmark/results/networkx_results.txt")

neo4j = neo4j_file.read_text(encoding="utf-8")
networkx = networkx_file.read_text(encoding="utf-8")

comparison = f"""
POKEC GRAPH DATABASE BENCHMARK COMPARISON
=========================================

Dataset: soc-Pokec
Dataset size: 120K

-----------------------------------------
NEO4J RESULTS
-----------------------------------------

{neo4j}

-----------------------------------------
NETWORKX RESULTS
-----------------------------------------

{networkx}

-----------------------------------------
COMPARISON SUMMARY
-----------------------------------------

Both Neo4j and NetworkX were tested using the same
soc-Pokec 120K graph dataset.

Neo4j:
- Graph database system
- Data stored and queried using Cypher
- Suitable for persistent graph storage and graph queries

NetworkX:
- Python graph analysis library
- Graph loaded into memory
- Suitable for graph algorithms and analysis

The benchmark results above can be used to compare:
- Node and relationship statistics
- Degree analysis
- Degree centrality
- PageRank
- Query/algorithm execution time

Conclusion:
Neo4j provides a database-oriented approach for storing
and querying graph data, while NetworkX provides an
in-memory Python-based approach for graph analysis.
"""

output_file = Path("benchmark/results/comparison_results.txt")
output_file.write_text(comparison, encoding="utf-8")

print(comparison)
print(f"Comparison saved to: {output_file}")