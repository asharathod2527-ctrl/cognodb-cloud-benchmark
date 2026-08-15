import os
import time
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


def get_driver():
    uri = os.getenv("COGNODB_URI")
    username = os.getenv("COGNODB_USERNAME")
    password = os.getenv("COGNODB_PASSWORD")

    if not all([uri, username, password]):
        raise RuntimeError(
            "Missing COGNODB_URI, COGNODB_USERNAME, or COGNODB_PASSWORD"
        )

    return GraphDatabase.driver(uri, auth=(username, password))


def run_query(driver, query, **params):
    start = time.perf_counter()

    with driver.session() as session:
        result = session.run(query, **params)
        records = list(result)

    elapsed = time.perf_counter() - start
    return elapsed, len(records)


def main():
    driver = get_driver()

    queries = {
        "create": """
            CREATE (n:Person {id: $id, name: $name})
            RETURN n
        """,
        "read": """
            MATCH (n:Person)
            RETURN n
            LIMIT $limit
        """,
        "update": """
            MATCH (n:Person {id: $id})
            SET n.name = $name
            RETURN n
        """,
        "delete": """
            MATCH (n:Person {id: $id})
            DELETE n
        """,
    }

    try:
        print("CognоDB benchmark")
        print("-" * 40)

        elapsed, count = run_query(
            driver,
            queries["create"],
            id="benchmark-1",
            name="Benchmark User",
        )
        print(f"CREATE: {elapsed:.6f}s ({count} records)")

        elapsed, count = run_query(
            driver,
            queries["read"],
            limit=10,
        )
        print(f"READ:   {elapsed:.6f}s ({count} records)")

        elapsed, count = run_query(
            driver,
            queries["update"],
            id="benchmark-1",
            name="Updated User",
        )
        print(f"UPDATE: {elapsed:.6f}s ({count} records)")

        elapsed, count = run_query(
            driver,
            queries["delete"],
            id="benchmark-1",
        )
        print(f"DELETE: {elapsed:.6f}s ({count} records)")

    finally:
        driver.close()


if _name_ == "_main_":
    main()
