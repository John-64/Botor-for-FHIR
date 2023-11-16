from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import LlamaCpp
from llama_cpp import Llama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-v0.1.Q6_K.gguf'

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

prompt = """
Question: {question}?
"""

llm = LlamaCpp(
    model_path=PATH, callback_manager=callback_manager, temperature = 0.35, verbose=True
)

print(llm("What is the date of twin tower attack?"))