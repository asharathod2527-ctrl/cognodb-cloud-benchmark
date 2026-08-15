from neo4j import GraphDatabase
import time
from pathlib import Path

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "Rathodyashoda@20"

RESULT_FILE = Path("benchmark/results/neo4j_results.txt")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()
print("Connected to Neo4j")


def run_query(query):
    with driver.session() as session:
        start = time.perf_counter()
        result = session.run(query)
        records = result.data()
        elapsed = time.perf_counter() - start
        return records, elapsed


print("\nNEO4J GRAPH BENCHMARK")
print("=====================")

# Count nodes
nodes_result, nodes_time = run_query(
    "MATCH (n) RETURN count(n) AS nodes"
)
nodes = nodes_result[0]["nodes"]

# Count relationships
relationships_result, relationships_time = run_query(
    "MATCH ()-[r]->() RETURN count(r) AS relationships"
)
relationships = relationships_result[0]["relationships"]

# Top nodes by degree
degree_result, degree_time = run_query(
    """
    MATCH (n)
    RETURN n.id AS id, count { (n)--() } AS degree
    ORDER BY degree DESC
    LIMIT 10
    """
)

# Top nodes by outgoing relationships
outgoing_result, outgoing_time = run_query(
    """
    MATCH (n)
    RETURN n.id AS id, count { (n)-[:FRIEND]->() } AS outgoing
    ORDER BY outgoing DESC
    LIMIT 10
    """
)

# Two-hop traversal
twohop_result, twohop_time = run_query(
    """
    MATCH (n {id: 1})-[:FRIEND]->()-[:FRIEND]->(x)
    RETURN count(DISTINCT x) AS nodes
    """
)

results = f"""
NEO4J GRAPH BENCHMARK
=====================

Database: Neo4j
Dataset: soc-Pokec
Relationships: FRIEND

Nodes: {nodes}
Relationships: {relationships}

Timing
------
Node count: {nodes_time:.6f} seconds
Relationship count: {relationships_time:.6f} seconds
Degree query: {degree_time:.6f} seconds
Outgoing relationship query: {outgoing_time:.6f} seconds
Two-hop traversal: {twohop_time:.6f} seconds

Top 10 Nodes by Degree
----------------------
{degree_result}

Top 10 Nodes by Outgoing FRIEND Relationships
-----------------------------------------------
{outgoing_result}

Two-hop traversal from node 1
-----------------------------
{twohop_result}
"""

print(results)

RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
RESULT_FILE.write_text(results, encoding="utf-8")

print(f"Results saved to: {RESULT_FILE}")

driver.close()