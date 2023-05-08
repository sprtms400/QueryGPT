# QueryGPT
## Make database query from natural language
You can generate query from natural language for querying database. (especially knowledge graph)
Like this.
```
'Madonna가 출현한 영화' >> MATCH (p:Person {name:"Madonna"})-[r:ACTED_IN]->(m:Movie) RETURN {movie: m.title} AS result
```
This can perform

## Environment and Requirements
+ Windows 10
+ Python3 (3.10.11)
+ openAI  Key

## Installation
```
pip install requirements.txt
```
