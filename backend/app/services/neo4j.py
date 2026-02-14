import os
from neo4j import GraphDatabase
from typing import Dict, Any

class Neo4jService:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "password")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label: str, name: str, properties: Dict[str, Any]):
        with self.driver.session() as session:
            result = session.execute_write(self._create_and_return_node, label, name, properties)
            return result

    @staticmethod
    def _create_and_return_node(tx, label, name, properties):
        # Sanitize label (Cypher doesn't allow parameters for labels)
        # In prod, validate label rigorously against allowed list
        query = (
            f"MERGE (n:{label} {{name: $name}}) "
            "SET n += $properties "
            "RETURN n, elementId(n) as id"
        )
        result = tx.run(query, name=name, properties=properties)
        record = result.single()
        if record:
            node = record["n"]
            properties = dict(node)
            properties["id"] = record["id"]
            properties["label"] = label # explicit return
            return properties
        return None

neo4j_service = Neo4jService()
