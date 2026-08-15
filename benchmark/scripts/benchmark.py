import time
import pandas as pd
import networkx as nx

DATA_FILE = r"benchmark\data\pokec-120k.txt"
RESULT_FILE = r"benchmark\results\networkx_results.txt"

print("Loading dataset...")
start = time.perf_counter()

df = pd.read_csv(
    DATA_FILE,
    sep=r"\s+",
    header=None,
    names=["source", "target"]
)

load_time = time.perf_counter() - start

print(f"Rows loaded: {len(df)}")

print("Building graph...")
start = time.perf_counter()

G = nx.from_pandas_edgelist(
    df,
    source="source",
    target="target",
    create_using=nx.DiGraph()
)

build_time = time.perf_counter() - start

nodes = G.number_of_nodes()
edges = G.number_of_edges()
density = nx.density(G)
components = nx.number_weakly_connected_components(G)

degrees = dict(G.degree())

top_degree = sorted(
    degrees.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

print("Calculating average degree...")
average_degree = sum(degrees.values()) / nodes

# Outgoing relationships
print("Calculating outgoing relationships...")
outgoing = dict(G.out_degree())

top_outgoing = sorted(
    outgoing.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

# Two-hop traversal from node 1
print("Calculating two-hop traversal...")
start = time.perf_counter()

if 1 in G:
    two_hop_nodes = set()

    for neighbor in G.successors(1):
        for second_neighbor in G.successors(neighbor):
            two_hop_nodes.add(second_neighbor)

    two_hop_count = len(two_hop_nodes)
else:
    two_hop_count = 0

two_hop_time = time.perf_counter() - start

# Degree centrality
print("Calculating degree centrality...")
start = time.perf_counter()

degree_centrality = nx.degree_centrality(G)

centrality_time = time.perf_counter() - start

top_centrality = sorted(
    degree_centrality.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

# PageRank
print("Calculating PageRank...")
start = time.perf_counter()

pagerank = nx.pagerank(G, max_iter=100)

pagerank_time = time.perf_counter() - start

top_pagerank = sorted(
    pagerank.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

results = f"""
POKEC GRAPH BENCHMARK - NETWORKX
================================

Database/Library: NetworkX
Dataset: soc-Pokec
Input file: {DATA_FILE}

Rows: {len(df)}
Nodes: {nodes}
Edges: {edges}
Density: {density}
Connected Components: {components}
Average Degree: {average_degree}

Timing
------
Data loading: {load_time:.6f} seconds
Graph building: {build_time:.6f} seconds
Outgoing relationship analysis: calculated
Two-hop traversal from node 1: {two_hop_time:.6f} seconds
Degree centrality: {centrality_time:.6f} seconds
PageRank: {pagerank_time:.6f} seconds

Two-hop traversal from node 1
-----------------------------
Nodes reached: {two_hop_count}

Top 10 Nodes by Degree
----------------------
{top_degree}

Top 10 Nodes by Outgoing Relationships
--------------------------------------
{top_outgoing}

Top 10 Nodes by Degree Centrality
---------------------------------
{top_centrality}

Top 10 Nodes by PageRank
------------------------
{top_pagerank}
"""

print(results)

with open(RESULT_FILE, "w", encoding="utf-8") as f:
    f.write(results)

print(f"Results saved to: {RESULT_FILE}")