import os
from neo4j import GraphDatabase

# SET NEO4J ENVIRONMENT VARIABLES
host = os.environ.get('NEO4J_URL')
user = os.environ.get('NEO4J_USER')
password = os.environ.get('NEO4J_PASS')
driver = GraphDatabase.driver(host, auth=(user, password))

# session.run Example QUERY
#   query = "CREATE (n:Person {name: $name, age: $age})"
#   parameters = {"name": "Alice", "age": 30}
#   session.run(query, parameters)
def run_query(query, parameters={}):
    with driver.session() as session:
        result = session.run(query, parameters)
        return result
    
if __name__ == '__main__':
    