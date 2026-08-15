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



\## Results



\### Neo4j



\- Node count: 0.036605 seconds

\- Relationship count: 0.028388 seconds

\- Degree query: 0.461818 seconds

\- Outgoing relationship query: 0.258774 seconds

\- Two-hop traversal: 0.323748 seconds



\### NetworkX



\- Data loading: 0.067743 seconds

\- Graph building: 0.320425 seconds

\- Two-hop traversal: 0.000141 seconds

\- Degree centrality: 0.030461 seconds

\- PageRank: 0.445548 seconds



\## Conclusion



Neo4j provides persistent graph storage and database-based graph querying, making it suitable for graph database workloads.



NetworkX provides an in-memory Python-based approach, making it suitable for graph algorithms, experimentation, and analysis.



The benchmark demonstrates that both tools can produce consistent graph-analysis results, while their strengths differ according to the workload and application requirements.



\## Project Structure



\- benchmark/ — benchmark scripts and results

\- config/ — configuration files

\- data/ — datasets and analysis files

\- results/ — benchmark outputs

\- analysis.py — analysis script

\- comparison.py — comparison script

\- neo4j\_import.py — Neo4j data import

\- app.py — application script



\## Running the Benchmark



Create and activate a Python virtual environment, install the dependencies from requirements.txt, and run the benchmark scripts in benchmark/scripts/.



\## Author



Asha Rathod





\## Graph Visualization



A representative subgraph of the soc-Pokec dataset is shown below.



!\[Pokec Graph Visualization](benchmark/results/pokec\_graph.png)

