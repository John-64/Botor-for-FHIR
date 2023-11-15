"""
from llama_cpp import Llama

llm = Llama(
    model_path="/Users/gianni/Desktop/Frontend/model/mistral-7b-v0.1.Q6_K.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    verbose=True,
)

response = llm("Year of twin towers attack?")

print(response) 
"""
from langchain.llms import CTransformers

llm = CTransformers(model='./model/wizard-vicuna-13b.Q3_K_S.gguf', model_type='mistral')

print(llm('AI is going to'))