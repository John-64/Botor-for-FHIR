import flask
import requests
import json
from openai import OpenAI
from llama_cpp import Llama

app = flask.Flask(__name__)

# Defining a function for extract the main information from a question made in natural language and return a FHIR query
def generate_query(question):
    # Insert here you API key
    API_KEY = "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"

    # Check out all the models here: https://platform.openai.com/docs/models/overview
    GPT_MODEL = "gpt-3.5-turbo-1106"

    # Setting up the client
    client = OpenAI(api_key = API_KEY)

    # Prompt for OpenAI
    messages = [
        {"role": "system", "content": 'Follow this form for build the query: "https://hapi.fhir.org/baseR4/replace-with-information"'
        },
        {"role": "user", "content": question},
        {"role": "system", "content": 'Now study the request and give me just the query, without other symbols or explaination (that because i will save it in a variabile). Replace the information you want to add in "replace-with-information". If you are not able, return "It is not possible to fulfill your request, please try again with a more specific question."'
        },
    ]

    # Get the answer
    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        max_tokens=50,
        temperature=0
    )

    query = response.choices[0].message.content

    return query

# This function will help me to understand if i can print the chart or text
def check_json_fields(json_data):
    try:
        # Load the JSON
        data = json.loads(json_data)

        # Check if "entry" is in to JSON
        if 'entry' in data:
            for entry in data['entry']:
                if 'resource' in entry and 'effectiveDateTime' in entry['resource'] and 'valueQuantity' in entry['resource']:
                    return True
            # If not
            return False
        else:
            # If yes
            return False

    except json.JSONDecodeError as e:
        print(f"Error during the JSON parsing: {e}")
        return False

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/process', methods=['POST']) 
def process():
    # Taking the question from the user
    data = flask.request.get_json()
    question = data['value']

    query = generate_query(question)
    print("This is the query created by OpenAI: " + query) ## Just testing

    # Check if the user have asked something different from the chatbot operating field
    if query != "It is not possible to fulfill your request, please try again with a more specific question.":
        # Server resource fetching
        json_answer = requests.get(query)

        if check_json_fields(json_answer.text):
            data = json_answer.json()
            array = []

            # Iterate through observations in the JSON
            for entry in data.get('entry', []):
                info_data = entry.get('resource', {})

                # Extract the desired values ​​for each observation
                id = info_data.get('id', '')
                status = info_data.get('status', '')
                code_text = info_data.get('code', {}).get('text', '')
                effective_date_time = info_data.get('effectiveDateTime', '')
                value = info_data.get('valueQuantity', {}).get('value', '')
                unit = info_data.get('valueQuantity', {}).get('unit', '')

                # Add to the array
                value = [id, status, code_text, effective_date_time, value, unit]
                array.append(value)

            return flask.jsonify(result="none", graph=array)
        else:
            # Chagne with your desired model path 
            model_path='/Users/gianni/Progetti/LLM Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'

            # Setting up the LLM
            model = Llama(model_path = model_path,
                        n_ctx = 2048,          
                        n_gpu_layers = 1,       
                        use_mlock = True
                    )   
            
            # Variable containing the textual JSON for greater readability
            json_text = json_answer.text

            # Prompt for LLM including the JSON requested
            prompt = f"""
            [INST]<<SYS>>
            You are a helpful, respectful and honest medical assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

            Given the following patient information JSON, create a human-readable sentence describing the patient:

            {json_text}

            Create a sentence that includes the patient's information.
            [/INST]
            """
            # Generating the answer
            output = model(prompt = prompt, max_tokens = 250, temperature = 0.5)
             # Variable containing the response for greater readability
            result = output['choices'][0]['text']

            return flask.jsonify(result=result, graph="none")
    else:
        return flask.jsonify(result=query, graph="none")
    
if __name__ == '__main__':
    app.debug = True
    # You can change the port as you prefer
    app.run(host='0.0.0.0', port=9000, threaded=True)