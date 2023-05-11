import os
import openai
from retry import retry

from prompting_template import few_shot_examples
from prompting_template import zero_shot_examples

openai.api_key = ''

for_few_shot= f"""
You are an assistant with an ability to generate Cypher queries based off example Cypher queries.
Example Cypher queries are: \n {few_shot_examples} \n
Do not response with any explanation or any other information except the Cypher query.
You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
You need to update the database using an appropriate Cypher statement when a user mentions their likes or dislikes, or what they watched already.
Do not provide any Cypher statements that can't be inferred from Cypher examples.
Inform the user when you can't infer the cypher statement due to the lack of context of the conversation and state what is the missing context.
"""

for_zero_shot= f"""
You are an assistant with an ability to generate Cypher queries based off example Cypher queries.
The Sample of Graph schema is : \n {zero_shot_examples} \n
Do not response with any explanation or any other information except the Cypher query.
You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
You need to update the database using an appropriate Cypher statement when a user mentions their likes or dislikes, or what they watched already.
Do not provide any Cypher statements that can't be inferred from Cypher examples.
Inform the user when you can't infer the cypher statement due to the lack of context of the conversation and state what is the missing context.
"""

system = for_zero_shot

@retry(tries=2, delay=5)
def generate_cypher(user_message):

    print('system : ', system)
    print('message : ', user_message)

    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": system}, {"role": "user", "content": 'Make a cypher query from \"' + user_message + '\"'}],
        temperature=0.0
    )
    response = completions['choices'][0]['message']['content']
    # Sometime the models bypasses system prompt and returns
    # data based on previous dialogue history
    if not "MATCH" in response and "{" in response:
        raise Exception(
            "GPT bypassed system message and is returning response based on previous conversation history"+ response)
    # If the model apologized, remove the first line
    if "apologi" in response:
        response = " ".join(response.split("\n")[1:])
    if "`" in response:
        response = response.split("```")[1].strip("`")
    print(response)
    return response