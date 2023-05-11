#
# <SCRIPTS..>
#   These scripts for training LLM to make what i want.
#   script infers the information of ontology, Like node, relation, property, etc..
#
# Sample cases for prompting_template
#
# case 1    : What are the presentations contatins "this_asset". 
# Answer 1  : Match (p:Presentation)-[r:CONTAINS]->(a:Asset {name: "this_asset"}) return p
#
# case 2    : 
# Answer 2  :
few_shot_examples = """
"""