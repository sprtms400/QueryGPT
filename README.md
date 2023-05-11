# QueryGPT
## Make database query from natural language
You can generate query from natural language for querying database. (especially knowledge graph)

>> !! 현재 테스트 단계이므로 맞춤형 서비스만 제공할 수 있는 상태입니다.

>> !! Does not performed for General purpose.

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

## Test Graph Structure
![Cublick Graph (2)](https://github.com/sprtms400/QueryGPT/assets/26298389/b1d1e210-d7fc-4bb1-ad9c-45acc74837de)


## Test Result
![image](https://github.com/sprtms400/QueryGPT/assets/26298389/4432b5fd-b1b3-4d39-8e0a-6e16a396003b)
