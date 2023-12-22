## Integrate our code OpenAI API
# import os
# from constants import openai_key
# from langchain.llms import OpenAI

# import streamlit as st

# os.environ["OPENAI_API_KEY"]=openai_key

# # streamlit framework

# st.title('Langchain Demo With OPENAI API')
# input_text=st.text_input("Search the topic u want")

# ## OPENAI LLMS
# llm=OpenAI(temperature=0.8)



# if input_text:
#     st.write(llm(input_text))

    


import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
import json

def get_openai_key():
    with open("keys.json") as json_file:
        data = json.load(json_file)
    return  data["openai_key"]

# os.environ["OPENAI_API_KEY"] = get_openai_key()
OpenAI.openai_api_key = get_openai_key()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain
