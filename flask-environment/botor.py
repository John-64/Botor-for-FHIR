import flask
from openai import OpenAI
from langchain.llms import LlamaCpp
import requests
import json

app = flask.Flask(__name__)

# Defining a function for extract the main information from a question made in natural language and return a FHIR query
def generate_query(question):
    # Insert here you API key
    API_KEY = "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"

    # Check out all the models here: https://platform.openai.com/docs/models/overview
    GPT_MODEL = "gpt-3.5-turbo-1106"

    # Setting up the client
    client = OpenAI(api_key = API_KEY)

    messages = [
        {"role": "system", "content": 'Follow this form for build the query: "https://hapi.fhir.org/baseR4/replace-with-information"'
        },
        {"role": "user", "content": question},
        {"role": "system", "content": 'Now study the request and give me just the query, without other symbols or explaination (that because i will save it in a variabile). Replace the information you want to add in "replace-with-information". '
        },
    ]

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        max_tokens=50,
        temperature=0
    )

    query = response.choices[0].message.content

    return query

# This function will help me to understand if i can print the graph or not
def check_json_fields(json_data):
    try:
        # Carica il JSON
        data = json.loads(json_data)

        # Verifica se l'array "entry" è presente
        if 'entry' in data:
            # Itera attraverso gli oggetti in "entry"
            for entry in data['entry']:
                # Verifica se i campi necessari sono presenti in ciascun oggetto "resource"
                if 'resource' in entry and 'effectiveDateTime' in entry['resource'] and 'valueQuantity' in entry['resource']:
                    return True
            # Nessun oggetto in "entry" con i campi necessari trovato
            return False
        else:
            # Se l'array "entry" non è presente, ritorna False
            return False

    except json.JSONDecodeError as e:
        print(f"Errore durante il parsing del JSON: {e}")
        return False

def generate_chart(json):
    da = json
    return da
    #-----

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/process', methods=['POST']) 
def process():
    # Replace with the path of your model
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
        verbose=False,
        f16_kv=True
    )

     # Taking the question from the user
    data = flask.request.get_json()
    question = data['value']

    query = generate_query(question)
    print("This is the query created by OpenAI: " + query) ## Just testing

    # Server resource fetching
    json_answer = requests.get(query).text

    if check_json_fields(json_answer):
        print("Il JSON contiene effectiveDateTime e valueQuantity.") ## Just testing
        return flask.jsonify(result="Qui ci sarà il grafo")
    else:
        print("Il JSON non contiene entrambi i campi necessari.") ## Just testing
        prompt = json_answer + "\n Take this patient information and provide me with a well-composed an human-readable sentence."

        result = llm(prompt)
        print(result)
        return flask.jsonify(result=result)

    # return flask.jsonify(result=result)

if __name__ == '__main__':
    app.debug = True
    # You can change the port as you prefer
    app.run(host='0.0.0.0', port=9000, threaded=True)