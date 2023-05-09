# QueryGPT
## Make database query from natural language
You can generate query from natural language for querying database. (especially knowledge graph)

> 현재 테스트 단계이므로 맞춤형 서비스만 제공할 수 있는 상태입니다.
> Does not performed for General purpose.

Like this.
```
'Madonna가 출현한 영화' >> MATCH (p:Person {name:"Madonna"})-[r:ACTED_IN]->(m:Movie) RETURN {movie: m.title} AS result
```
This generates a Cypher query that matches the given sentence using the LLM.

## Environment and Requirements
+ Windows 10
+ Python3 (3.10.11)
+ openAI  Key

## Installation
```
pip install requirements.txt
```

Test Graph Structure
![image](https://user-images.githubusercontent.com/26298389/237041908-c0b409a3-6d2f-4972-af77-4afb99345d08.png)
