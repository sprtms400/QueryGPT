### Gvae total schema information from arrows.app
### Cypher Query based learning.
zero_shot_examples_1 = """
CREATE (n3:Object)-[:includedAt]->(n2:Asset {name: "(name of asset)", aspect_ratio: "", style: "style of asset", mood: "mood of asset", description: "", uploader: ""})-[:includes]->(n3)-[:supersetOf]->(n3)-[:subsetOf]->(n3)-[:showsTogetherWith]->(n3),
(n4:Tag {tag_id: "", tagName: ""})-[:taggedAt]->(n2)-[:hasTag]->(n4)-[:taggedAt]->(n5:Presentation {presentation_id: "", name: "", aspect_ratio: "", style: "", mood: "", description: "", uploader: ""})-[:hasTag]->(n4)-[:taggedWith]->(n4),
(n10:User {user_id: "", name: "", age: "", gender: ""})-[:looked]->(n2)-[:includedAt]->(n5)-[:includes]->(n2)<-[:purchased]-(n10)-[:looked]->(n5)-[:ownedBy]->(n10)<-[:ownedBy]-(n2),
(n5)-[:presentedAt]->(n8:Device)-[:presented]->(n5)<-[:purchased]-(n10),
(n9:Location {Type: "(ID or OD)", Coordinates: ""})-[:hasDevice]->(n8)-[:locatedAt]->(n9)-[:nearBy {distance: ""}]->(n9) 
"""

### Gvae total schema information from Human Designer
### Explain structure with Natural Langauge
### 다음은 Noe4J의 Graph Schema의 내용을 서술한것이다. ' 레이블은 Device, Location, Presentation, User, Tag, Asset, Object' 가 존재하고 각각의 프로퍼티는 다음과 같다 'Device 레이블 노드는 프로퍼티를 갖지 않는다.', 'Location 레이블 노드는 locationType, Coordinates를 프로퍼티로 갖는다', 'Presentation 레이블 노드는 'presentation_id', 'name', 'aspect_ratio', 'style', 'mood', 'description', 'uploader' 를 프로퍼티로 갖는다', 'User 레이블 노드는 user_id, name, age, gender 를 프로퍼티로 갖는다', 'Tag 레이블 노드는 'tag_id', 'tagName' 을 프로퍼티로 갖는다', 'Asset 레이블 노드는 name, aspect_ratio, style, mood, description, uploader, Subject 를 프로퍼티로 갖는다', 'Object 레이블 노드는 프로퍼티를 갖지 않는다', 이어서 노드 간의 릴레이션은 다음과 같다 'Device레이블 노드와 Location 레이블 노드는 locatedAt, hasDevice 관계를 갖는다,' 'Device레이블 노드와 Presentation 레이블 노드는 presented, presentedAt 관계를 갖는다', 'Presentation레이블 노드와 Tag 레이블 노드는 hasTag, taggedAt 관계를 갖는다', 'Presentation레이블 노드와 Asset 레이블 노드는 includes, includedAt 관계를 갖는다', 'Presentation레이블 노드와 User 레이블 노드는 ownedBy, looked, purchased 관계를 갖는다', 'Tag레이블 노드와 Asset레이블 노드는 taggedAt, hasTag 관계를 갖는다', 'User레이블노드와 Asset레이블 노드는 purchased, looked, ownedBy 관계를 갖는다', 'Asset레이블 노드와 Object레이블 노드는 includes, includedAt 관계를 갖는다', 'Location레이블노드는 Location레이블 노드와  nearBy 관계를 갖는다', 'Tag레이블노드는 Tag레이블노드와  taggedWith관계를 갖는다', 'Object레이블노드는 Object레이블노드와 supersetOf, subsetOf, showsTogetherWith 관계를 갖는다'
zero_shot_examples_2 = """
This graph schema consists of the following node labels and properties: The Device node has no properties. The Location node has 'locationType' and 'Coordinates' properties. The Presentation node has 'presentation_id', 'name', 'aspect_ratio', 'style', 'mood', 'description', and 'uploader' properties. The User node has 'user_id', 'name', 'age', and 'gender' properties. The Tag node has 'tag_id' and 'tagName' properties. The Asset node has 'name', 'aspect_ratio', 'style', 'mood', 'description', 'uploader', and 'Subject' properties. The Object node has no properties. The relationships between the nodes are as follows: The Device and Location nodes have 'locatedAt' and 'hasDevice' relationships. The Device and Presentation nodes have 'presented' and 'presentedAt' relationships. The Presentation and Tag nodes have 'hasTag' and 'taggedAt' relationships. The Presentation and Asset nodes have 'includes' and 'includedAt' relationships. The Presentation and User nodes have 'ownedBy', 'looked', and 'purchased' relationships. The Tag and Asset nodes have 'taggedAt' and 'hasTag' relationships. The User and Asset nodes have 'purchased', 'looked', and 'ownedBy' relationships. The Asset and Object nodes have 'includes' and 'includedAt' relationships. The Location node has a 'nearBy' relationship with other Location nodes. The Tag node has a 'taggedWith' relationship with other Tag nodes. The Object node has 'supersetOf', 'subsetOf', and 'showsTogetherWith' relationships with other Object nodes.
"""

### Gvae total schema information from JSON Structure
### Explain structure with JSON structure
zero_shot_examples_3 = """

"""

zero_shot_examples = zero_shot_examples_2