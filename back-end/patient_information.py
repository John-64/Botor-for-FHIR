from langchain.llms import LlamaCpp
import requests

# Esegui la richiesta e converte la risposta in un oggetto JSON
response = requests.get("https://hapi.fhir.org/baseR4/Patient/30163")

PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'
# Setting up the LLM for my MacBook Air M1 - 8GB
n_gpu_layers = 1
n_batch = 512
n_ctx = 2048

llm = LlamaCpp(
    model_path=PATH,
    n_gpu_layers=n_gpu_layers,
    n_ctx=n_ctx,
    n_batch=n_batch,
    temp=0.35,
    f16_kv=True,
    verbose=False
)

prompt = "Given the following patient information JSON, create a human-readable sentence describing the patient:\n" + response.text + "\nCreate a sentence that includes the patient's information."
result = llm(prompt)
print(result)
