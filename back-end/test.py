#from gpt4all import GPT4All

#PATH='/Users/gianni/Progetti/LLM Models/wizard-vicuna-13b.Q3_K_S.gguf'

#model = GPT4All(PATH)
#output = model.generate(prompt='Give me just the the date of twin tower attack?', temp=0.5, max_tokens=20)
#print(output)


"""
import time
from gpt4all import GPT4All

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-v0.1.Q2_K.gguf'


model = GPT4All(PATH)
output = model.generate(prompt='Give me just the the date of twin tower attack?', temp=0.5, max_tokens=200)
end_time = time.time()

print(output)

generation_time = end_time - start_time
print(f"\nGeneration time: {generation_time} seconds")

import time
from gpt4all import GPT4All

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-v0.1.Q2_K.gguf'

model = GPT4All(PATH)
start_time = time.time()
output = model.generate(
    prompt='Mi dai un metodo di studio efficace?',
    temp=0.2,
    max_tokens=200
)
end_time = time.time()
print(output)
generation_time = end_time - start_time
print(f"\nGeneration time: {generation_time} seconds")

# Stampa a pezzi
#tokens = []
#for token in model.generate("The capital of France is", max_tokens=20, streaming=True):
#    tokens.append(token)
#print(tokens)



# create pieline for QA

from gpt4all import GPT4All
from llama_cpp import Llama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

PATH='/Users/gianni/Progetti/LLM Models/llama-2-7b-chat.Q2_K.gguf'
llm = Llama(model_path=PATH)
#model = GPT4All(PATH)


llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.run(question)

from langchain.llms import CTransformers

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-v0.1.Q2_K.gguf'

llm = CTransformers(model=PATH, model_type='mistral')

print(llm('AI is going to'))
"""
import time
from gpt4all import GPT4All

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'

model = GPT4All(PATH)

start_time = time.time()

#question = "Rispondi Dammi un metodo di studio efficace per lo studio all'università"

#output = model.generate(prompt="Answer this question always in the same language of the question: {Question}", temp=0.35)

question = "Come stai?"

prompt = f"Answer just at this question always in Italian: {question}"

output = model.generate(prompt=prompt, temp=0.35)

end_time = time.time()

print(output)

generation_time = end_time - start_time

print(f"\nAnswer took: %.2f seconds"%generation_time)

# Prova a implementarlo in Flask