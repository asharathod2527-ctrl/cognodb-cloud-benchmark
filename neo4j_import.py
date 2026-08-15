from neo4j import GraphDatabase
import csv
import time

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "Rathodyashoda@20"

DATA_FILE = r"C:\PokeProject\data\pokec-120k.tsv"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()
print("Connected to Neo4j")

with driver.session() as session:
    print("Clearing existing database...")
    session.run("MATCH (n) DETACH DELETE n").consume()

    print("Creating constraint...")
    try:
        session.run(
            "CREATE CONSTRAINT user_id_unique IF NOT EXISTS "
            "FOR (n:User) REQUIRE n.id IS UNIQUE"
        ).consume()
    except Exception as e:
        print("Constraint message:", e)

print("Reading dataset...")

rows = []

with open(DATA_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")

    for source, target in reader:
        rows.append({
            "source": int(source),
            "target": int(target)
        })

print(f"Rows loaded: {len(rows)}")

batch_size = 5000

start = time.perf_counter()

with driver.session() as session:

    for i in range(0, len(rows), batch_size):

        batch = rows[i:i + batch_size]

        session.run(
            """
            UNWIND $rows AS row

            MERGE (a:User {id: row.source})
            MERGE (b:User {id: row.target})

            MERGE (a)-[:FRIEND]->(b)
            """,
            rows=batch
        ).consume()

        print(
            f"Imported {min(i + batch_size, len(rows))}/{len(rows)} relationships"
        )

import_time = time.perf_counter() - start

print()
print("Import completed")
print(f"Import time: {import_time:.4f} seconds")

with driver.session() as session:

    result = session.run(
        """
        MATCH (n:User)
        RETURN count(n) AS nodes
        """
    ).single()

    nodes = result["nodes"]

    result = session.run(
        """
        MATCH ()-[r:FRIEND]->()
        RETURN count(r) AS relationships
        """
    ).single()

    relationships = result["relationships"]

print()
print("NEO4J GRAPH")
print("===========")
print(f"Nodes: {nodes}")
print(f"Relationships: {relationships}")
print(f"Import time: {import_time:.4f} seconds")

driver.close()