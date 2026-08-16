\# Graph Database Benchmarking



\## Project Overview



This project benchmarks graph data processing and analysis using Neo4j and NetworkX.



The objective is to compare a graph database system with an in-memory Python graph analysis library using the same graph dataset and benchmark operations.



\## Dataset



Dataset: soc-Pokec



Dataset size: 120K relationships



Nodes: 60,454



Relationships: 120,000



The large raw relationship dataset is not stored in this repository because of GitHub file-size limitations.



\## Technologies



\- Python

\- Neo4j

\- NetworkX

\- Cypher

\- Pandas

\- Matplotlib

\- Git and GitHub



\## Benchmark Operations



The benchmark evaluates:



\- Node count

\- Relationship count

\- Degree queries

\- Outgoing relationship queries

\- Two-hop graph traversal

\- Degree centrality

\- PageRank



Each benchmark was executed three times to reduce the effect of individual run variation.



\## Results



\### Neo4j — Average of 3 Runs



| Operation | Average Time |

|---|---:|

| Node count | 0.004043 s |

| Relationship count | 0.002170 s |

| Degree query | 0.051678 s |

| Outgoing relationship query | 0.044550 s |

| Two-hop traversal | 0.025820 s |



\### NetworkX — Average of 3 Runs



| Operation | Average Time |

|---|---:|

| Data loading | 0.040231 s |

| Graph building | 0.199158 s |

| Two-hop traversal | 0.000082 s |

| Degree centrality | 0.021016 s |

| PageRank | 0.295986 s |



\## Interpretation



The benchmark shows different strengths between Neo4j and NetworkX.



Neo4j provides persistent graph storage and database-oriented querying using Cypher. It performed the database query operations quickly in the measured benchmark.



NetworkX operates on an in-memory graph and showed particularly fast two-hop traversal and graph-analysis operations after the graph was loaded.



The results should not be interpreted as a universal winner because the systems have different architectures and workloads.



\## Conclusion



Neo4j is suitable for persistent graph storage, graph database workloads, and query-based graph applications.



NetworkX is suitable for in-memory graph algorithms, experimentation, analysis, and research workflows.



The benchmark demonstrates that both systems can process the same soc-Pokec graph while providing different performance characteristics depending on the operation.



\## Graphs



\### NetworkX Performance



!\[NetworkX Performance](benchmark/results/networkx\_performance.png)



\### Neo4j Performance



!\[Neo4j Performance](benchmark/results/neo4j\_performance.png)



\## Project Structure



\- benchmark/ — benchmark scripts and results

\- benchmark/scripts/benchmark.py — NetworkX benchmark

\- benchmark/scripts/neo4j\_benchmark.py — Neo4j benchmark

\- benchmark/scripts/comparison.py — final comparison calculation

\- benchmark/scripts/create\_graph.py — performance graph generation

\- benchmark/results/ — benchmark results and graphs

\- config/ — configuration files

\- data/ — datasets and analysis files

\- results/ — additional benchmark outputs

\- analysis.py — analysis script

\- neo4j\_import.py — Neo4j data import

\- app.py — application script



\## Running the Benchmark



Create and activate a Python virtual environment and install the dependencies from requirements.txt.



Run the NetworkX benchmark:



```bash

py benchmark/scripts/benchmark.py

