from langchain.prompts import PromptTemplate
from llama_cpp import Llama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

PATH='/Users/gianni/Progetti/LLM Models/wizard-vicuna-13b.Q3_K_S.gguf'

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = Llama(model_path=PATH, verbose=True, temperature=0.75, max_tokens=2000, callback_manager=callback_manager)

prompt = PromptTemplate(
    input_variables=['input'],
    template="""
    ### Input:
    {input}
    """)

formatted_prompt = prompt.format(input="Question: A rap battle between Stephen Colbert and John Oliver")

response = llm(formatted_prompt)

print(response)