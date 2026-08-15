import pandas as pd
import networkx as nx
from pathlib import Path

DATA_FILE = Path("data/pokec-120k.txt")
RESULT_FILE = Path("data/analysis_results.txt")

print("Loading Pokec dataset...")

df = pd.read_csv(
    DATA_FILE,
    sep=r"\s+",
    header=None,
    names=["source", "target"]
)

G = nx.from_pandas_edgelist(
    df,
    source="source",
    target="target"
)

nodes = G.number_of_nodes()
edges = G.number_of_edges()
density = nx.density(G)
components = nx.number_connected_components(G)
average_degree = sum(dict(G.degree()).values()) / nodes

degree = dict(G.degree())
top_degree = sorted(
    degree.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

degree_centrality = nx.degree_centrality(G)
top_degree_centrality = sorted(
    degree_centrality.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

pagerank = nx.pagerank(G, max_iter=100)
top_pagerank = sorted(
    pagerank.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

clustering = nx.average_clustering(G)

triangles = sum(nx.triangles(G).values()) // 3

results = f"""
POKEC NETWORK ANALYSIS
======================

Dataset: soc-Pokec
Input file: {DATA_FILE}

Nodes: {nodes}
Edges: {edges}
Density: {density}
Connected components: {components}
Average degree: {average_degree}
Average clustering coefficient: {clustering}
Total triangles: {triangles}

Top 10 nodes by degree:
{top_degree}

Top 10 nodes by degree centrality:
{top_degree_centrality}

Top 10 nodes by PageRank:
{top_pagerank}
"""

print(results)

RESULT_FILE.write_text(results, encoding="utf-8")

print(f"\nResults saved to: {RESULT_FILE}")